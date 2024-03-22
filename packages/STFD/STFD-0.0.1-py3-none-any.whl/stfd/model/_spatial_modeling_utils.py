import math
import scanpy as sc
import cv2 
import numpy as np
from typing import Optional
import torch 
import matplotlib.pyplot as plt
import torch.nn.functional as F
import pandas as pd
import os
from sklearn.neighbors import KNeighborsClassifier, NearestNeighbors
from typing import List 
import copy 
from scipy.spatial import ConvexHull, Delaunay
import einops
is_squidpy_installed = False
try:
    import squidpy as sq
    is_squidpy_installed = True
except: 
    from ..externals._squidpy_spatial_variable_genes import (
        spatial_neighbors,
        spatial_autocorr,
    )
is_noise_installed = False
try:
    from noise import pnoise2
    is_noise_installed = True
except:
    pass
is_sinfonia_installed = False
try:
    import sinfonia
    is_sinfonia_installed = True
except:
    from ..externals import sinfonia

from ..utils._decorators import ignore_warning
from ..utils._utilities import FLATTEN
from ..preprocessing._preprocess import normalize_non_inplace
from ..externals.segment_anything.modeling.image_encoder import ImageEncoderViT
from ..externals.segment_anything.utils.transforms import ResizeLongestSide


def noise(size=512):
    x,y = np.meshgrid(np.arange(size),np.arange(size))
    xy = np.concatenate([ x[:,:,None],y[:,:,None] ], axis=2)
    xy =  xy
    
    z = einops.rearrange(
        np.array(list(map(lambda x: 
            pnoise2(
                np.radians(x[0]), 
                np.radians(x[1]), 
                base=52, 
                octaves=9,
                persistence=1.2,
                lacunarity=0.4, 
                repeatx=1024, 
                repeaty=1024, 
            ), 
        einops.rearrange(xy,'a b c -> (a b) c')))), '(a b) -> a b', 
        a = size, b = size
    )

    return z[None,:]

def preprocess_image(
    x: torch.Tensor,
    img_size: int,
    normalize_method: int = 0,
    pixel_mean: torch.Tensor = None, 
    pixel_std: torch.Tensor = None,
    pixel_average: torch.Tensor = None
) -> torch.Tensor:
    """Normalize pixel values and pad to a square input."""
    # Normalize colors
    if normalize_method == 0:
        x = (x - pixel_mean) / pixel_std
    else:
        x = x / 255

    # Pad
    h, w = x.shape[-2:]
    padh = img_size - h
    padw = img_size - w
    x = F.pad(x, (0, padw, 0, padh))
    if pixel_average is not None:
        mask = torch.zeros(1, 1, img_size, img_size)
        mask[:, :, :h, :w] = 1
        r = x[0,:,(mask == 0)[0,0,:]].shape[-1]
        x[0,:,(mask == 0)[0,0,:]] = torch.tensor(
            pixel_average.to(x.device) / 255 if normalize_method == 1 else pixel_average.to(x.device) * pixel_std + pixel_mean, 
            dtype=x.dtype
        ).repeat(
            r, 1
        ).T
    return x

def spatially_variable_genes(adata, n_top_genes=1000, mode="moran"):
    if not 'normalized' in adata.layers.keys():
        normalize_non_inplace(adata)
    if is_squidpy_installed:
        sq.gr.spatial_neighbors(adata)
        sq.gr.spatial_autocorr(
            adata, 
            mode=mode,
            genes=adata.var_names,
            layer='normalized'
        )
    else:
        spatial_neighbors(adata)
        spatial_autocorr(
            adata, 
            mode=mode,
            genes=adata.var_names,
            layer='normalized'
        )
    if mode == "moran":
        s = adata.uns['moranI'][
            np.array(~adata.uns['moranI']['I'].isna()) & 
            np.array(list(map(lambda x: not (
                x.startswith("MT-") or 
                x.startswith("RPS") or 
                x.startswith("RPL") or 
                x.startswith("HSP") or
                x.startswith("DNAJ")
            ), adata.uns['moranI'].index)))
        ].sort_values("I", ascending=False).index[:n_top_genes]
    elif mode == 'geary':
        s = adata.uns['gearyC'][
            np.array(~adata.uns['gearyC']['C'].isna()) & 
            np.array(list(map(lambda x: not (
                x.startswith("MT-") or 
                x.startswith("RPS") or 
                x.startswith("RPL") or 
                x.startswith("HSP") or
                x.startswith("DNAJ")
            ), adata.uns['gearyC'].index)))
        ].sort_values("C", ascending=False).index[:n_top_genes]
    adata.var['highly_variable_moranI'] = adata.var_names.isin(s)

def spatially_variable_genes_sinfonia(adata, n_top_genes=1000):
    if not 'normalized' in adata.layers.keys():
        normalize_non_inplace(adata)
    sinfonia.statistics.spatially_variable_genes(
        adata,
        n_top_genes=n_top_genes,
        layer='normalized',
    )

def sample_with_fixed_sparsity(labels, N, sparsity):
    probabilities = np.exp(-sparsity * np.arange(len(labels)))
    probabilities /= probabilities.sum()

    labels_copy = copy.copy(labels)
    np.random.shuffle(labels_copy)
    sampled_labels = np.random.choice(labels_copy, size=N, replace=True, p=probabilities)

    return sampled_labels

def compute_st_batch_variable_genes_core(
    st_adata,
    batch_key,
    min_frac,
    min_logfc
):
    if len(np.unique(st_adata.obs[batch_key])) == 1:
        return {
            st_adata.obs[batch_key].iloc[0]: np.ones(st_adata.shape[1])
        }
    sc.tl.rank_genes_groups(st_adata, groupby=batch_key, method='t-test')
    l = list(st_adata.var.index)
    result = []
    columns = list(pd.DataFrame(st_adata.uns['rank_genes_groups']['logfoldchanges']).columns)
    for i,j,k in zip(pd.DataFrame(st_adata.uns['rank_genes_groups']['logfoldchanges']).to_numpy(),
        pd.DataFrame(st_adata.uns['rank_genes_groups']['names']).to_numpy(),
        pd.DataFrame(st_adata.uns['rank_genes_groups']['pvals_adj']).to_numpy(),
    ):
        for e,(m,n,p) in enumerate(zip(i,j,-np.log10(k))):
            result.append((columns[e],m,n,p))
    result = pd.DataFrame(result, columns=['groups','logfoldchanges','gene_name','pvals_adj'])

    mask_genes = {}

    selected_genes = {}
    for i in np.unique(st_adata.obs[batch_key]):

        sel = result.loc[
            np.array(result['logfoldchanges'] > 1)  &
            np.array(result['pvals_adj'].replace(np.inf, 300) > 10) &
            np.array(result.iloc[:,0] == i),
            ['groups','gene_name']
        ]
        selected_genes[i] = list(sel['gene_name'])


    ht = sc.pl.dotplot(
        st_adata,
        np.unique(FLATTEN(selected_genes.values())),
        groupby=batch_key, 
        show=False, 
        return_fig=True
    )
    size_df = ht.dot_size_df

    for i in np.unique(st_adata.obs[batch_key]):
        mask_genes[i] = []
        m = dict(zip(
            result.loc[result['groups'] == i,'gene_name'],
            result.loc[result['groups'] == i,'logfoldchanges']
        ))
        for j in selected_genes[i]:
            if size_df.loc[i,j] > min_frac and m[j] > min_logfc:
                mask_genes[i].append(j)


    G_mask_batch = {}
    for i in np.unique(st_adata.obs[batch_key]):
        G_mask_batch[i] = np.ones(st_adata.shape[1])
        mask_indices = np.array([l.index(x) for x in mask_genes[i]])
        if len(mask_indices) > 0:
            G_mask_batch[i][mask_indices] = 0

    return G_mask_batch

def compute_st_batch_variable_genes(
    st_adata,
    batch_key: str,
    additional_batch_keys: Optional[List[str]] = None,
    min_frac: float = 0.8,
    min_logfc: float = 3.
):
    if 'normalized' not in st_adata.layers.keys():
        st_adata.layers['normalized'] = st_adata.X
        sc.pp.normalize_total(st_adata, target_sum=1e4, layer='normalized')
        sc.pp.log1p(st_adata, layer='normalized')
    
    if additional_batch_keys is None:
        G_mask_batch = compute_st_batch_variable_genes_core(
            st_adata, 
            batch_key,
            min_frac=min_frac,
            min_logfc=min_logfc
        )
        return G_mask_batch
    else:
        all_G_mask_batch = {}
        all_G_mask_batch[batch_key] = compute_st_batch_variable_genes_core(
            st_adata, 
            batch_key,
            min_frac=min_frac,
            min_logfc=min_logfc
        )
        for additional_batch_key in additional_batch_keys:
            all_G_mask_batch[additional_batch_key] = compute_st_batch_variable_genes_core(
                st_adata,
                additional_batch_key,
                min_frac=min_frac,
                min_logfc=min_logfc
            )
        return all_G_mask_batch

def filter_spatial_outlier_spots(adata: sc.AnnData, subset=True):
    coordinates = adata.obsm['spatial']
    neighbors = NearestNeighbors(n_neighbors=100)
    neighbors.fit(coordinates)
    D,I=neighbors.kneighbors(coordinates)
    distance1 = D[:,1:].mean(1)
    Q3 = np.percentile(distance1 , 99)
    outliers1 = (distance1 > Q3)
    distance2 = D[:,1:].min(1)

    Q3 = np.percentile(distance2 , 75)
    Q1 = np.percentile(distance2 , 25)
    IQR = max(np.mean(distance2) * 0.01, Q3-Q1)
    outliers2 = (distance2 > np.mean(distance2) + IQR)
    outliers = outliers1 & outliers2
    if subset:
        return adata[~outliers]
    else:
        adata.obs['is_outlier_spot'] = list(map(str, outliers))

def get_spatial_image(adata: sc.AnnData):
    spatial_key = list(adata.uns['spatial'].keys())[0]
    if 'hires' in adata.uns['spatial'][spatial_key]['images']:
        image = adata.uns['spatial'][spatial_key]['images']['hires'].copy()
        s = adata.uns["spatial"][spatial_key]["scalefactors"]["tissue_hires_scalef"]
    elif 'lowres' in adata.uns['spatial'][spatial_key]['images']:
        image = adata.uns['spatial'][spatial_key]['images']['lowres'].copy()
        s = adata.uns["spatial"][spatial_key]["scalefactors"]["tissue_lowres_scalef"]
    else:
        raise ValueError("No image found")
    if all(image.flatten() > 1):
      image = (image / 255).astype(np.float32)
    return image, s

def get_spatial_scalefactors_dict(adata: sc.AnnData):
    spatial_key = list(adata.uns['spatial'].keys())[0]
    return adata.uns['spatial'][spatial_key]['scalefactors']

def transform_spatial_image(
    adata: sc.AnnData,
    transform: ResizeLongestSide,
):
    image, s = get_spatial_image(adata)
    if all( (image <= 1).flatten() ):
        image = (image * 255).astype(np.uint8)
    image = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2RGB,
    )
    spatial_coord = adata.obsm["spatial"].copy() * s
    
    fig,ax=plt.subplots()
    ax.scatter(
        spatial_coord[:,0],
        spatial_coord[:,1]
    )
    cur_coords = np.concatenate([ax.get_xlim(), ax.get_ylim()])
    y1=(cur_coords[3]-cur_coords[2])*0.015
    x1=(cur_coords[1]-cur_coords[0])*0.015
    cur_coords[2] += y1
    cur_coords[3] -= y1
    cur_coords[0] += x1
    cur_coords[1] -= x1
    plt.close()
    # cur_coords[0] -= max(image.shape[0] * 0.1, 0)
    # cur_coords[1] += min(image.shape[0] * 0.1, image.shape[0])
    # cur_coords[2] -= max(image.shape[1] * 0.1, 0)
    # cur_coords[3] += min(image.shape[1] * 0.1, image.shape[1])
    
    new_image = image[
        (np.arange(image.shape[0]) > cur_coords[2]) & (np.arange(image.shape[0]) < cur_coords[3]),
        :
    ][:,(np.arange(image.shape[1]) > cur_coords[0]) & (np.arange(image.shape[1]) < cur_coords[1])]

    pixel_mean = einops.rearrange(
        image[
            (np.arange(image.shape[0]) < cur_coords[2]) | (np.arange(image.shape[0]) > cur_coords[3]),
            :
        ][:,(np.arange(image.shape[1]) < cur_coords[0]) | (np.arange(image.shape[1]) > cur_coords[1])
    ], 'a b c -> (a b) c').mean(0)
    
    spatial_coord[:,0] -= np.argwhere((np.arange(image.shape[0]) > cur_coords[0]) & (np.arange(image.shape[0]) < cur_coords[1])).min() 
    spatial_coord[:,1] -= np.argwhere((np.arange(image.shape[1]) > cur_coords[2]) & (np.arange(image.shape[1]) < cur_coords[3])).min()

    original_shape = new_image.shape[:2]
    image_coord = np.meshgrid(np.arange(new_image.shape[1]), np.arange(new_image.shape[0]))
    image_coord = np.stack(image_coord, -1)
    image_coord = transform.apply_coords(image_coord, original_shape)
    image = transform.apply_image(new_image)
    spatial_coord = transform.apply_coords(spatial_coord, original_shape)

    return image, image_coord, spatial_coord, original_shape, s, pixel_mean

def preprocess_spatial_image(x: torch.Tensor, img_size: int) -> torch.Tensor:
    # Pad
    h, w = x.shape[-2:]
    padh = img_size - h
    padw = img_size - w
    x = F.pad(x, (0, padw, 0, padh))
    return x

def get_spatial_condition(
    adata: sc.AnnData,
    condition_key: str, 
    spatial_coord: np.ndarray, 
    image_size: int
):
    assert condition_key in adata.obs.columns
    
    if len(np.unique(adata.obs[condition_key])) == 1:
        return adata.obs[condition_key].iloc[0]
    else:
        coordinates, spatial_mask = get_spatial_mask(
            image_size, spatial_coord
        )
        conditions = list(map(lambda x: x+1,pd.Categorical(adata.obs[condition_key]).codes))
        knc = KNeighborsClassifier(n_neighbors=1)
        knc.fit(spatial_coord, conditions)
        result = knc.predict(einops.rearrange(
            coordinates,
            'w h c -> (w h) c'
        )).reshape(image_size, image_size)
        result[spatial_mask] = 0
        return result


def get_spatial_mask(
    img_size:int,
    spatial_coord: np.ndarray,
    n_neighbors: int = 1
):
        coordinates = np.indices((
            img_size,img_size
        )).transpose(1, 2, 0)
        coordinates_flat = einops.rearrange(coordinates, 'a b c -> (b a) c')

        neighbors = NearestNeighbors(n_neighbors=n_neighbors)
        neighbors.fit(spatial_coord)

        D, I = neighbors.kneighbors(coordinates_flat)

        mask_d = (D.min(1) > 20 * (img_size // 1024)).reshape((
            img_size,img_size
        )).astype(np.uint8)

        mask = np.zeros(mask_d.shape, dtype=np.bool)
        mask_final = np.zeros(mask_d.shape)
        
        hull = Delaunay(spatial_coord)
        mask[(hull.find_simplex(coordinates) == -1).reshape((
            img_size,img_size
        ))] = True

        contours, _ = cv2.findContours(mask_d, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(mask_final, contours, -1, (255,255,255), cv2.FILLED)
        mask = ~np.bitwise_and(~mask.astype(np.bool).T, mask_final.astype(np.bool)) 
        return coordinates, mask



def convert_to_istar(adata: sc.AnnData, output_path: str):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    image, image_coord, spatial_coord, original_shape, s, pixel_mean = transform_spatial_image(
        adata,
        ResizeLongestSide(4096)
    )
    # image = preprocess_spatial_image(image, 4096)
    spot = list(map(lambda x: f'{x[0]}x{x[1]}', adata.obs.loc[:,['x','y']].to_numpy()))
    cnts = pd.DataFrame(adata.X.toarray(), index=spot, columns=adata.var_names)
    cnts.index.name = 'spot'
    locs_raw = pd.DataFrame(adata.obsm['spatial'], index=spot, columns=['x','y'])
    locs_raw.index.name = 'spot'
    scale_factors = get_spatial_scalefactors_dict(adata)

    cnts.to_csv(os.path.join(output_path,"cnts.tsv"), sep='\t')
    locs_raw.to_csv(os.path.join(output_path,"locs-raw.tsv"), sep='\t')
    plt.imsave(os.path.join(output_path,"he-raw.jpg"), image)
    with open(os.path.join(output_path,"radius-raw.txt"), "w+") as f:
        f.write(str(scale_factors["spot_diameter_fullres"]) + '\n')
    with open(os.path.join(output_path,"pixel-size-raw.txt"), "w+") as f:
        f.write("0.25\n")

