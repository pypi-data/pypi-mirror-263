import scanpy as sc
import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
from ..utils._compat import Literal
from ..model._spatial_modeling_utils import (
    get_spatial_scalefactors_dict, 
    get_spatial_image
)

def hex_to_rgb(value: str):
    assert(value[0] == '#' and len(value) in [7])
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) / 255 for i in range(0, lv, lv // 3))

def filter_valid_spots(
    adata: sc.AnnData,
    min_spots: int
):
    all_prediction_types = np.unique(adata.obs['celltype_predict'])
    valid_spots = []
    for i in all_prediction_types:
        num_spots = np.sum(adata.obs['celltype_predict'] == i)
        if num_spots >= min_spots:
            valid_spots.append(i)
    return valid_spots

def plot_spatial_deconvolution(
    adata: sc.AnnData, 
    palettes: dict, 
    min_spots: int, 
    img_alpha:float=0.5,
    show_color_bar=True,
    palette: dict = None,
    s=10,
    show=False,
    ax=None,
    layout: Literal['piechart','gradient'] = 'gradient'
):
    spatial_coord = adata.obsm["spatial"].copy()
    #fig, (ax1,ax2) = plt.subplots(1,2,figsize=(5,5))
    #fig.set_size_inches(10, 5) 
    if ax is None:
        fig, ax1 = plt.subplots(figsize=(5,5))
    else:
        ax1=ax
    img,scale=get_spatial_image(adata)
    ax1.imshow(img, alpha=img_alpha)
    xlim = ax1.get_xlim()
    ylim = ax1.get_ylim()
    valid_spots = filter_valid_spots(adata, min_spots)
    if isinstance(list(palettes.values())[0], str):
        palettes = {k:hex_to_rgb(v) for k,v in palettes.items()}
    if layout == 'piechart':
        c = list(adata.obs.columns).index('celltype_predict_proportions')
        for e,(x,y) in enumerate(zip(spatial_coord[:,0] * scale,
                spatial_coord[:,1] * scale)):
            ct = dict(zip(
                list(palettes.keys()),adata.obs.iloc[e].loc[list(palettes.keys())].to_numpy().flatten()))
            ax1.pie(
                ct.values(),
                radius=s * scale,
                colors=list(palettes.values()),
                center=(x,y)
            )
    elif layout == 'gradient':
        for i in valid_spots:
            alphas = adata.obs.loc[
                adata.obs['celltype_predict'] == i,
                'celltype_predict_proportions'
            ]
            alphas = (alphas - alphas.min()) / (alphas.max() - alphas.min()) * 0.5 + 0.5
            ax1.scatter(
                spatial_coord[
                    adata.obs['celltype_predict'] == i,
                    0
                ] * scale,
                spatial_coord[
                    adata.obs['celltype_predict'] == i,
                    1
                ] * scale,
                c=list(map(lambda x: tuple(list(palettes[i]) + [x]), alphas)),
                s=s * scale,
                lw=0
            )
    else:
        raise ValueError('layout must be either "piechart" or "gradient"')
    

    ax1.set_xbound(xlim[0],xlim[1])
    ax1.set_ybound(ylim[0],ylim[1])
    plt.grid(False)
    ax1.axis('off')

    if show_color_bar:
        sc.pl._tools.scatterplots._add_categorical_legend(
                ax1,
                pd.Categorical(valid_spots),
                palette,
                'right margin',
                'bold',
                None,
                None,
                False,
                'F7F7F7',
                False,
                False
            )
    if show:
        plt.show()
    return fig,ax1