# Pytorch
import torch
from torch import nn, optim
from torch.nn import functional as F
from torch.utils.data import DataLoader
from torch.utils.data.sampler import SubsetRandomSampler
from torch.distributions import kl_divergence as kld
from torch.optim.lr_scheduler import ReduceLROnPlateau
from torch.distributions import Normal

# Third party models
import scipy 
from typing import Optional, List, Iterable, Union, Mapping, Type, Dict, Callable, Tuple
from itertools import chain
from itertools import zip_longest
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MaxAbsScaler
import copy
from scipy.spatial import ConvexHull, Delaunay
import omegaconf
import gc
import cv2
import scanpy as sc
import einops
import numpy as np
import pandas as pd
import scipy
from tqdm import tqdm
from collections import Counter
import os 
from scipy.sparse import issparse
from copy import deepcopy
from functools import partial 


from scatlasvae.model._gex_model import scAtlasVAE as VAEMixin
from scatlasvae.model._primitives import Linear, FCLayer, SAE
from scatlasvae.utils._loss import LossFunction
from scatlasvae.utils._parallelizer import Parallelizer

from ._spatial_ldm import stAutoEncoderKL, stLatentDiffusion
from .. import basedir
from ..utils._compat import Literal
from ..utils._logger import mt, mw, get_tqdm, Colors
from ..utils._utilities import FLATTEN, dict_update_and_return
from ._spatial_gene_sets import GENE_SETS, get_spatial_gene_set
from ..preprocessing._preprocess import normalize_non_inplace
from ._model_utils import (
    print_gpu_mem,
    print_cpu_mem,
    one_hot,
    get_k_elements,
    get_last_k_elements,
    get_elements,
    EarlyStopping,
    get_default_device
)


from ..externals.segment_anything.modeling.image_encoder import ImageEncoderViT
from ..externals.segment_anything.modeling.mask_decoder import MaskDecoder, MLP
from ..externals.segment_anything.modeling.prompt_encoder import PromptEncoder, PositionEmbeddingRandom
from ..externals.segment_anything.modeling import TwoWayTransformer
from ..externals.segment_anything.modeling.common import LayerNorm2d
from ..externals.segment_anything import SamPredictor, sam_model_registry
from ..externals.segment_anything.utils.transforms import ResizeLongestSide
from ..externals.hipt4k.hipt_4k import HIPT_4K
from ..externals.ldm.modules.distributions.distributions import normal_kl, DiagonalGaussianDistribution
from ..externals.ldm.modules.encoders.modules import ClassEmbedder

from ._spatial_modeling_utils import (
    transform_spatial_image, 
    get_spatial_scalefactors_dict, 
    filter_spatial_outlier_spots,
    sample_with_fixed_sparsity,
    spatially_variable_genes,
    spatially_variable_genes_sinfonia,
    preprocess_image,
    get_spatial_condition
)

class stModelBase(VAEMixin):
    def __init__(self, *,
        sc_adata: Optional[sc.AnnData] = None,
        st_adatas: Optional[List[sc.AnnData]] = None,
        hidden_stacks: List[int] = [128],
        st_hidden_stacks: Optional[List[int]] = None,
        n_latent: int = 10,
        n_batch: int = 0,
        n_label: int = 0,
        n_additional_batch: Optional[Iterable[int]] = None,
        batch_key = None,
        label_key = 'cell_type',
        additional_batch_keys: Optional[Iterable[str]] = None,
        st_condition_key: Optional[str] = None,
        mmd_key: Optional[Literal['batch','additional_batch','both']] = None,
        gan_key: Optional[Literal['batch','additional_batch','both']] = None,
        new_adata_key: str = 'undefined',
        dispersion:  Literal["gene", "gene-batch", "gene-cell"] = "gene-cell",
        log_variational: bool = True,
        total_variational: bool = True,
        bias: bool = True,
        use_batch_norm: bool = True,
        use_layer_norm: bool = False,
        batch_hidden_dim: int = 8,
        batch_embedding: Literal["embedding", "onehot"] = "onehot",
        batch_variable_gene_mask: Optional[Union[np.ndarray, Mapping[str, np.ndarray]]] = None,
        filter_outlier_spots: bool = False,
        sc_reconstruction_method: Literal['mse', 'zg', 'zinb'] = 'zinb',
        st_reconstruction_method:  Literal['mse', 'nb', 'zinb'] = 'zinb',
        st_svgs_method: Literal['moranI','gearyC','moranI_gearyC'] = 'moranI',
        st_deconvolution_key: Literal['hidden','latent'] = 'latent',
        st_deconvolution_method: Literal['softmax','softplus'] = 'softplus',
        st_gamma_constrain_method: Literal['vamp', 'mmd'] = 'mmd',
        si_to_st_reconstruction_method: Literal['sum','mean'] = 'sum',
        si_autoencoder_config: Mapping = omegaconf.OmegaConf.load(
            str(basedir) + '/configs/st_diffusion_model/config.yaml'
        )['model']['params']['first_stage_config']['params'],
        si_diffusion_config: Mapping = omegaconf.OmegaConf.load(
            str(basedir) + '/configs/st_diffusion_model/config.yaml'
        )['model']['params']['latent_diffusion_config'],
        si_image_size: int = 1024,
        si_encoder_backend: Literal['sam','hipt'] = 'sam',
        si_to_st_method: Literal['softmax','softplus','sigmoid','deconvolution'] = 'sigmoid',
        si_to_st_loss: Literal['mse','bce'] = 'mse',
        sd_condition_stage_key: Optional[Union[Literal['leiden'], str, List[str]]] = None,
        constrain_n_label: bool = True,
        constrain_n_batch: bool = True,
        encode_libsize: bool = False,
        decode_libsize: bool = True,
        dropout_rate: float = 0.1,
        pre_encoder_dropout_rate: float = 0.1,
        v_bias_max: float = 0.2,
        activation_fn: nn.Module = nn.ReLU,
        inject_batch: bool = True,
        inject_additional_batch: bool = True,
        device: Optional[Union[str, torch.device]] = None,
        pretrained_state_dict: Optional[Mapping[str, torch.Tensor]] = None,
        initialize_st_image_dataset = True,
        parallel_dataset_initialization: bool = False,
        initialize_diffusion_model = False,
        initialize_vit_model = False,
    ) -> None:
        if device is None:
            device = get_default_device()

        if sc_adata is None:
            sc_adata_obs = pd.DataFrame()
            if batch_key is not None:
                sc_adata_obs[batch_key] = ['dummy' for _ in range(len(st_adatas))]
            if additional_batch_keys is not None:
                for additional_batch_key in additional_batch_keys:
                    sc_adata_obs[additional_batch_key] = ['dummy' for _ in range(len(st_adatas))]
            if label_key is not None:
                sc_adata_obs[label_key] = ['dummy' for _ in range(len(st_adatas))]
            sc_adata_var = list(st_adatas.values())[0].var
            
            sc_adata = sc.AnnData(
                X = np.zeros((len(st_adatas),list(st_adatas.values())[0].shape[1])),
                obs = sc_adata_obs,
                var = sc_adata_var
            )

        super(stModelBase, self).__init__(
            adata=sc_adata,
            hidden_stacks=hidden_stacks,
            n_latent=n_latent,
            n_batch=n_batch,
            n_label=n_label,
            n_additional_batch=n_additional_batch,
            batch_key=batch_key,
            label_key=label_key,
            additional_batch_keys=additional_batch_keys,
            dispersion=dispersion,
            log_variational=log_variational,
            bias=bias,
            use_batch_norm=use_batch_norm,
            use_layer_norm=use_layer_norm,
            batch_hidden_dim=batch_hidden_dim,
            batch_embedding=batch_embedding,
            reconstruction_method=sc_reconstruction_method,
            constrain_n_label=constrain_n_label,
            constrain_n_batch=constrain_n_batch,
            encode_libsize=encode_libsize,
            decode_libsize=decode_libsize,
            dropout_rate=dropout_rate,
            activation_fn=activation_fn,
            inject_batch=inject_batch,
            inject_additional_batch=inject_additional_batch,
            mmd_key=mmd_key,
            new_adata_key=new_adata_key,
            device=device,
            pretrained_state_dict=pretrained_state_dict
        )

        if self.n_label == 0:
            raise ValueError("n_label must be greater than 0")

        for k,v in st_adatas.items():
            normalize_non_inplace(v)
            v.layers['max_abs'] = MaxAbsScaler().fit_transform(v.layers['normalized'])

        if filter_outlier_spots:
            for k,v in st_adatas.items():
                st_adatas[k] = filter_spatial_outlier_spots(v, subset=True)

        self.st_adatas = st_adatas
        self.st_hidden_stacks = st_hidden_stacks
        self.st_condition_key = st_condition_key
        self.st_additional_batch_keys = [st_condition_key] if st_condition_key is not None else None
        self.sd_condition_stage_key = sd_condition_stage_key
        self.batch_variable_gene_mask = batch_variable_gene_mask
        self.total_variational = total_variational
        self.v_bias_max = v_bias_max
        self.st_deconvolution_method = st_deconvolution_method
        self.st_reconstruction_method = st_reconstruction_method
        self.st_gamma_constrain_method = st_gamma_constrain_method
        self.st_deconvolution_key = st_deconvolution_key
        self.si_to_st_reconstruction_method = si_to_st_reconstruction_method
        self.st_svgs_method = st_svgs_method
        self.gan_key = gan_key
        self.si_to_st_loss = si_to_st_loss
        self.si_to_st_method = si_to_st_method
        self.parallel_dataset_initialization = parallel_dataset_initialization
        self._debug = False

        #######################
        # Additional Modules  #
        #######################

        self.image_size = self.img_size = si_image_size
        
        si_to_st_function = lambda x,i: torch.sum(
                    einops.rearrange(
                        self.px_rna_scale_decoder(
                            self.decoder(
                                torch.cat([
                                    einops.rearrange(
                                        einops.repeat(
                                            torch.from_numpy(self.sc_vprior_q_mu).to(x.device),
                                            'l d -> b l d',
                                            b = x.shape[0] * x.shape[1]
                                        ), 
                                        'b l d -> (b l) d'
                                    ),
                                    torch.cat([
                                        torch.ones(
                                            (x.shape[0] * x.shape[1] * self.sc_vprior_q_mu.shape[0], 1), 
                                            device=x.device
                                        ) * j for j in i
                                    ], dim=1)
                                ], dim = 1),
                            )
                        ),
                        '(b e l) d -> b e l d', b = x.shape[0], e = x.shape[1]
                    ) * x.unsqueeze(3),
                    dim=-2
                ) if si_to_st_method == 'deconvolution' else None

        if initialize_vit_model:
            self.si_transformer = siTransformer(
                gene_dim=self.in_dim,
                prompt_embed_dim=self.n_hidden,
                decoder_num_heads=8,
                encoder_backend=si_encoder_backend,
                si_to_st_method=si_to_st_method,
                si_to_st_function=si_to_st_function,
                n_label=self.n_label,
                si_to_st_loss=si_to_st_loss,
                si_to_st_reconstruction_method=si_to_st_reconstruction_method,
                st_deconvolution_method=st_deconvolution_method,
                n_hidden=self.n_hidden,
                image_size=self.image_size,
                _debug=self._debug,
                _adata=self.adata,
                _st_adatas=self.st_adatas,
                device=device,
            )

            self.si_latent_to_prompt_embedding = nn.Linear(
                self.n_latent,
                self.n_hidden
            )

            self.__model_architecture__ = "vit"

        if initialize_diffusion_model:
            self.sd_diffusion = sitDiffusion(
                latent_dim = self.n_latent,
                px_rna_dim = self.n_hidden,
                gene_dim = self.in_dim,
                image_size = self.image_size,
                image_embedding_size = self.image_size // 32,
                si_to_st_method = 'deconvolution' if si_to_st_method == 'deconvolution' else 'none',
                si_to_st_n_labels = self.n_label,
                si_to_st_function=si_to_st_function,
                si_autoencoder_config = si_autoencoder_config,
                si_diffusion_config = si_diffusion_config,
                prompt_embed_dim = self.n_latent // 2,
                si_to_st_reconstruction_method = si_to_st_reconstruction_method,
                _debug = self._debug,
                _adata = self.adata,
                _st_adatas = self.st_adatas,
                device = device,
            )

            self.sd_diffusion_latent_to_prompt_embedding = nn.Linear(
                self.n_latent,
                self.n_latent // 2
            )

            self.__model_architecture__ = "diffusion"

        ###################
        # Discriminators  #
        ###################

        self.st_discriminator = None 
        self.st_additional_discriminator = None 

        #######################
        # Additional ENCODERS #
        #######################

        self.st_pre_encoder_dropout = nn.Dropout(p=pre_encoder_dropout_rate)

        self.st_encoder = SAE(
            self.in_dim if not self.encode_libsize else self.in_dim + 1,
            stacks = hidden_stacks if st_hidden_stacks is None else st_hidden_stacks,
            # n_cat_list = [self.n_batch] if self.n_batch > 0 else None,
            cat_dim = batch_hidden_dim,
            cat_embedding = batch_embedding,
            encode_only = True,
            **self.fcargs
        )
        self.st_encoder_z_mean_fc = Linear(
            self.st_encoder.out_dim,
            self.n_latent, # * self.n_label
            init = 'normal'
        )

        self.st_encoder_z_var_fc = Linear(
            self.st_encoder.out_dim,
            self.n_latent, # * self.n_label
            init = 'normal'
        )

        self.st_encoder_z_gamma = Linear(
            self.n_latent,
            self.n_latent * self.n_label,
            init = 'normal'
        )

        if st_deconvolution_key == 'latent':
            self.st_encoder_to_n_label_fc = nn.Sequential(
                Linear(
                    self.n_latent,
                    self.n_hidden // 2,
                    init = 'default'
                ),
                nn.ReLU(),
                nn.Dropout(p=0.2),
                Linear(
                    self.n_hidden // 2,
                    self.n_label,
                    init='default'
                )
            )
            self.st_encoder_to_bias_fc = nn.Sequential(
                Linear(
                    self.n_latent,
                    self.n_hidden // 2,
                    init = 'default'
                ),
                nn.ReLU(),
                nn.Dropout(p=0.2),
                Linear(
                    self.n_hidden // 2,
                    1,
                    init='default'
                ),
                nn.Sigmoid()
            )
        elif st_deconvolution_key == 'hidden':
            self.st_encoder_to_n_label_fc = nn.Sequential(
                Linear(
                    self.n_hidden,
                    self.n_hidden // 2,
                    init = 'default'
                ),
                nn.ReLU(),
                nn.Dropout(p=0.2),
                Linear(
                    self.n_hidden // 2,
                    self.n_label,
                    init='default'
                )
            )
            self.st_encoder_to_bias_fc = nn.Sequential(
                Linear(
                    self.n_hidden,
                    self.n_hidden // 2,
                    init = 'default'
                ),
                nn.ReLU(),
                nn.Dropout(p=0.2),
                Linear(
                    self.n_hidden // 2,
                    1,
                    init='default'
                ),
                nn.Sigmoid()
            )
        else:
            raise ValueError("st_deconvolution_key must be 'latent' or 'hidden'")



        self.st_px_rna_dropout_decoder = Linear(
            self.n_hidden,
            self.in_dim,
            init='final'
        )

        self.transform = ResizeLongestSide(self.image_size)

        self.initialize_st_dataset(initialize_st_image_dataset)

        if initialize_vit_model:
            pixel_mean = np.vstack(list(map(lambda x: einops.rearrange(x['image'],'a b c -> (a b) c'), self.st_image_map.values()))).mean(0)
            pixel_std = np.vstack(list(map(lambda x: einops.rearrange(x['image'],'a b c -> (a b) c'), self.st_image_map.values()))).std(0)

            self.si_transformer.set_pixel_mean_std(pixel_mean, pixel_std)

        if gan_key is not None: 
            if gan_key == 'both' or gan_key == 'batch':
                self.st_discriminator = nn.Linear(self.n_latent, self.n_batch_st)
            if gan_key == 'both' or gan_key == 'additional_batch':
                self.st_additional_discriminator = [None for _ in self.n_additional_batch_st]
                for e,i in enumerate(self.n_additional_batch_st):
                    self.st_additional_discriminator[e] = nn.Linear(self.n_latent, i)
                self.st_additional_discriminator =  nn.ModuleList(self.st_additional_discriminator)
        
        original_decoder_n_cat_list = self.decoder_n_cat_list

        if self.n_additional_batch_ is not None and self.inject_additional_batch:
            decoder_n_cat_list = [self.n_batch + self.n_batch_st] + list(map(lambda x: x[0] + x[1], zip(self.n_additional_batch_, self.n_additional_batch_st)))
        else:
            if self.n_batch > 0 and inject_batch:
                decoder_n_cat_list = [self.n_batch + self.n_batch_st]
            else:
                decoder_n_cat_list = None

        self.decoder_n_cat_list = decoder_n_cat_list

        original_weight = torch.tensor(self.decoder._fclayer[0].weight)
        original_bias = torch.tensor(self.decoder._fclayer[0].bias)

        if self.batch_embedding == 'embedding':
            original_embedding_weights = [self.decoder.cat_embedding[e].weight.detach() for e in range(len(self.decoder_n_cat_list))]

        self.decoder = FCLayer(
            in_dim = self.n_latent,
            out_dim = self.n_hidden,
            n_cat_list = self.decoder_n_cat_list,
            cat_dim = self.batch_hidden_dim,
            cat_embedding = self.batch_embedding,
            use_layer_norm=False,
            use_batch_norm=True,
            dropout_rate=0,
            device=self.device
        )

        if self.batch_embedding == 'embedding':
            for i in range(len(self.decoder_n_cat_list)):
                new_embedding = self.decoder.cat_embedding[i]
                new_embedding_weight = new_embedding.weight.detach()
                new_embedding_weight[:original_decoder_n_cat_list[i],:] = original_embedding_weights[i]
                new_embedding.weight = nn.Parameter(new_embedding_weight)
                new_embedding = new_embedding.to(self.device)
                self.decoder.cat_embedding[i] = new_embedding

            
        new_weight = torch.tensor(self.decoder._fclayer[0].weight)
        new_bias = torch.tensor(self.decoder._fclayer[0].bias)
        new_weight[:,:(self.n_latent + self.batch_hidden_dim)] = original_weight[
            :,:(self.n_latent + self.batch_hidden_dim)
        ]
        new_bias[:self.n_latent + self.batch_hidden_dim] = original_bias[
            :self.n_latent + self.batch_hidden_dim
        ]

        self.decoder._fclayer[0].weight = nn.Parameter(new_weight)
        self.decoder._fclayer[0].bias = nn.Parameter(new_bias)

        #######################
        # Additional DECODERS #
        #######################

        self.st_decoder = FCLayer(
            in_dim = self.n_latent,
            out_dim = self.n_hidden,
            n_cat_list = self.decoder_n_cat_list,
            cat_dim = batch_hidden_dim,
            cat_embedding = batch_embedding,
            use_layer_norm=False,
            use_batch_norm=True,
            dropout_rate=0,
            device=self.device
        )

        self.st_px_rna_scale_bias_decoder = nn.Sequential(
            nn.Linear(self.n_hidden, self.in_dim),
            nn.Softmax(dim=-1)
        )

        self.to(self.device)

        if self.device != 'cpu' and pretrained_state_dict is not None:
            self.initialize_gamma_decoder()

    def initialize_gamma_decoder(self,
        lr: float = 1e-3,
        weight_decay: float = 1e-6,
        eps: float = 1e-8,
        n_per_batch: int = 128,
    ):
        self.train()
        loss_record = [np.finfo(np.float64).max]
        steps = 0
        optimizer = optim.AdamW(
            self.st_encoder_z_gamma.parameters(),
            lr=lr,
            weight_decay=weight_decay,
        )
        while loss_record[-1] > 10:
            z_st = Normal(0, 1).rsample((n_per_batch, self.n_latent)).to(self.device)
            gamma_st = self.st_encoder_z_gamma(z_st)
            gamma_st = gamma_st.view(-1, self.n_label, self.n_latent)
            if self.st_gamma_constrain_method == 'vamp':
                loss = -Normal(torch.tensor(
                        self.sc_vprior_q_mu,
                        device=self.device
                    ), torch.sqrt(
                        torch.tensor(
                            self.sc_vprior_q_var,
                            device=self.device
                        ) + eps)
                    ).log_prob(gamma_st).mean(0).sum()
            elif self.st_gamma_constrain_method == 'mmd':
                loss = torch.tensor(0., device=self.device)
                vprior = self.vprior()
                for i in range(self.n_label):
                    loss += LossFunction.mmd_loss_trvae(
                        gamma_st[:,i], vprior[:,i]
                    ) 
            else:
                raise ValueError("st_gamma_constrain_method must be 'vamp' or 'mmd'")
                

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            loss_record.append(loss.item())
            steps += 1
            if steps > 5000:
                mw("gamma_decoder failed to converge after 5,000 steps. Please check your model weights and hyperparameters.")
                break 
            
        mt("gamma_decoder initialized in {} steps".format(steps))

    def vprior(self):
        return torch.tensor(
                    np.vstack(
                        np.array(list(map(lambda x: 
                            x[np.random.choice(range(x.shape[0]), size=128, replace=False)], 
                            self.sc_vprior_q_mu_list
                        ))).transpose(1,0,2)[None,:,:]
                    ), 
                    device=self.device
                )

    def initialize_st_dataset(self, initialize_st_image_dataset):

        if self.st_additional_batch_keys is not None:
            self.additional_batch_keys = list(self.additional_batch_keys) + list(self.st_additional_batch_keys)

        self.compute_prior_from_sc()

        sample_spot_numbers = list(map(lambda x: x.shape[0], self.st_adatas.values()))
        # normalize between 0.5 to 1, more spots less weight
        sample_spot_numbers = -(sample_spot_numbers - np.min(sample_spot_numbers)) / (np.max(sample_spot_numbers) - np.min(sample_spot_numbers)) * 0.5 + 1
        self.sample_spot_numbers_weight_dict = dict(zip(
            list(self.st_adatas.keys()),
            sample_spot_numbers 
        ))

        mt("Initializing ST dataset into memory")
        if self.batch_key is not None:
            n_batch_st_ = len(
                np.unique(
                    FLATTEN([
                        np.unique(adata.obs[self.batch_key])
                        for adata in self.st_adatas.values()
                    ])
                )
            )
            self.batch_category_st = pd.Categorical(
                FLATTEN([
                        adata.obs[self.batch_key]
                        for adata in self.st_adatas.values()
                ])
            )
            self.n_batch_st = n_batch_st_
            self.batch_category_st_summary = dict(Counter(self.batch_category_st))

        mt("    Finishing initializing batch category")
        self.n_additional_batch_st = []
        if self.additional_batch_keys is not None:
            self.additional_batch_category_st = []
            self.additional_batch_category_st_summary = []
            for additional_batch_key in self.additional_batch_keys:
                n_additional_batch_st_ = len(
                    np.unique(
                        FLATTEN([
                            np.unique(adata.obs[additional_batch_key])
                            for adata in self.st_adatas.values()
                        ])
                    )
                )
                self.n_additional_batch_st.append(n_additional_batch_st_)

                self.additional_batch_category_st.append(pd.Categorical(
                    FLATTEN([
                            adata.obs[additional_batch_key]
                            for adata in self.st_adatas.values()
                    ])
                ))
                self.additional_batch_category_st_summary.append(
                    dict(Counter(self.additional_batch_category_st[-1]))
                )
                for i in range(len(self.additional_batch_category_st_summary[-1])):
                    for k in self.additional_batch_category_st[-1].categories:
                        if k not in self.additional_batch_category_st_summary[-1].keys():
                            self.additional_batch_category_st_summary[-1][k] = 0


            self.additional_batch_category_st_summary_reverse = [
                dict(zip(
                    list(map(lambda x: 
                        x + self.n_additional_batch[i],
                        self.additional_batch_category_st[i].codes
                    )), 
                    self.additional_batch_category_st[i])) \
                    for i in range(1) 
            ] 
            # range 1 may be changed to len(self.additional_batch_keys) but 
            # it is not necessary for the current design

        mt("    Finishing initializing additional batch category")

        self.additional_batch_category_st_dict = [
            dict(zip(
                self.additional_batch_category_st[i], 
                self.additional_batch_category_st[i].codes
            )) for i in range(len(self.additional_batch_category_st))
        ]
        self.batch_category_st_dict = dict(zip(
            self.batch_category_st, 
            self.batch_category_st.codes
        ))
        
        self.additional_batch_to_batch_st_dict = [
            dict(zip(
                self.additional_batch_category_st[i], 
                self.batch_category_st
            )) for i in range(len(self.additional_batch_category_st))
        ]


        X_st = []
        X_st_normalized = []
        pbar = get_tqdm()(
            range(len(self.st_adatas)), 
            desc="Normalizing gene expression",
            bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}'
        )
        for adata in self.st_adatas.values():
            X_st.append(adata.X)
            if self.si_to_st_loss == 'bce' and self.si_to_st_method == 'sigmoid':
                X_st_normalized.append(adata.layers['max_abs'])
            else:
                X_st_normalized.append(adata.layers['normalized'])
            pbar.update(1)
        pbar.close()

        if any(list(map(lambda x: scipy.sparse.issparse(x), X_st))):
            if any(list(map(lambda x: not scipy.sparse.issparse(x), X_st))):
                mw("Mixing sparse and dense matrices. Converting all to sparse matrices")
            X_st = scipy.sparse.vstack(list(map(lambda x: scipy.sparse.csr_matrix(x), X_st)))
        else:
            X_st = np.concatenate(X_st, axis=0)

        if any(list(map(lambda x: scipy.sparse.issparse(x), X_st_normalized))):
            if any(list(map(lambda x: not scipy.sparse.issparse(x), X_st_normalized))):
                mw("Mixing sparse and dense matrices. Converting all to sparse matrices")
            X_st_normalized = scipy.sparse.vstack(list(map(lambda x: scipy.sparse.csr_matrix(x), X_st)))
        else:
            X_st_normalized = np.concatenate(X_st_normalized, axis=0)

        self.X_st = X_st
        self.X_st_normalized = X_st_normalized
        self._n_record_st = X_st.shape[0]

        self._indices_st = np.arange(self._n_record_st)

        if initialize_st_image_dataset:
            self._indices_st_batch_map = {}
            self.st_image_map = {}
            self.st_scalefactors_map = {}
            c = 0
            pbar = get_tqdm()(
                range(len(self.st_adatas)), 
                desc="Initializing spatial information",
                bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}'
            )
            for k, a in self.st_adatas.items():
                self._indices_st_batch_map[k] = np.arange(
                    c, c + a.shape[0]
                )
                image, image_coord, spatial_coord, original_shape, scale, pixel_mean = transform_spatial_image(
                    a, 
                    self.transform
                )

                st_cond = None
                if self.sd_condition_stage_key is not None and self.__model_architecture__ == 'diffusion':
                    if isinstance(self.sd_condition_stage_key, str):
                        st_cond = get_spatial_condition(
                            a, 
                            self.sd_condition_stage_key,
                            spatial_coord,
                            self.image_size
                        )
                    elif isinstance(self.sd_condition_stage_key, list):
                        st_cond = [get_spatial_condition(
                            a, 
                            self.sd_condition_stage_key[i],
                            spatial_coord,
                            self.image_size
                        ) for i in range(len(self.sd_condition_stage_key))]



                self.st_image_map[k] = {
                    'image': image,
                    'image_coord': image_coord,
                    'spatial_coord': spatial_coord,
                    'original_shape': original_shape,
                    'original_scale': scale,
                    'transform_scale': image.shape[0] / original_shape[0],
                    'pixel_mean': pixel_mean,
                    'cond': st_cond
                }
                self.st_scalefactors_map[k] = get_spatial_scalefactors_dict(a)
                c += a.shape[0]
                pbar.update(1)
            pbar.close()

        if self.sd_condition_stage_key is not None and self.__model_architecture__ == 'diffusion':

            _on_start_cond = list(self.st_image_map.values())[0]['cond']

            if _on_start_cond is not None and isinstance(_on_start_cond, str):
                self.cond_stage_model = ClassEmbedder(
                    self.sd_diffusion.second_stage_model.model.diffusion_model.context_dim,
                )

                all_conditions = pd.Categorical(list(map(lambda x: x['cond'], self.st_image_map.values())))
                for e,k in enumerate(self.st_image_map.keys()):
                    self.st_image_map[k]['cond'] = {"class": np.array([
                        all_conditions.codes[e]
                    ]
                )}

                self.cond_stage_function = lambda c: self.cond_stage_model({
                    "class": torch.from_numpy(c).to(self.device)
                })

            elif _on_start_cond is not None and isinstance(_on_start_cond, np.ndarray):
                self.cond_stage_model = ClassEmbedder(
                    self.sd_diffusion.second_stage_model.model.diffusion_model.context_dim // 2,
                )
                self._cond_stage_pe = PositionEmbeddingRandom(
                    self.sd_diffusion.second_stage_model.model.diffusion_model.context_dim // 2,
                )
                self.cond_stage_function = lambda c: torch.cat([
                        einops.rearrange(
                        self.cond_stage_model({"class": torch.from_numpy(c).to(self.device)}),
                        "w b h c -> b c w h"
                    ), 
                    self._cond_stage_pe(c.shape).unsqueeze(0).to(self.device)
                ])

            self.sd_diffusion.set_cond_stage_function(self.cond_stage_function)

        batch_categories_st = None
        additional_batch_categories_st = None
        
        if self.batch_key is not None:
            if any(map(lambda adata: self.batch_key not in adata.obs.columns, self.st_adatas.values())):
                raise ValueError("batch_key not found in all st_adatas")
            batch_categories_st = np.array(list(map(lambda x: 
                x + self.n_batch,
                self.batch_category_st.codes
            )))

        if self.additional_batch_keys is not None:
            for additional_batch_key in self.additional_batch_keys:
                if any(map(lambda adata: additional_batch_key not in adata.obs.columns, self.st_adatas.values())):
                    raise ValueError("additional_batch_key not found in all st_adatas")
            additional_batch_categories_st = [
                np.array(x.codes) + (self.n_additional_batch[e] if e < len(self.n_additional_batch) else 0) for e,x in enumerate(self.additional_batch_category_st)
            ]
        mt("    Finishing initializing spatial batch category")

        def _compute_svgs(data, queue = None):
            if queue is not None:
                queue.put(None)

            results = []
            for k,adata in data:
                st_loss_weight = np.ones(adata.var.shape[0])
                if self.st_svgs_method in ['moranI','gearyC']:
                    if 'dispersions_norm' not in adata.var.columns:
                        sc.pp.highly_variable_genes(
                            adata,
                            layer='normalized',
                            min_disp=0.15
                        )
                    if self.st_svgs_method == 'moranI':
                        spatially_variable_genes(adata, mode='moran')
                        moran_df = adata.uns['moranI'][
                                np.array(~adata.uns['moranI']['I'].isna()) &
                                np.array(list(map(lambda x: not (
                                    x.startswith("MT-") or
                                    x.startswith("RPS") or
                                    x.startswith("RPL") or
                                    x.startswith("HSP") or
                                    x.startswith("DNAJ")
                                ), adata.uns['moranI'].index)))
                            ].sort_values("I", ascending=False)

                        weight = MaxAbsScaler().fit_transform(moran_df.iloc[:,0].to_numpy().reshape(-1,1))
                    else: 
                        spatially_variable_genes(adata, mode='geary')
                        geary_df = adata.uns['gearyC'][
                            np.array(~adata.uns['gearyC']['C'].isna()) &
                            np.array(list(map(lambda x: not (
                                x.startswith("MT-") or
                                x.startswith("RPS") or
                                x.startswith("RPL") or
                                x.startswith("HSP") or
                                x.startswith("DNAJ")
                            ), adata.uns['gearyC'].index)))
                        ].sort_values("C", ascending=False)

                        weight = MaxAbsScaler().fit_transform(geary_df.iloc[:,0].to_numpy().reshape(-1,1))
                    if weight.min() < 0: weight -= weight.min()
                    weight = (weight * 20).flatten()
                    d = dict(zip(moran_df.index, weight))
                    st_loss_weight = np.ones(adata.var.shape[0])
                    for i,j in d.items():
                        st_loss_weight[list(adata.var.index).index(i)] = j

                elif self.st_svgs_method == 'moranI_gearyC':
                    spatially_variable_genes_sinfonia(adata)
                    sc.pp.highly_variable_genes(
                        adata,
                        layer='normalized',
                        inplace=False
                    )
                    moran_df = adata.var.loc[
                            np.array(~adata.var['moranI'].isna()) & 
                            np.array(list(map(lambda x: not (
                                x.startswith("MT-") or 
                                x.startswith("RPS") or 
                                x.startswith("RPL") or 
                                x.startswith("HSP") or
                                x.startswith("DNAJ")
                            ), adata.var['moranI'].index))),
                            ['moranI']
                        ].sort_values("moranI", ascending=False)
                    
                    geary_df = adata.var.loc[
                        np.array(~adata.var['gearyC'].isna()) &
                        np.array(list(map(lambda x: not (
                            x.startswith("MT-") or 
                            x.startswith("RPS") or 
                            x.startswith("RPL") or 
                            x.startswith("HSP") or
                            x.startswith("DNAJ")
                        ), adata.var['gearyC'].index))),
                        ['gearyC']
                    ].sort_values("gearyC", ascending=False)
                    

                    weight_moran = MaxAbsScaler().fit_transform(moran_df.iloc[:,0].to_numpy().reshape(-1,1))
                    if weight_moran.min() < 0: weight_moran -= weight_moran.min()
                    weight_moran = (weight_moran * 20).flatten()
                    d_moran = dict(zip(moran_df.index, weight_moran))
                    weight_geary = MaxAbsScaler().fit_transform(geary_df.iloc[:,0].to_numpy().reshape(-1,1))
                    if weight_geary.min() < 0: weight_geary -= weight_geary.min()
                    weight_geary = (weight_geary * 20).flatten()
                    d_geary = dict(zip(geary_df.index, weight_geary))
                    
                    for k in set(d_moran.keys()).union(set(d_geary.keys())):
                        st_loss_weight[list(adata.var.index).index(k)] = (d_moran.get(k, 0) + d_geary.get(k, 0)) / 2

                else:
                    raise ValueError("st_svgs_method must be 'moranI', 'gearyC', or 'moranI_gearyC'")

                st_loss_weight[np.array(adata.X.mean(0)).flatten() < 0.0125] = 0
                st_loss_weight[
                    (np.array(np.array(adata.X.mean(0)).flatten() > 3) |
                    np.array(np.array(adata.X.mean(0)).flatten() < 0.005)) & 
                    np.array(adata.var['dispersions_norm'] < -0.1)
                ] = 0.25
                st_loss_weight[[list(adata.var.index).index(x) for x in get_spatial_gene_set(adata, 'TLS')]] = GENE_SETS['TLS']['weight']
                results.append((k,st_loss_weight))
            return results
        self.st_loss_weight_dict = {}
        if not self.parallel_dataset_initialization:
            pbar = get_tqdm()(
                range(len(self.st_adatas)), 
                desc="Initializing spatially variable genes weights",
                bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}'
            )
            for k in self.st_image_map.keys():
                st_loss_weight = _compute_svgs([(k, self.st_adatas[k])])
                self.st_loss_weight_dict[k] = st_loss_weight[0][1]
                pbar.update(1)
            pbar.close()
        else:
            n_jobs = min(len(self.st_adatas), os.cpu_count())
            mt(f"    Initializing spatially variable genes weights using {n_jobs} cores")
            p = Parallelizer(n_jobs=n_jobs).parallelize(
                map_func=_compute_svgs,
                map_data=list(self.st_adatas.items()),
                reduce_func=FLATTEN
            )()
            for k,v in p:
                self.st_loss_weight_dict[k] = v
        
        mt("    Finishing initializing spatially variable gene weights")
        
        if self.batch_variable_gene_mask is not None:
            if isinstance(self.batch_variable_gene_mask, np.ndarray):
                G_mask = np.vstack([
                        einops.repeat(
                            np.array(x.X.sum(0) != 0).flatten(), 
                            'k -> n k', n = x.shape[0]
                        ) for x in self.st_adatas.values()
                ])
                G_mask = G_mask * self.batch_variable_gene_mask
                mw("warning: using batch_variable_gene_mask as a numpy array is deprecated. Please use a dictionary instead")

            elif isinstance(self.batch_variable_gene_mask, Mapping):
                if self.batch_key is not None and self.additional_batch_keys is None:
                    G_mask = np.vstack([
                        einops.repeat(
                            np.array(x.X.sum(0) != 0).flatten() * \
                            self.batch_variable_gene_mask[x.obs[self.batch_key].values[0]],
                            'k -> n k', n = x.shape[0]
                        ) for x in self.st_adatas.values()
                    ])

                elif self.batch_key is not None and self.additional_batch_keys is not None:
                    all_masks = []
                    for x in self.st_adatas.values():
                        mask_ = self.batch_variable_gene_mask[
                            self.additional_batch_keys[0]
                        ][
                            x.obs[self.additional_batch_keys[0]].values[0]
                        ]

                        for additional_batch_key in self.additional_batch_keys[1:]:
                            mask_ = mask_ * self.batch_variable_gene_mask[additional_batch_key][x.obs[additional_batch_key].values[0]]
                        all_masks.append(mask_)

                    G_mask = np.vstack([
                        einops.repeat(
                            np.array(x.X.sum(0) != 0).flatten() * \
                            self.batch_variable_gene_mask[self.batch_key][x.obs[self.batch_key].values[0]] * mask_,
                            'k -> n k', n = x.shape[0]
                        ) for x,mask_ in zip(self.st_adatas.values(), all_masks)
                    ])
        else: 
            G_mask = np.vstack([
                einops.repeat(
                    np.array(x.X.sum(0) != 0).flatten(), 
                    'k -> n k', n = x.shape[0]
                ) for x in self.st_adatas.values()
            ])
        
        self._G_mask = G_mask

        if batch_categories_st is not None and additional_batch_categories_st is not None:
            _dataset_st = list(zip(
                X_st, 
                X_st_normalized, 
                G_mask, 
                batch_categories_st, 
                *additional_batch_categories_st
            ))
        elif batch_categories_st is not None:
            _dataset_st = list(zip(X_st, X_st_normalized, G_mask, batch_categories_st))
        else:
            _dataset_st = list(zip(X_st, X_st_normalized, G_mask))

        _dataset_st_normalized = X_st_normalized

        _shuffle_indices_st = list(range(len(_dataset_st)))
        np.random.shuffle(_shuffle_indices_st)
        self._dataset_st = np.array([_dataset_st[i] for i in _shuffle_indices_st])
        mt("    Finishing initializing ST expression")
        self._dataset_st_normalized = _dataset_st_normalized[_shuffle_indices_st]
        mt("    Finishing initializing ST normalized expression")

        self._shuffle_indices_st = np.array(
            [x for x,_ in sorted(zip(range(len(_dataset_st)), _shuffle_indices_st),
            key=lambda x: x[1])]
        )

        self._shuffled_indices_reverse_st = np.array(_shuffle_indices_st)


    def as_merged_st_adata(self):
        _adata = sc.concat(list(map(lambda x: x[:,:0], self.st_adatas.values())))
        adata = sc.AnnData(
            X = self.X_st,
            obs = _adata.obs,
            var = _adata.var,
            uns = _adata.uns,
            layers={
                'normalized': self.X_st_normalized,
            }
        )
        return adata 
    
    def __repr__(self):
        super_repr = super(stModelBase, self).__repr__()
        return super_repr + "\n" + \
            f'{Colors.ORANGE}stModelBase{Colors.NC} object containing:\n' + \
            f'    {Colors.GREEN}n_spatial_adata{Colors.NC}: {len(self.st_adatas)}\n'

    def as_multi_dataloader(
        self,
        n_per_batch: int = 128,
        subset_indices_sc: Union[torch.tensor, np.ndarray] = None,
        subset_indices_st: Union[torch.tensor, np.ndarray] = None,
        train_test_split: bool = False,
        random_seed: bool = 42,
        validation_split: bool = .2,
        shuffle: bool = True,
        return_sc: bool = True,
        return_st: bool = True,
    ):
        indices_sc = self._indices if subset_indices_sc is None else subset_indices_sc
        indices_st = self._indices_st if subset_indices_st is None else subset_indices_st
        np.random.seed(random_seed)
        if shuffle:
            np.random.shuffle(indices_sc)
            np.random.shuffle(indices_st)
        if train_test_split:
            split_sc = int(np.floor(validation_split * self._n_record))
            split_st = int(np.floor(validation_split * self._n_record_st))
            if split_sc % n_per_batch == 1:
                n_per_batch += 1
            if split_st % n_per_batch == 1:
                n_per_batch += 1
            train_indices_sc, val_indices_sc = indices_sc[split_sc:], indices_sc[:split_sc]
            train_indices_st, val_indices_st = indices_st[split_st:], indices_st[:split_st]
            train_sampler_sc = SubsetRandomSampler(train_indices_sc)
            train_sampler_st = SubsetRandomSampler(train_indices_st)
            validation_sampler_sc = SubsetRandomSampler(val_indices_sc)
            validation_sampler_st = SubsetRandomSampler(val_indices_st)
            return {
                "sc": (
                    DataLoader(indices_sc, n_per_batch, sampler=train_sampler_sc),
                    DataLoader(indices_sc, n_per_batch, sampler=train_sampler_sc)
                ),
                "st": (
                    DataLoader(indices_st, n_per_batch, sampler=train_sampler_st),
                    DataLoader(indices_st, n_per_batch, sampler=train_sampler_st)
                )
            }

        if len(indices_sc) % n_per_batch == 1:
            n_per_batch += 1
        if len(indices_st) % n_per_batch == 1:
            n_per_batch += 1

        return {
            "sc": DataLoader(indices_sc, n_per_batch, shuffle=shuffle),
            "st": DataLoader(indices_st, n_per_batch, shuffle=shuffle)
        }

    def compute_prior_from_sc(self):
        mt("Computing VampPrior from sc data")
        self.adata.obs['index'] = list(range(self.adata.shape[0]))
        agg = self.adata.obs.groupby(self.label_key).agg({'index': list})
        m = dict(zip(agg.index, agg['index']))
        sc_q_mu, sc_q_var = self.get_sc_latent_embedding(latent_key=['q_mu','q_var'])

        sc_prior_q_mu_list = [None for _ in range(self.n_label)]
        sc_prior_q_var_list = [None for _ in range(self.n_label)]

        for k,indices in m.items():
            sc_prior_q_mu_list[list(self.label_category.categories).index(k)] = sc_q_mu[
                indices
            ]
            sc_prior_q_var_list[list(self.label_category.categories).index(k)] = sc_q_var[
                indices
            ]
        self.sc_vprior_q_mu = np.vstack(list(map(lambda x: x.mean(0), sc_prior_q_mu_list)))
        self.sc_vprior_q_var = np.vstack(list(map(lambda x: x.mean(0), sc_prior_q_var_list)))
        self.sc_vprior_q_mu_list = sc_prior_q_mu_list
        self.sc_vprior_q_var_list = sc_prior_q_var_list

    def _normalize_data(self, X, after=None, copy=True):
        X = X.clone() if copy else X
        X = X.to(torch.float32)  # Check if torch.float64 should be used
        counts = X.sum(axis=-1)
        counts_greater_than_zero = counts[counts > 0]
        after = torch.median(counts_greater_than_zero, dim=0).values if after is None else after
        counts = counts + (counts == 0)
        counts = counts / after
        X /= counts.unsqueeze(1)
        return X

    def encode_multi(self,
        X_sc: Optional[torch.Tensor] = None,
        X_st: Optional[torch.Tensor] = None,
        eps: float = 1e-4,
        encode_sc: bool = True,
        encode_st: bool = True,
    ) -> Dict[str, torch.Tensor]:
        sc_dict, st_dict = None, None
        if X_sc is not None and encode_sc:
            libsize_sc = torch.log(X_sc.sum(1))

            if self.log_variational:
                X_sc = torch.log(1+X_sc)
            q_sc = self.encoder.encode(torch.hstack([X_sc,libsize_sc.unsqueeze(1)])) if self.encode_libsize else self.encoder.encode(X_sc)
            q_mu_sc = self.z_mean_fc(q_sc)
            q_var_sc = torch.exp(self.z_var_fc(q_sc)) + eps
            z_sc = Normal(q_mu_sc, q_var_sc.sqrt()).rsample()
            sc_dict = dict(
                q = q_sc,
                q_mu = q_mu_sc,
                q_var = q_var_sc,
                z = z_sc
            )
        if X_st is not None and encode_st:
            libsize_st = torch.log(X_st.sum(1))
            if self.total_variational:
                X_st = self._normalize_data(X_st, after=1e4)
            if self.log_variational:
                X_st = torch.log(1+X_st)

            X_st = self.st_pre_encoder_dropout(X_st)

            q_st = self.st_encoder.encode(torch.hstack([X_st,libsize_st.unsqueeze(1)])) if self.encode_libsize else self.st_encoder.encode(X_st)
            q_mu_st = self.st_encoder_z_mean_fc(q_st)
            # q_mu_st = q_mu_st.view(-1, self.n_label, self.n_latent)
            # q_mu_st_reshape = einops.rearrange(q_mu_st, 'b l k -> (b l) k')
            q_var_st = torch.exp(self.st_encoder_z_var_fc(q_st)) + eps
            # q_var_st = q_var_st.view(-1, self.n_label, self.n_latent)
            # q_var_st_reshape = einops.rearrange(q_var_st, 'b l k -> (b l) k')
            # q_var_st_reshape = torch.exp(q_var_st_reshape) + eps
            z_st = Normal(q_mu_st, q_var_st.sqrt()).rsample()

            gamma_st = self.st_encoder_z_gamma(z_st)
            gamma_st = gamma_st.view(-1, self.n_label, self.n_latent)

            q_v_st = self.st_encoder_to_n_label_fc(
                q_mu_st if self.st_deconvolution_key == 'latent' else q_st
            )
            q_v_bias_st = self.st_encoder_to_bias_fc(
                q_mu_st if self.st_deconvolution_key == 'latent' else q_st
            )
            q_v_bias_st = torch.clamp(q_v_bias_st, 0, self.v_bias_max)

            if self.st_deconvolution_method == 'softmax':
                q_v_st = F.softmax(q_v_st)
            elif self.st_deconvolution_method == 'softplus':
                q_v_st = F.softplus(q_v_st)
                q_v_st = q_v_st / q_v_st.sum(axis=1).reshape(-1, 1)
            else:
                raise ValueError("st_deconvolution_method must be either 'softmax' or 'softplus'")

            q_v_st = q_v_st.view(-1, self.n_label)

            st_dict = dict(
                q = q_st,
                q_mu_st = q_mu_st,
                q_var_st = q_var_st,
                z = z_st,
                gamma_st = gamma_st,
                q_v_st = q_v_st,
                q_v_bias_st = q_v_bias_st
            )

        H = {
            "sc": sc_dict,
            "st": st_dict
        }
        return H

    def decode_multi(self,
        H: Dict[str, torch.Tensor],
        lib_size_sc: Optional[torch.Tensor] = None,
        lib_size_st: Optional[torch.Tensor] = None,
        batch_index_sc: Optional[torch.Tensor] = None,
        batch_index_st: Optional[torch.Tensor] = None,
        additional_batch_index_sc: Optional[torch.Tensor] = None,
        additional_batch_index_st: Optional[torch.Tensor] = None,
        eps: float = 1e-4,
        decode_sc: bool = True,
        decode_st: bool = True,
        add_bias: bool = False
    ):
        R_sc, R_st = None, None
        if H['sc'] is not None and decode_sc:
            R_sc = super(stModelBase, self).decode(
                H['sc'],
                lib_size=lib_size_sc,
                batch_index=batch_index_sc,
                additional_batch_index=additional_batch_index_sc,
                eps=eps
            )

        if H['st'] is not None and decode_st:
            z_st = H['st']['z']
            gamma_st = H['st']['gamma_st']

            # [batch, n_latent, n_label]
            if additional_batch_index_st is not None and self.inject_additional_batch:
                if self.st_condition_key is not None:
                    additional_batch_index_st = list(map(lambda x: 
                        x[1], # - self.n_additional_batch[x[0]], 
                        enumerate(additional_batch_index_st[:-1])
                    ))
                else:
                    additional_batch_index_st = list(map(lambda x: 
                        x[1], # - self.n_additional_batch[x[0]], 
                        enumerate(additional_batch_index_st)
                    ))
                d_st = torch.hstack([
                    torch.zeros(z_st.shape, device=self.device), 
                    batch_index_st,#
                    *additional_batch_index_st
                ])
                z_st = torch.hstack([
                    z_st, 
                    batch_index_st,#
                    *additional_batch_index_st
                ])
                gamma_st = torch.hstack([
                    einops.rearrange(gamma_st, 'b l k -> b k l'),
                    einops.repeat(batch_index_st,#
                                  'b d -> b d l', l = self.n_label),
                    *[einops.repeat(b, 'b d -> b d l', l = self.n_label) for b in additional_batch_index_st]
                ])

            elif batch_index_st is not None and self.inject_batch:
                d_st = torch.hstack([torch.zeros(z_st.shape, device=self.device), batch_index_st-self.n_batch])
                z_st = torch.hstack([z_st, batch_index_st-self.n_batch])
                gamma_st = torch.hstack([
                    einops.rearrange(gamma_st, 'b l k -> b k l'),
                    einops.repeat(batch_index_st,#
                                  'b d -> b d l', l = self.n_label)
                ])

            gamma_st = einops.rearrange(gamma_st, 'b k l -> (b l) k')

            px_st = self.decoder(gamma_st)

            px_st_rna_scale = self.px_rna_scale_decoder(px_st)

            q_v_st = H['st']['q_v_st']
            q_v_bias_st = H['st']['q_v_bias_st']

            px_st_rna_scale = einops.rearrange(
                px_st_rna_scale, 
                '(b l) d -> b l d', 
                b = z_st.shape[0]
            )

            px_st_rna_scale = torch.sum(
                px_st_rna_scale * q_v_st.unsqueeze(2),
                dim=1
            )

            px_st_rna_scale_bias = self.st_px_rna_scale_bias_decoder(
                self.st_decoder(d_st)
            )

            px_st_rna_scale_bias = px_st_rna_scale_bias * q_v_bias_st.unsqueeze(1)

            px_st_rna_scale_out = px_st_rna_scale

            if add_bias:
                px_st_rna_scale_out = px_st_rna_scale_out * (1-q_v_bias_st).unsqueeze(1) + px_st_rna_scale_bias

            if self.decode_libsize and not self.st_reconstruction_method == 'mse':
                px_st_rna_scale_out_final = px_st_rna_scale_out * lib_size_st.unsqueeze(1)
            elif self.st_reconstruction_method == 'mse':
                px_st_rna_scale_out_final = px_st_rna_scale_out * 1e4
                px_st_rna_scale_out_final = torch.log(px_st_rna_scale_out_final + 1)
            else:
                px_st_rna_scale_out_final = px_st_rna_scale_out

            px_st_rna_rate = self.px_rna_rate_decoder(px_st)

            px_st_rna_rate = einops.rearrange(px_st_rna_rate, '(b l) d -> b l d', b = z_st.shape[0])

            px_st_rna_rate = torch.sum(
                px_st_rna_rate * q_v_st.unsqueeze(2),
                dim=1
            )

            px_st_rna_dropout = self.st_px_rna_dropout_decoder(
                self.st_decoder(z_st)
            )
            px_st_rna_dropout = einops.rearrange(
                px_st_rna_dropout, 
                '(b l) d -> b l d', b = z_st.shape[0]
            )

            px_st_rna_dropout = torch.sum(
                px_st_rna_dropout * q_v_st.unsqueeze(2),
                dim=1
            )

            R_st = dict(
                px_st_rna_scale = px_st_rna_scale_out_final,
                px_st_rna_scale_orig = px_st_rna_scale_out,
                px_st_rna_rate = px_st_rna_rate,
                px_st_rna_dropout = px_st_rna_dropout,
            )

        return {
            "sc": R_sc,
            "st": R_st
        }

    def forward_multi(self,
        X_sc: Optional[torch.Tensor] = None,
        X_st: Optional[torch.Tensor] = None,
        lib_size_sc: Optional[torch.Tensor] = None,
        lib_size_st: Optional[torch.Tensor] = None,
        batch_index_sc: Optional[torch.Tensor] = None,
        label_index_sc: Optional[torch.Tensor] = None,
        batch_index_st: Optional[torch.Tensor] = None,
        additional_batch_index_sc: Optional[torch.Tensor] = None,
        additional_batch_index_st: Optional[torch.Tensor] = None,
        G_mask: Optional[torch.Tensor] = None,
        st_gene_loss_weight: Optional[torch.Tensor] = None,
        st_spot_loss_weight: Optional[torch.Tensor] = None,
        eps: float = 1e-4,
        reduction: str = "mean",
        forward_sc: bool = True,
        forward_st: bool = True,
        compute_mmd: bool = True,
        add_bias: bool = False
    ):
        H = self.encode_multi(
            X_sc=X_sc,
            X_st=X_st,
            eps=eps,
            encode_sc=forward_sc,
            encode_st=forward_st
        )
        R = self.decode_multi(
            H,
            lib_size_sc=lib_size_sc,
            lib_size_st=lib_size_st,
            batch_index_sc=batch_index_sc,
            batch_index_st=batch_index_st,
            additional_batch_index_sc=additional_batch_index_sc,
            additional_batch_index_st=additional_batch_index_st,
            eps=eps,
            decode_sc=forward_sc,
            decode_st=forward_st,
            add_bias=add_bias
        ) 

        gamma_st = H['st']['gamma_st']

        if self.st_gamma_constrain_method == 'vamp':
            neg_log_likelihood_prior = -Normal(
                torch.tensor(
                    self.sc_vprior_q_mu,
                    device=self.device
                ), torch.tensor(
                    self.sc_vprior_q_var,
                    device=self.device
                )
            ).log_prob(gamma_st).mean(0).sum()
        else: 
            vprior = self.vprior()
            neg_log_likelihood_prior = torch.tensor(0., device=self.device)
            for i in range(self.n_label):
                neg_log_likelihood_prior += LossFunction.mmd_loss_trvae(
                    gamma_st[:,i], vprior[:,i]
                )

        batch_variant_cell_type_loss = H['st']['q_v_bias_st'].sum()

        v = H['st']['q_v_st']

        v_sparsity_loss = -torch.sum(v * torch.log(v + 1e-4), dim=1).mean()

        gate_loss = R['st']['px_st_rna_dropout'].sum(dim=1).mean()

        kl_divergence_sc = torch.tensor(0.)
        if forward_sc:
            q_mu_sc = H['sc']['q_mu']
            q_var_sc = H['sc']['q_var']
            mean_sc = torch.zeros_like(q_mu_sc)
            scale_sc = torch.ones_like(q_var_sc)
            kl_divergence_sc = kld(
                Normal(q_mu_sc, q_var_sc.sqrt()),
                Normal(mean_sc, scale_sc)
            ).sum(dim = 1)

        q_mu_st = H['st']['q_mu_st']
        q_var_st = H['st']['q_var_st']
        mean_st = torch.zeros_like(q_mu_st)
        scale_st = torch.ones_like(q_var_st)

        kl_divergence_st = kld(
            Normal(q_mu_st, q_var_st.sqrt()),
            Normal(mean_st, scale_st)).sum(dim = 1)

        reconstruction_loss_sc = torch.tensor(0.)
        reconstruction_loss_st = torch.tensor(0.)

        if self.reconstruction_method == 'zinb':
            if X_sc is not None and forward_sc:
                reconstruction_loss_sc = LossFunction.zinb_reconstruction_loss(
                    X_sc,
                    mu = R['sc']['px_rna_scale'],
                    theta = R['sc']['px_rna_rate'].exp(),
                    gate_logits = R['sc']['px_rna_dropout'],
                    reduction = reduction
                )
        else:
            raise NotImplementedError()

        if self.st_reconstruction_method == 'nb':
            if X_st is not None:
                reconstruction_loss_st = LossFunction.nb_reconstruction_loss(
                    X_st,
                    mu = R['st']['px_st_rna_scale'],
                    theta = R['st']['px_st_rna_rate'].exp(),
                    reduction = 'none' if G_mask is not None else reduction
                )
                if st_gene_loss_weight is not None:
                    reconstruction_loss_st = reconstruction_loss_st * st_gene_loss_weight
                if st_spot_loss_weight is not None:
                    reconstruction_loss_st = reconstruction_loss_st * st_spot_loss_weight.unsqueeze(1)


                if G_mask is not None:
                    mask_sum = G_mask.sum(1)
                    mask_weight = G_mask.shape[1] / mask_sum
                    reconstruction_loss_st = reconstruction_loss_st * G_mask
                    if reduction == 'mean':
                        reconstruction_loss_st = reconstruction_loss_st.mean(dim = 1)
                    elif reduction == 'sum':
                        reconstruction_loss_st = reconstruction_loss_st.sum(dim = 1)
                
        elif self.st_reconstruction_method == 'zinb':
            if X_st is not None:
                reconstruction_loss_st = LossFunction.zinb_reconstruction_loss(
                    X_st,
                    mu = R['st']['px_st_rna_scale'],
                    theta = R['st']['px_st_rna_rate'].exp(),
                    gate_logits = R['st']['px_st_rna_dropout'],
                    reduction = 'none' if G_mask is not None else reduction
                )
                if st_gene_loss_weight is not None:
                    reconstruction_loss_st = reconstruction_loss_st * st_gene_loss_weight
                if st_spot_loss_weight is not None:
                    reconstruction_loss_st = reconstruction_loss_st * st_spot_loss_weight.unsqueeze(1)

                if G_mask is not None:
                    mask_sum = G_mask.sum(1)
                    mask_weight = G_mask.shape[1] / mask_sum
                    reconstruction_loss_st = reconstruction_loss_st * G_mask
                    if reduction == 'mean':
                        reconstruction_loss_st = reconstruction_loss_st.mean(dim = 1) * mask_weight
                    elif reduction == 'sum':
                        reconstruction_loss_st = reconstruction_loss_st.sum(dim = 1) * mask_weight
                        
        elif self.st_reconstruction_method == 'mse':
            if X_st is not None:
                reconstruction_loss_st = LossFunction.mse(
                    R['st']['px_st_rna_scale'],
                    X_st,
                    reduction = 'none' if G_mask is not None else reduction
                )
                if st_gene_loss_weight is not None:
                    reconstruction_loss_st = reconstruction_loss_st * st_gene_loss_weight
                if st_spot_loss_weight is not None:
                    reconstruction_loss_st = reconstruction_loss_st * st_spot_loss_weight.unsqueeze(1)


                if G_mask is not None:
                    mask_sum = G_mask.sum(1)
                    mask_weight = G_mask.shape[1] / mask_sum
                    reconstruction_loss_st = reconstruction_loss_st * G_mask
                    if reduction == 'mean':
                        reconstruction_loss_st = reconstruction_loss_st.mean(dim = 1) * mask_weight
                    elif reduction == 'sum':
                        reconstruction_loss_st = reconstruction_loss_st.sum(dim = 1) * mask_weight
        else:
            raise NotImplementedError()

        prediction_loss = torch.tensor(0.)
        if self.n_label > 0 and forward_sc:
            criterion = nn.CrossEntropyLoss(
                weight=self.label_category_weight
            )
            prediction = self.fc(H['sc']['z'])
            if self.new_adata_code and self.new_adata_code in label_index_sc:
                prediction_index = (label_index_sc != self.new_adata_code).squeeze()
                prediction_loss = criterion(prediction[prediction_index], one_hot(label_index_sc[prediction_index], self.n_label))
            else:
                prediction_loss = criterion(prediction, one_hot(label_index_sc, self.n_label))

        mmd_loss_st = torch.tensor(0., device=self.device)
        if self.mmd_key is not None and compute_mmd:
            if self.mmd_key == 'batch':
                mmd_loss_st = self.mmd_loss(
                    H['st']['q_mu_st'], 
                    batch_index_st.detach().cpu().numpy(),
                    dim=1
                )
            elif self.mmd_key == 'additional_batch':
                for i in range(len(self.additional_batch_keys)):
                    mmd_loss_st = mmd_loss_st + self.mmd_loss(
                        H['st']['q_mu_st'], 
                        additional_batch_index_st[i].detach().cpu().numpy(),
                        dim=1
                    )
            elif self.mmd_key == 'both':
                if self.st_condition_key is not None:
                    mmd_loss_st = self.hierarchical_mmd_loss_1(
                        H['st']['q_mu_st'], 
                        additional_batch_index_st[len(self.n_additional_batch)].detach().cpu().numpy(),
                        batch_index_st.detach().cpu().numpy(),
                        dim=1
                    ) * 3
                else:
                    mmd_loss_st = self.mmd_loss(
                        H['st']['q_mu_st'], 
                        batch_index_st.detach().cpu().numpy(),
                        dim=1
                    ) * 3
                for i in range(len(self.n_additional_batch)):
                    mmd_loss_st = mmd_loss_st + self.hierarchical_mmd_loss_2(
                        H['st']['q_mu_st'], 
                        batch_index_st.detach().cpu().numpy(),
                        additional_batch_index_st[i].detach().cpu().numpy(),
                        dim=1
                    )
            else: 
                raise ValueError()

        gan_loss_st = self.gan_loss(H, batch_index_st, additional_batch_index_st)
        L = {
            "reconstruction_loss_sc": reconstruction_loss_sc,
            "reconstruction_loss_st": reconstruction_loss_st,
            "kl_divergence_sc": kl_divergence_sc,
            "kl_divergence_st": kl_divergence_st,
            "prediction_loss": prediction_loss,
            "mmd_loss_st": mmd_loss_st,
            "gan_loss_st": gan_loss_st,
            'neg_log_likelihood_prior_loss': neg_log_likelihood_prior,
            'batch_variant_cell_type_loss': batch_variant_cell_type_loss,
            'v_sparsity_loss': v_sparsity_loss,
            'gate_loss': gate_loss
        }
        return H, R, L

    def gan_loss(self, H, batch_index_st, additional_batch_index_st, detach=False):
        gan_loss_st = torch.tensor(0., device=self.device)
        criterion = nn.CrossEntropyLoss()
        if self.gan_key is not None: 
            if self.gan_key == 'batch':
                gan_loss_st = gan_loss_st + criterion(
                    self.st_discriminator(
                        H['st']['q_mu_st'] if not detach else H['st']['q_mu_st'].detach()
                    ),
                    one_hot(batch_index_st  - self.n_batch, self.n_batch_st)
                )
            elif self.gan_key == 'both':
                gan_loss_st = gan_loss_st + criterion(
                    self.st_discriminator(
                        H['st']['q_mu_st'] if not detach else H['st']['q_mu_st'].detach()
                    ),
                    one_hot(batch_index_st - self.n_batch, self.n_batch_st)
                )
                for i in range(len(self.additional_batch_keys)):
                    gan_loss_st = gan_loss_st + criterion(
                        self.st_additional_discriminator[i](
                            H['st']['q_mu_st'] if not detach else H['st']['q_mu_st'].detach()
                        ),
                        one_hot(additional_batch_index_st[i] - self.n_additional_batch[i], self.n_additional_batch_st[i])
                    )
        return gan_loss_st

    def fit_sc(self,
        **kwargs
    ):
        return super(stModelBase, self).fit(**kwargs)

    def fit(self,
        max_epoch:int = 35,
        n_per_batch:int = 128,
        kl_weight: float = 1.,
        nllp_weight: float = 1.,
        mmd_weight: float = 1.,
        enforce_label_weight: float = 1.,
        enforce_sparsity_weight: float = 1.,
        enforce_non_zero_gate_weight: float = 1.,
        deconv_weight: float = 1.,
        reconstruction_loss_st_weight: float = 1.,
        reconstruction_loss_sc_weight: float = 1.,
        compute_batch_after: float = 0.,
        add_batch_bias_after: float = 0.5,
        optimizer_parameters: Iterable = None,
        optimize_sc_decoder: bool = False,
        validation_split: float = .2,
        lr: bool = 5e-5,
        lr_schedule: bool = True,
        lr_factor: float = 0.6,
        lr_patience: int = 30,
        lr_threshold: float = 0.0,
        lr_min: float = 1e-6,
        n_epochs_kl_warmup: Union[int, None] = 0,
        n_epochs_nllp_warmup: Union[int, None] = 0,
        kl_warmup_start: float = 0.2,
        nllp_warmup_start: float = 1,
        weight_decay: float = 1e-6,
        random_seed: int = 12,
        reconstruction_reduction: str = 'sum',
        train_sc: bool = True,
        use_early_stopping: bool = False,
        early_stopping_patience: int = 5,
        eps=1e-4
    ):
        if compute_batch_after < 1:
            compute_batch_after = int(max_epoch * compute_batch_after)
        if add_batch_bias_after < 1:
            add_batch_bias_after = int(max_epoch * add_batch_bias_after)

        self.checkpoints = {}

        if n_epochs_kl_warmup:
            n_epochs_kl_warmup = min(max_epoch, n_epochs_kl_warmup)
            kl_warmup_gradient = (kl_weight-kl_warmup_start) / n_epochs_kl_warmup
            kl_weight_max = kl_weight
            kl_weight = kl_warmup_start

        if n_epochs_nllp_warmup:
            n_epochs_nllp_warmup = min(max_epoch, n_epochs_nllp_warmup)
            nllp_warmup_gradient = (nllp_weight-kl_warmup_start) / n_epochs_nllp_warmup
            nllp_weight_max = nllp_weight
            nllp_weight = nllp_warmup_start


        if use_early_stopping:
            early_stopping = EarlyStopping(patience=early_stopping_patience, verbose=True)
        self.train()

        if optimizer_parameters is None:
            optimizer = optim.AdamW(
                chain(*[getattr(self, x).parameters() for x in np.unique(list(filter(lambda x: 
                    ('st' in x and 'discriminator' not in x) \
                        if not optimize_sc_decoder \
                        else (('st' in x or x.startswith("decoder.")) \
                    and 'discriminator' not in x),
                    map(lambda x: x.split(".")[0], 
                    self.state_dict().keys())
                )))]),
                lr, 
                weight_decay=weight_decay
            )
        else:
            optimizer = optim.AdamW(optimizer_parameters, lr, weight_decay=weight_decay)

        if self.gan_key is not None: 
            optimizer_d = optim.AdamW(
                chain(*[getattr(self, x).parameters() for x in np.unique(list(filter(lambda x: 
                    'discriminator' in x,
                    map(lambda x: x.split(".")[0], 
                    self.state_dict().keys())
                )))]),
                lr, 
                weight_decay=weight_decay
            )

        scheduler = ReduceLROnPlateau(
            optimizer,
            patience=lr_patience,
            factor=lr_factor,
            threshold=lr_threshold,
            min_lr=lr_min,
            threshold_mode="abs",
            verbose=True,
        ) if lr_schedule else None

        pbar = get_tqdm()(range(max_epoch), desc="Epoch", bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}')
        loss_record = {
            "epoch_reconstruction_loss_sc": 0,
            "epoch_kldiv_loss_sc": 0,
            "epoch_reconstruction_loss_st": 0,
            "epoch_kldiv_loss_st": 0,
        }

        epoch_total_loss_list = []
        epoch_reconstruction_loss_sc_list = []
        epoch_kldiv_loss_sc_list = []
        epoch_reconstruction_loss_st_list = []
        epoch_kldiv_loss_st_list = []
        epoch_nll_prior_loss_list = []
        epoch_mmd_loss_st_list = []
        epoch_gan_loss_st_list = []
        epoch_sampled_deconvolution_loss_list = []

        for epoch in range(1, max_epoch+1):

            if epoch == compute_batch_after:
                self.checkpoints['compute_batch_after'] = deepcopy(self.state_dict())
            if epoch == add_batch_bias_after:
                self.checkpoints['add_batch_bias_after'] = deepcopy(self.state_dict())
            if epoch % 10 == 0:
                self.checkpoints[f'epoch_{epoch}'] = deepcopy(self.state_dict())

            epoch_total_loss = 0
            epoch_reconstruction_loss_sc = 0
            epoch_kldiv_loss_sc = 0
            epoch_reconstruction_loss_st = 0
            epoch_kldiv_loss_st = 0
            epoch_nll_prior_loss = 0
            epoch_mmd_loss_st = 0
            epoch_gan_loss_st = 0
            self._trained = True
            pbar.desc = "Epoch {}".format(epoch)

            dataloaders = self.as_multi_dataloader(
                n_per_batch=n_per_batch,
                train_test_split = True,
                validation_split = validation_split,
                random_seed=random_seed,
            )

            X_train_st = dataloaders['st'][0]
            X_test_st = dataloaders['st'][1]
            X_train_sc = dataloaders['sc'][0]
            X_test_sc = dataloaders['sc'][1]

            if len(X_train_sc) < len(X_train_st):
                zipping = zip_longest(X_train_sc, X_train_st)
            else:
                zipping = zip(X_train_sc, X_train_st)

            for b, (X_sc, X_st) in enumerate(zipping):
                X_sc, X_st, X_st_normalized, lib_size_sc, lib_size_st, batch_index, batch_index_st, label_index, G_mask, additional_batch_index, additional_batch_index_st, st_gene_loss_weight, st_spot_loss_weight = self._prepare_batch(
                    X_sc,
                    X_st,
                    prepare_sc = train_sc
                )
                if X_sc is None or X_st is None:
                    continue

                if  X_sc.shape[0] == 1 or X_st.shape[0] == 1:
                    continue

                H, R, L = self.forward_multi(
                    X_sc,
                    X_st,
                    lib_size_sc,
                    lib_size_st,
                    batch_index_sc = batch_index,
                    batch_index_st = batch_index_st,
                    additional_batch_index_sc = additional_batch_index,
                    additional_batch_index_st = additional_batch_index_st,
                    label_index_sc = label_index,
                    st_gene_loss_weight = st_gene_loss_weight,
                    st_spot_loss_weight = st_spot_loss_weight,
                    reduction = reconstruction_reduction,
                    G_mask = G_mask,
                    forward_sc = train_sc,
                    compute_mmd = mmd_weight > 0 and epoch > int(compute_batch_after),
                    add_bias = epoch > int(add_batch_bias_after)
                )

                all_sampled_labels = []
                all_sampled_cell_number = list(map(round, torch.clip(
                    torch.distributions.Normal(10,2).sample_n(X_st.shape[0]),
                    2,
                    18
                ).numpy()))
                all_sampled_X = []
                valid_labels = list(set(label_index.detach().cpu().numpy().astype(int).flatten()))
                for e in range(X_st.shape[0]):
                    cell_number = all_sampled_cell_number[e]
                    sample_labels = np.random.choice(
                        valid_labels,
                        np.random.randint(2, 4),
                        replace = False
                    )
                    sampled_labels = sample_with_fixed_sparsity(
                        sample_labels,
                        cell_number,
                        np.random.choice([0.5,1,1.5], 1)[0],
                    )
                    z = np.zeros((self.n_label,))
                    sampled_X = []
                    for j in sampled_labels:
                        z[j] = 1
                        _x = X_sc[
                            (label_index == j).squeeze().detach().cpu().numpy()
                        ]
                        sampled_X.append(
                            _x[np.random.choice(np.arange(_x.shape[0]), 1)[0]]
                        )
                    all_sampled_X.append(torch.vstack(sampled_X).sum(0))
                    all_sampled_labels.append(z)

                all_sampled_labels = np.vstack(all_sampled_labels)
                all_sampled_labels = torch.tensor(all_sampled_labels, dtype=torch.float32, device=self.device)
                all_sampled_X = torch.vstack(all_sampled_X).to(self.device)
                scale_factors = X_st.sum(1) / all_sampled_X.sum(1)
                all_sampled_X = all_sampled_X * scale_factors.unsqueeze(1)
                torch.round(all_sampled_X * scale_factors.unsqueeze(1))
                all_sampled_labels = F.softmax(all_sampled_labels, dim=-1)

                H_sampled = self.encode_multi(
                    X_st = all_sampled_X,
                    encode_sc = False
                )
                sampled_deconvolution_loss = LossFunction.cosine_similarity(
                    H_sampled['st']['q_v_st'],
                    all_sampled_labels
                ).sum() + LossFunction.mmd_loss_trvae(
                    H_sampled['st']['z'],
                    H['st']['z']
                )

                reconstruction_loss_sc = L['reconstruction_loss_sc']
                reconstruction_loss_st = L['reconstruction_loss_st']
                reconstruction_loss_sc = torch.nan_to_num(reconstruction_loss_sc, nan=0.0, posinf=0.0, neginf=0.0)
                reconstruction_loss_st = torch.nan_to_num(reconstruction_loss_st, nan=0.0, posinf=0.0, neginf=0.0)
                kl_divergence_sc = L['kl_divergence_sc']
                kl_divergence_st = L['kl_divergence_st']
                nllp = L['neg_log_likelihood_prior_loss']
                mmd_loss_st = L['mmd_loss_st']
                batch_variant_cell_type_loss = L['batch_variant_cell_type_loss']
                v_sparsity_loss = L['v_sparsity_loss']
                gate_loss = L['gate_loss']
                gan_loss_st = L['gan_loss_st']

                avg_reconstruction_loss_sc = reconstruction_loss_sc.sum() / X_sc.shape[0]
                if reconstruction_reduction == 'sum':
                    avg_reconstruction_loss_st = reconstruction_loss_st.sum() / X_st.shape[0]
                elif reconstruction_reduction == 'mean':
                    avg_reconstruction_loss_st = reconstruction_loss_st.sum()
                avg_kldiv_loss_sc = kl_divergence_sc.sum() / X_sc.shape[0]
                avg_kldiv_loss_st = kl_divergence_st.sum() / X_st.shape[0]
                avg_mmd_loss_st = mmd_loss_st.mean()
                avg_batch_variant_cell_type_loss = batch_variant_cell_type_loss / X_st.shape[0]

                if optimize_sc_decoder:
                    loss = (
                        reconstruction_loss_sc_weight * avg_reconstruction_loss_sc + 
                        reconstruction_loss_st_weight * avg_reconstruction_loss_st + 
                        kl_weight * (avg_kldiv_loss_sc + avg_kldiv_loss_st) + 
                        nllp_weight * nllp + 
                        mmd_weight * avg_mmd_loss_st +
                        enforce_non_zero_gate_weight * gate_loss +
                        deconv_weight * sampled_deconvolution_loss
                    )
                else:
                    loss = (
                        reconstruction_loss_st_weight * avg_reconstruction_loss_st + 
                        kl_weight * avg_kldiv_loss_st + 
                        nllp_weight * nllp + 
                        mmd_weight * avg_mmd_loss_st +
                        enforce_non_zero_gate_weight * gate_loss +
                        deconv_weight * sampled_deconvolution_loss
                    )

                if epoch > int(max_epoch * add_batch_bias_after):
                    loss = loss + enforce_label_weight * avg_batch_variant_cell_type_loss

                loss = loss + enforce_sparsity_weight * v_sparsity_loss 

                epoch_total_loss += loss.item()

                if self.gan_key is None or epoch < int(compute_batch_after):
                    optimizer.zero_grad()
                    if not torch.isnan(loss):
                        loss.backward()
                    else:
                        pbar.set_postfix({
                            "message": "NaN detected. Skipping batch."
                        })
                    optimizer.step()
                else:                     
                    loss = loss - gan_loss_st * 100

                    if not torch.isnan(loss):    

                        optimizer.zero_grad()
                        if not torch.isnan(loss):
                            loss.backward(retain_graph=True)
                            optimizer.step()
                        else:
                            pbar.set_postfix({
                                "message": "NaN detected. Skipping batch."
                            })

                        optimizer_d.zero_grad()
                        gan_loss = self.gan_loss(
                            H, 
                            batch_index_st, 
                            additional_batch_index_st,
                            detach=True
                        )
                        gan_loss.backward(retain_graph=True)
                        optimizer_d.step()

                    else:
                        pbar.set_postfix({
                            "message": "NaN detected. Skipping batch."
                        })

                epoch_reconstruction_loss_sc += avg_reconstruction_loss_sc.item()
                epoch_kldiv_loss_sc += avg_kldiv_loss_sc.item()
                epoch_reconstruction_loss_st += avg_reconstruction_loss_st.item()
                epoch_kldiv_loss_st += avg_kldiv_loss_st.item()
                epoch_nll_prior_loss += nllp.item()
                epoch_mmd_loss_st += avg_mmd_loss_st.item()
                epoch_gan_loss_st += gan_loss_st.item()

                pbar.set_postfix({
                    'rc_st': '{:.2e}'.format(epoch_reconstruction_loss_st / (b+1)),
                    'nllp': '{:.2e}'.format(epoch_nll_prior_loss / (b+1)),
                    'step': f'{b} / {max(len(X_train_sc),len(X_train_st))}'
                })

            if lr_schedule:
                scheduler.step(epoch_reconstruction_loss_st)
            if use_early_stopping:
                early_stopping(epoch_reconstruction_loss_st, self)
                if early_stopping.early_stop:
                    mt("Early stopped")
                    pbar.close()
                    break 

            epoch_total_loss_list.append(epoch_total_loss)
            epoch_reconstruction_loss_sc_list.append(epoch_reconstruction_loss_sc)
            epoch_kldiv_loss_sc_list.append(epoch_kldiv_loss_sc)
            epoch_reconstruction_loss_st_list.append(epoch_reconstruction_loss_st)
            epoch_kldiv_loss_st_list.append(epoch_kldiv_loss_st)
            epoch_nll_prior_loss_list.append(epoch_nll_prior_loss)
            epoch_mmd_loss_st_list.append(epoch_mmd_loss_st)
            epoch_gan_loss_st_list.append(epoch_gan_loss_st)
            epoch_sampled_deconvolution_loss_list.append(sampled_deconvolution_loss.item())

            pbar.update(1)
            if n_epochs_kl_warmup:
                kl_weight = min( kl_weight + kl_warmup_gradient, kl_weight_max)
            if n_epochs_nllp_warmup:
                nllp_weight = min( nllp_weight + nllp_warmup_gradient, nllp_weight_max)

            random_seed += 1
        pbar.close()
        self.checkpoints['trained_state_dict'] = deepcopy(self.state_dict())

        return dict(
            epoch_total_loss_list=epoch_total_loss_list,
            epoch_reconstruction_loss_sc_list=epoch_reconstruction_loss_sc_list,
            epoch_kldiv_loss_sc_list=epoch_kldiv_loss_sc_list,
            epoch_reconstruction_loss_st_list=epoch_reconstruction_loss_st_list,
            epoch_kldiv_loss_st_list=epoch_kldiv_loss_st_list,
            epoch_nll_prior_loss_list=epoch_nll_prior_loss_list,
            epoch_mmd_loss_st_list=epoch_mmd_loss_st_list,
            epoch_gan_loss_st_list=epoch_gan_loss_st_list,
            epoch_sampled_deconvolution_loss_list=epoch_sampled_deconvolution_loss_list
        )

    def fit_si(
        self,
        max_epoch:int = 35,
        lr: float = 5e-5,
    ):
        self.train()
        optimizer = torch.optim.Adam(chain(
            # self.si_transformer.image_encoder.parameters(), 
            self.si_transformer.image_encoder_transition.parameters(),
            self.si_transformer.output_upscaling.parameters(),
            self.si_transformer.image_decoder.parameters()
        ), lr=lr)
        pbar = get_tqdm()(
            range(max_epoch),
            bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}'
        )
        pbar_postfix = {
            "msg": "",
            "loss_si": 0.,
            'step': f'0 / {len(self.st_adatas)}',
            'vram': print_gpu_mem(int(self.device.split(":")[-1]))[0],
            'ram': print_cpu_mem()[0]
        }
        total_loss_list = []
        for _ in range(max_epoch):
            
            epoch_si_loss = 0
            for e, k in enumerate(self.st_image_map.keys()):
                spatial_coord = torch.tensor(self.st_image_map[k]['spatial_coord']).to(self.device)

                l = np.array(sorted(spatial_coord[
                    spatial_coord[:,1] == Counter(spatial_coord[:,1]).most_common()[0], 0
                ]))
                l = np.mean(l[1:] - l[:-1]) / 2 # the radius between spot

                input_image_torch = torch.as_tensor(
                    self.st_image_map[k]['image'],
                    device=self.device
                )
                transformed_image = input_image_torch.permute(2, 0, 1).contiguous()[None, :, :, :]
                pixel_average = torch.tensor(self.st_image_map[k]['pixel_mean'], device=transformed_image.device)
                preprocessed_image = preprocess_image(
                    transformed_image,
                    self.img_size,
                    int(self.si_transformer.encoder_backend != 'sam'),
                    self.si_transformer.pixel_mean,
                    self.si_transformer.pixel_std,
                    pixel_average
                )

                if self.si_transformer.encoder_backend == 'sam':
                    image_embedding = self.si_transformer.image_encoder(preprocessed_image)
                    image_embedding = einops.rearrange(
                        image_embedding,
                        'n e a b -> n a b e'
                    )
                    image_embedding = self.si_transformer.image_encoder_transition(image_embedding)
                    image_embedding = einops.rearrange(
                        image_embedding,
                        'n w h e -> n e w h'
                    )
                else:
                    image_embedding = self.si_transformer.image_encoder.forward_all256(preprocessed_image)
                    image_embedding = einops.rearrange(
                        image_embedding[1],
                        'n e a b c d -> n (a c) (b d) e'
                    )
                    image_embedding = self.si_transformer.image_encoder_transition(image_embedding)
                    image_embedding = einops.rearrange(
                        image_embedding,
                        'n w h e -> n e w h'
                    )

                # Expand per-image data in batch direction to be per-mask
                src = torch.repeat_interleave(image_embedding, 1, dim=0)
                upscaled_embedding_pre = self.si_transformer.output_upscaling(src)

                upscaled_image_reconstruction = self.si_transformer.image_decoder(
                    einops.rearrange(upscaled_embedding_pre, 'a b c d -> a c d b')
                )

                # Start computing the image/ST mask
                coordinates = np.indices((
                    self.img_size, 
                    self.img_size
                )).transpose(1, 2, 0)
                coordinates_flat = einops.rearrange(coordinates, 'a b c -> (b a) c')

                neighbors = NearestNeighbors(n_neighbors=1)
                neighbors.fit(spatial_coord.detach().cpu().numpy())

                D, I = neighbors.kneighbors(coordinates_flat)

                mask_d = (D.min(1) < 10 * (self.img_size // 512)).reshape((
                    self.img_size, 
                    self.img_size
                )).astype(np.uint8)

                mask = np.zeros(mask_d.shape, dtype=np.bool)
                mask_final = np.zeros(mask_d.shape)

                hull = Delaunay(spatial_coord.detach().cpu().numpy())
                mask[(hull.find_simplex(coordinates) == -1).reshape((
                    self.img_size, 
                    self.img_size
                ))] = True

                contours, _ = cv2.findContours(mask_d, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                cv2.drawContours(mask_final, contours, -1, (255,255,255), cv2.FILLED)
                mask = ~np.bitwise_and(~mask.astype(np.bool).T, mask_final.astype(np.bool)) 

                original_mask = mask.copy()
                # Finish computing the image/ST mask

                loss_si = (
                    ( 255 * upscaled_image_reconstruction ) - 
                    ( 255 * einops.rearrange(
                        F.interpolate(
                            preprocessed_image,
                            (
                                self.img_size // 2,
                                self.img_size // 2,
                            ),
                            mode="bilinear",
                            align_corners=False,
                        ), 'b c w h -> b w h c'))
                ) ** 2
                mask_torch = F.interpolate(
                    torch.from_numpy(~original_mask).to(upscaled_image_reconstruction.device)
                    .unsqueeze(0).unsqueeze(0).float(),
                    (
                        self.img_size // 2,
                        self.img_size // 2,
                    ),
                    mode="bilinear",
                    align_corners=False,
                ).squeeze().bool()

                loss_si = (loss_si * mask_torch.unsqueeze(-1).float()).sum() / (mask_torch).sum()
                epoch_si_loss += loss_si.item()

                optimizer.zero_grad()
                loss_si.backward()
                optimizer.step()
                
                pbar_postfix['step'] = f'{e} / {len(self.st_image_map)}'
                pbar_postfix['vram'] = print_gpu_mem(int(self.device.split(":")[-1]))[0]
                pbar_postfix['ram'] = print_cpu_mem()[0]
                pbar.set_postfix(pbar_postfix)

                if self.si_transformer.encoder_backend == 'sam':
                    reconst_img = upscaled_image_reconstruction[0] *  self.si_transformer.pixel_std[0,:,0,0] + self.si_transformer.pixel_mean[0,:,0,0]
                    reconst_img = torch.clamp(reconst_img.detach().cpu() / 255,0.,1.)
                elif self.si_transformer.encoder_backend == 'hipt':
                    reconst_img = torch.clamp(upscaled_image_reconstruction[0].detach().cpu(),0.,1.)

                if self._debug:
                    import matplotlib.pyplot as plt
                    fig,ax=plt.subplots()
                    plt.imshow(reconst_img)
                    if self.si_transformer.encoder_backend == 'sam':
                        fig.savefig(f'{self._debug_output_path}/sam_{k}_tmp1.png', dpi=100)
                    else: 
                        fig.savefig(f'{self._debug_output_path}/hipt_{k}_tmp1.png', dpi=100)
                    plt.close(fig)

                pbar.update(1)
                
            pbar_postfix["loss_si"] = epoch_si_loss
            pbar_postfix['msg'] = "Finished epoch"
            pbar.set_postfix(pbar_postfix)
            total_loss_list.append(epoch_si_loss)

        pbar.close()
        return total_loss_list

    def fit_si_transformer(self, 
        max_epoch: int = 35,
        lr: float = 5e-5, 
        weight_decay: float = 1e-3,
        n_neighbor = 1,
        st_weight: float = 1.,
        si_weight: float = 1.,
        optimizer_parameters: Iterable = None,
    ):
        self.train()
        if optimizer_parameters is None:
            if self.si_transformer.encoder_backend == 'sam':
                optimizer = optim.AdamW(
                    chain(
                        *[
                            getattr(self, x).parameters()
                            for x in np.unique(
                                list(
                                    filter(
                                        lambda x: (
                                            ("si_" in x or "st_encoder" in x)
                                            and ("si_transformer" not in x)
                                        ),
                                        map(
                                            lambda x: x.split(".")[0],
                                            self.state_dict().keys(),
                                        ),
                                    )
                                )
                            )
                        ]
                        + [
                            getattr(self.si_transformer, x).parameters()
                            for x in np.unique(
                                list(
                                    filter(
                                        lambda x: (
                                            "image_encoder" not in x
                                            and "image_encoder_transition" not in x
                                            and "output_upscaling" not in x
                                        ),
                                        map(
                                            lambda x: x.split(".")[0],
                                            self.si_transformer.state_dict().keys(),
                                        ),
                                    )
                                )
                            )
                        ]
                    ),
                    weight_decay=weight_decay,
                )
            else:
                optimizer = optim.AdamW(
                    chain(*[getattr(self, x).parameters() for x in np.unique(list(filter(lambda x: 
                        (('si_' in x or 'st_encoder' in x) and ('si_transformer' not in x)),
                        map(lambda x: x.split(".")[0], 
                        self.state_dict().keys())
                    )))] + [getattr(self.si_transformer, x).parameters() for x in np.unique(list(filter(lambda x: 
                        ('image_encoder' not in x),
                        map(lambda x: x.split(".")[0], 
                        self.si_transformer.state_dict().keys())
                    )))]),
                    weight_decay=weight_decay
                )
        else:
            optimizer = optim.AdamW(optimizer_parameters, lr, weight_decay=weight_decay)

        loss_record = []
        pbar = get_tqdm()(
            range(max_epoch),
            bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}'
        )
        pbar_postfix = {
            "msg": "",
            "loss_st": 0.,
            "loss_si": 0.,
            'step': f'0 / {len(self.st_adatas)}',
            'vram': print_gpu_mem(int(self.device.split(":")[-1]))[0],
            'ram': print_cpu_mem()[0]
        }
        for epoch in range(max_epoch):
            epoch_total_loss = 0.
            epoch_st_loss = 0.
            epoch_si_loss = 0.
    
            for e,k in enumerate(self.st_image_map):
                st_loss_weight = torch.from_numpy(self.st_loss_weight_dict[k]).to(self.device)
                spatial_coord = torch.tensor(self.st_image_map[k]['spatial_coord']).to(self.device)

                l = np.array(sorted(spatial_coord[
                    spatial_coord[:,1] == Counter(spatial_coord[:,1]).most_common()[0], 0
                ]))
                l = np.mean(l[1:] - l[:-1]) / 2 # the radius between spot
                subset_indices = self._shuffle_indices_st[self._indices_st_batch_map[k]]
                X = torch.from_numpy(
                    scipy.sparse.vstack(list(map(lambda x: x[0], 
                    self._dataset_st[subset_indices]))).toarray()
                ).to(self.device)

                X_normalized = torch.from_numpy(
                    self._dataset_st_normalized[self._shuffle_indices_st[self._indices_st_batch_map[k]]]
                )

                if (self.si_transformer.si_to_st_loss == "bce" and \
                    self.si_transformer.si_to_st_method != 'sigmoid'):
                    X_normalized = F.softmax(X_normalized, dim=1)

                # TODO: replace hard-coding
                latent_embedding = self.st_encoder_z_mean_fc(
                    self.st_encoder.encode(torch.log(1+X))
                )
                latent_embedding = self.si_latent_to_prompt_embedding(latent_embedding)

                input_image_torch = torch.as_tensor(
                    self.st_image_map[k]['image'],
                    device=self.device
                )
                transformed_image = input_image_torch.permute(2, 0, 1).contiguous()[None, :, :, :]
                pixel_average = torch.tensor(self.st_image_map[k]['pixel_mean'], device=transformed_image.device)
                preprocessed_image = preprocess_image(
                    transformed_image,
                    self.img_size,
                    int(self.si_transformer.encoder_backend != 'sam'),
                    self.si_transformer.pixel_mean,
                    self.si_transformer.pixel_std,
                    pixel_average
                )
                pbar_postfix['msg'] = f"Sample {k} finished preprocessing"
                pbar.set_postfix(pbar_postfix)

                output = self.si_transformer(
                    preprocessed_image,
                    spatial_coord,
                    latent_embedding,
                    X_normalized,
                    st_loss_weight = st_loss_weight,
                    n_neighbor = n_neighbor,
                    upscaled_diameter = self.st_scalefactors_map[k]['spot_diameter_fullres'] * \
                        self.st_image_map[k]['original_scale'] * \
                        self.st_image_map[k]['transform_scale'],
                    k = k,
                    batch_indices = [self.batch_category_st_dict[
                        self.additional_batch_to_batch_st_dict[0][k]
                    ], self.additional_batch_category_st_dict[0][k]],
                    progress_callback = lambda x: pbar.set_postfix(
                        dict_update_and_return(pbar_postfix, x)
                    )
                )

                loss_st = output['loss_st']
                loss_si = output['loss_si']
                loss = loss_st * st_weight + loss_si * si_weight
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

                pbar_postfix['msg'] = f"Sample {k} finished optimization"
                pbar_postfix["step"] = f'{e} / {len(self.st_adatas)}'
                pbar_postfix['vram'] = print_gpu_mem(int(self.device.split(":")[-1]))[0]
                pbar_postfix['ram'] = print_cpu_mem()[0]
                pbar.set_postfix(pbar_postfix)

                torch.cuda.empty_cache()
                gc.collect()

                epoch_total_loss += loss.item()
                epoch_st_loss += loss_st.item()
                epoch_si_loss += loss_si.item()
            pbar_postfix["loss_st"] = epoch_st_loss
            pbar_postfix["loss_si"] = epoch_si_loss
            pbar_postfix['msg'] = "Finished epoch"
            pbar.set_postfix(pbar_postfix)
            pbar.update(1)
            loss_record.append(epoch_total_loss)
        pbar.close()
        return loss_record

    def fit_sd_diffusion_first_stage_model(
        self,
        max_epoch: int = 35,
        lr: float = 5e-5, 
        n_neighbor = 1,
        st_weight: float = 1.,
        si_weight: float = 1.,
        st_loss_weight: torch.Tensor = None,
        optimize_st_encoder: bool = False
    ):
        self.train()

        optimizer = optim.AdamW(
            chain(
                self.st_encoder.parameters() if optimize_st_encoder else [],
                self.sd_diffusion_latent_to_prompt_embedding.parameters(),
                self.sd_diffusion.twowaytransformer.parameters(),
                self.sd_diffusion.first_stage_model.encoder.parameters(),
                self.sd_diffusion.first_stage_model.decoder.parameters(),
                self.sd_diffusion.first_stage_model.quant_conv.parameters(),
                self.sd_diffusion.first_stage_model.post_quant_conv.parameters(),
                self.sd_diffusion.first_stage_model.gene_decoder.parameters()
            ),
            lr = lr,
            betas = (0.5,0.9)
        )
        optimizer_d = optim.AdamW(
            self.sd_diffusion.first_stage_model.loss.discriminator.parameters(),
            lr = lr,
            betas = (0.5,0.9)
        )

        loss_record = {
            "epoch_total_loss": [],
            "epoch_st_loss": [],
            "epoch_si_loss": [],
        }
        pbar = get_tqdm()(
            range(max_epoch),
            bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}'
        )

        pbar_postfix = {
            "msg": "",
            "loss_st": 0.,
            "loss_si": 0.,
            'step': f'0 / {len(self.st_adatas)}',
            'vram': print_gpu_mem(int(self.device.split(":")[-1]))[0],
            'ram': print_cpu_mem()[0]
        }

        step = 0
        for epoch in range(max_epoch):
            epoch_total_loss = 0.
            epoch_st_loss = 0.
            epoch_si_loss = 0.
            for e, k in enumerate(self.st_image_map.keys()):

                st_loss_weight = self.st_loss_weight_dict[k]
                st_loss_weight = torch.from_numpy(self.st_loss_weight_dict[k]).to(self.device)
                
                spatial_coord = torch.tensor(self.st_image_map[k]['spatial_coord']).to(self.device)

                l = np.array(sorted(spatial_coord[
                    spatial_coord[:,1] == Counter(spatial_coord[:,1]).most_common()[0], 0
                ]))
                l = np.mean(l[1:] - l[:-1]) / 2 # the radius between spot
                subset_indices = self._shuffle_indices_st[self._indices_st_batch_map[k]]
                X = torch.from_numpy(
                    scipy.sparse.vstack(list(map(lambda x: x[0], 
                    self._dataset_st[subset_indices]))).toarray()
                ).to(self.device)

                X_normalized = torch.from_numpy(
                    self._dataset_st_normalized[
                        self._shuffle_indices_st[
                            self._indices_st_batch_map[k]
                        ]
                    ]
                )

                if (self.si_to_st_loss == "bce" and \
                    self.si_to_st_method != 'sigmoid'):
                    # X_normalized = self._normalize_data(X_normalized, after=1)
                    X_normalized = F.softmax(X_normalized, dim=1)

                # TODO: replace hard-coding
                latent_embedding_orig = self.st_encoder_z_mean_fc(
                    self.st_encoder.encode(torch.log(1+X))
                )
                latent_embedding = self.sd_diffusion_latent_to_prompt_embedding(latent_embedding_orig)

                input_image_torch = torch.as_tensor(
                    self.st_image_map[k]['image'],
                    device=self.device
                )
                transformed_image = input_image_torch.permute(2, 0, 1).contiguous()[None, :, :, :]
                pixel_average = torch.tensor(self.st_image_map[k]['pixel_mean'], device=transformed_image.device)
                preprocessed_image = preprocess_image(
                    transformed_image,
                    self.image_size,
                    1,
                    pixel_average=pixel_average
                )

                output = self.sd_diffusion.forward_first_stage(
                    preprocessed_image,
                    spatial_coord,
                    latent_embedding,
                    latent_embedding_orig,
                    X_normalized,
                    st_loss_weight = st_loss_weight,
                    n_neighbor = n_neighbor,
                    upscaled_diameter = self.st_scalefactors_map[k]['spot_diameter_fullres'] * \
                        self.st_image_map[k]['original_scale'] * \
                        self.st_image_map[k]['transform_scale'],
                    k = k,
                    batch_indices=[self.batch_category_st_dict[
                        self.additional_batch_to_batch_st_dict[0][k]
                    ], self.additional_batch_category_st_dict[0][k]],
                    optimizer_idx = 1 if step % 3 == 0 else 0,
                    progress_callback = lambda x: pbar.set_postfix(
                        dict_update_and_return(pbar_postfix, x)
                    )
                )

                loss_st = output['loss_st']
                loss_latent = output['loss_latent']
                loss_ae = output['loss_ae']
                loss_disc = output['loss_disc']

                loss = (loss_st + loss_latent) * st_weight + loss_ae * si_weight

                if step % 3 == 0:
                    optimizer_d.zero_grad()
                    loss_disc.backward()
                    optimizer_d.step()
                else:
                    optimizer.zero_grad()
                    loss.backward()
                    optimizer.step()
                step += 1
                pbar_postfix['msg'] = f"Sample {k} finished optimization"
                pbar_postfix["step"] = f'{e} / {len(self.st_adatas)}'
                pbar_postfix['vram'] = print_gpu_mem(int(self.device.split(":")[-1]))[0]
                pbar_postfix['ram'] = print_cpu_mem()[0]

                pbar.set_postfix(pbar_postfix)


                torch.cuda.empty_cache()
                gc.collect()

                epoch_total_loss += loss.item()
                epoch_st_loss += loss_st.item()
                epoch_si_loss += loss_ae.item()
                
            pbar_postfix["loss_st"] = epoch_st_loss
            pbar_postfix["loss_si"] = epoch_si_loss
            pbar_postfix['msg'] = "Finished epoch"
            loss_record['epoch_total_loss'].append(epoch_total_loss)
            loss_record['epoch_st_loss'].append(epoch_st_loss)
            loss_record['epoch_si_loss'].append(epoch_si_loss)
            pbar.set_postfix(pbar_postfix)
            pbar.update(1)
            
        pbar.close()
        return loss_record

    @torch.no_grad()
    def get_sc_latent_embedding(
        self,
        latent_key: Literal["z", "q_mu"] = "q_mu",
        n_per_batch: int = 128,
        show_progress: bool = True
    ):
        return super(stModelBase, self).get_latent_embedding(
            latent_key=latent_key,
            n_per_batch=n_per_batch,
            show_progress=show_progress
        )

    @torch.no_grad()
    def get_sc_normalized_expression(
        self,
        n_per_batch: int = 128,
        show_progress: bool = True
    ):
        return super(stModelBase, self).get_normalized_expression()

    @torch.no_grad()
    def get_st_latent_embedding(
        self,
        latent_type: Literal["q", "q_mu", "gamma", "v"] = "q_mu",
        n_per_batch: int = 128,
        show_progress: bool = True,
        subset_indices_st: Optional[List] = None,
        apply_func: Optional[Callable] = None
    ) -> np.ndarray:
        self.eval()

        dataloaders = self.as_multi_dataloader(
            subset_indices_sc = list(range(len(self._dataset))), 
            subset_indices_st = subset_indices_st if subset_indices_st is not None else list(range(len(self._dataset_st))),
            n_per_batch=n_per_batch,
            shuffle=False
        )

        X_st_dl = dataloaders['st']
        X_sc_dl = dataloaders['sc']

        if show_progress:
            pbar = get_tqdm()(X_st_dl, desc="Latent Embedding", bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}')
        Zs = []

        if len(X_sc_dl) < len(X_st_dl):
            zipping = zip_longest(X_sc_dl, X_st_dl)
        else:
            zipping = zip(X_sc_dl, X_st_dl)

        for b, (X_sc, X_st) in enumerate(zipping):
            X_sc, X_st, X_st_normalized, lib_size_sc, lib_size_st, batch_index, batch_index_st, label_index, G_mask, additional_batch_index, additional_batch_index_st, st_gene_loss_weight, st_spot_loss_weight = self._prepare_batch(
                X_sc,
                X_st,
                prepare_sc = False
            )

            H = self.encode_multi(
                X_sc=X_sc,
                X_st=X_st,
                encode_sc=False
            )
            if latent_type == 'gamma':
                o = torch.sum(H['st']['gamma_st'] * H['st']['q_v_st'].unsqueeze(2),dim=1)
            elif latent_type == 'q_mu':
                o = H['st']['q_mu_st']
            elif latent_type == 'q':
                o = H['st']['q']
            elif latent_type == 'v':
                o = H['st']['q_v_st']
            else:
                raise ValueError("latent_type must be either 'q', 'gamma', or 'q_mu'")

            if apply_func is not None:
                o = apply_func(o)
            Zs.append(
                o.detach().cpu().numpy()
            )
            if show_progress:
                pbar.update(1)
        if show_progress:
            pbar.close()
        if subset_indices_st is None:
            return np.vstack(Zs)[self._shuffle_indices_st]
        return np.vstack(Zs)

    @torch.no_grad()
    def get_st_deconvolution(
        self,
        latent_key: Literal["z_st", "q_mu_st"] = "q_mu_st",
        n_per_batch: int = 128,
        show_progress: bool = True
    ) -> np.ndarray:
        self.eval()

        dataloaders = self.as_multi_dataloader(
            subset_indices_sc = list(range(len(self._dataset))), 
            subset_indices_st = list(range(len(self._dataset_st))),
            n_per_batch=n_per_batch,
            shuffle=False
        )

        X_st_dl = dataloaders['st']
        X_sc_dl = dataloaders['sc']

        if show_progress:
            pbar = get_tqdm()(X_st_dl, desc="Deconvolution", bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}')
        Zs = []
        if len(X_sc_dl) < len(X_st_dl):
            zipping = zip_longest(X_sc_dl, X_st_dl)
        else:
            zipping = zip(X_sc_dl, X_st_dl)

        for b, (X_sc, X_st) in enumerate(zipping):
            X_sc, X_st, X_st_normalized, lib_size_sc, lib_size_st, batch_index, batch_index_st, label_index, G_mask, additional_batch_index, additional_batch_index_st, st_gene_loss_weight, st_spot_loss_weight = self._prepare_batch(
                X_sc,
                X_st,
                prepare_sc=False
            )

            H = self.encode_multi(
                X_sc=X_sc,
                X_st=X_st,
                encode_sc=False
            )
            Zs.append(H['st']['q_v_st'].detach().cpu().numpy())
            if show_progress:
                pbar.update(1)

        if show_progress:
            pbar.close()
        return np.vstack(Zs)[self._shuffle_indices_st]

    def get_st_reconstructed_expression(
        self,
        k = 'px_st_rna_scale',
        n_per_batch: int = 128,
        show_progress: bool = True
    )  -> np.ndarray:
        self.eval()

        dataloaders = self.as_multi_dataloader(
            subset_indices_sc = list(range(len(self._dataset))), 
            subset_indices_st = list(range(len(self._dataset_st))),
            n_per_batch=n_per_batch,
            shuffle=False
        )

        X_st_dl = dataloaders['st']
        X_sc_dl = dataloaders['sc']

        if show_progress:
            pbar = get_tqdm()(X_st_dl, desc="Reconstruction", bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}')
        Zs = []

        if len(X_sc_dl) < len(X_st_dl):
            zipping = zip_longest(X_sc_dl, X_st_dl)
        else:
            zipping = zip(X_sc_dl, X_st_dl)

        for b, (X_sc, X_st) in enumerate(zipping):
            X_sc, X_st, X_st_normalized, lib_size_sc, lib_size_st, batch_index, batch_index_st, label_index, G_mask, additional_batch_index, additional_batch_index_st, st_gene_loss_weight, st_spot_loss_weight = self._prepare_batch(
                X_sc,
                X_st,
                prepare_sc=False
            )

            H, R, L = self.forward_multi(
                X_sc,
                X_st,
                lib_size_sc,
                lib_size_st,
                batch_index_sc=batch_index,
                batch_index_st=batch_index_st,
                additional_batch_index_sc=additional_batch_index,
                additional_batch_index_st=additional_batch_index_st,
                label_index_sc=label_index,
                G_mask=G_mask,
                forward_sc=False
            )

            Zs.append(R['st'][k].detach().cpu().numpy())
            if show_progress:
                pbar.update(1)
        if show_progress:
            pbar.close()
        return np.vstack(Zs)[self._shuffle_indices_st]

    def _prepare_batch(
        self, 
        X_sc, 
        X_st, 
        prepare_sc: bool = True, 
        prepare_st: bool = True
    ):
        prepare_sc = X_sc is not None and prepare_sc
        prepare_st = X_st is not None and prepare_st
        if prepare_sc:
            X_sc = self._dataset[X_sc.cpu().numpy()]
        if prepare_st:
            X_st = self._dataset_st[X_st.cpu().numpy()]
        batch_index, label_index, additional_label_index, additional_batch_index = (
            None, None, None, None
        )
        lib_size_sc, lib_size_st = None, None
        batch_index_st, additional_batch_index_st = None, None
        if self.n_additional_batch_ is not None:
            if self.n_batch > 0 and self.n_label > 0:
                if prepare_sc:
                    X_sc, batch_index, label_index, additional_batch_index = (
                        get_k_elements(X_sc,0),
                        get_k_elements(X_sc,1),
                        get_k_elements(X_sc,2),
                        get_last_k_elements(X_sc,3)
                    )
                    additional_batch_index = list(np.vstack(additional_batch_index).T.astype(int))
                if prepare_st:
                    X_st, X_st_normalized, G_mask, batch_index_st, additional_batch_index_st = (
                        get_k_elements(X_st,0),
                        get_k_elements(X_st,1),
                        get_k_elements(X_st,2),
                        get_k_elements(X_st,3),
                        get_last_k_elements(X_st,4)
                    )
                    additional_batch_index_st = list(np.vstack(additional_batch_index_st).T.astype(int))
        else:
            if self.n_batch > 0 and self.n_label > 0:
                if prepare_sc:
                    X_sc, batch_index, label_index = (
                        get_k_elements(X_sc,0),
                        get_k_elements(X_sc,1),
                        get_k_elements(X_sc,2)
                    )
                if prepare_st:
                    X_st, X_st_normalized, G_mask, batch_index_st = (
                        get_k_elements(X_st,0),
                        get_k_elements(X_st,1),
                        get_k_elements(X_st,2),
                        get_k_elements(X_st,3)
                    )

        if prepare_sc:
            X_sc = torch.tensor(np.vstack(list(map(lambda x: x.toarray() if issparse(x) else x, X_sc))))

        if prepare_st:
            X_st = torch.tensor(np.vstack(list(map(lambda x: x.toarray() if issparse(x) else x, X_st))))
            X_st_normalized = torch.tensor(np.vstack(list(map(lambda x: x.toarray() if issparse(x) else x, X_st_normalized))))


        if self.n_label > 0:
            if prepare_sc:
                label_index = torch.tensor(label_index)
                if not isinstance(label_index, torch.FloatTensor):
                    label_index = label_index.type(torch.FloatTensor)
                label_index = label_index.to(self.device).unsqueeze(1)

        if self.n_batch > 0:
            if prepare_sc:
                batch_index = torch.tensor(batch_index)
                if not isinstance(batch_index, torch.FloatTensor):
                    batch_index = batch_index.type(torch.FloatTensor)
                batch_index = batch_index.to(self.device).unsqueeze(1)

            if prepare_st:
                batch_index_st = torch.tensor(batch_index_st)
                if not isinstance(batch_index_st, torch.FloatTensor):
                    batch_index_st = batch_index_st.type(torch.FloatTensor)
                batch_index_st = batch_index_st.to(self.device).unsqueeze(1)

        if self.n_additional_batch_ is not None:
            if prepare_sc:
                for i in range(len(additional_batch_index)):
                    additional_batch_index[i] = torch.tensor(additional_batch_index[i])
                    if not isinstance(additional_batch_index[i], torch.FloatTensor):
                        additional_batch_index[i] = additional_batch_index[i].type(torch.FloatTensor)
                    additional_batch_index[i] = additional_batch_index[i].to(self.device).unsqueeze(1)

            if prepare_st:
                for i in range(len(additional_batch_index_st)):
                    additional_batch_index_st[i] = torch.tensor(additional_batch_index_st[i])
                    if not isinstance(additional_batch_index_st[i], torch.FloatTensor):
                        additional_batch_index_st[i] = additional_batch_index_st[i].type(torch.FloatTensor)
                    additional_batch_index_st[i] = additional_batch_index_st[i].to(self.device).unsqueeze(1)

        if prepare_sc:
            if not isinstance(X_sc, torch.FloatTensor):
                X_sc = X_sc.type(torch.FloatTensor)
            X_sc = X_sc.to(self.device)
            lib_size_sc = X_sc.sum(1).to(self.device)

        if prepare_st:
            if not isinstance(X_st, torch.FloatTensor):
                X_st = X_st.type(torch.FloatTensor)
            X_st = X_st.to(self.device)
            lib_size_st = X_st.sum(1).to(self.device)

        G_mask = torch.tensor(G_mask).to(self.device)
        knames = list(map(lambda x: 
            self.additional_batch_category_st_summary_reverse[0][int(x)],
            additional_batch_index_st[0].detach().cpu().numpy().flatten()
        ))
        st_gene_loss_weight = torch.tensor(
            list(map(lambda x: self.st_loss_weight_dict[x], knames))
        ).to(self.device)

        st_spot_loss_weight = torch.tensor(
            list(map(lambda x: self.sample_spot_numbers_weight_dict[x], knames))
        ).to(self.device)

        return X_sc, X_st, X_st_normalized, lib_size_sc, lib_size_st, batch_index, batch_index_st, label_index, G_mask, additional_batch_index, additional_batch_index_st, st_gene_loss_weight, st_spot_loss_weight

    def debug(self, flag, path=None):
        self._debug = flag
        if hasattr(self, 'si_transformer'):
            self.si_transformer._debug = flag
        if hasattr(self, 'sd_diffusion'):
            self.sd_diffusion._debug = flag
    
        if path is not None:
            self.set_debug_output_path(path)

    def set_debug_output_path(self, path):
        self._debug_output_path = path
        if hasattr(self, 'si_transformer'):
            self.si_transformer._debug_output_path = path
        if hasattr(self, 'sd_diffusion'):
            self.sd_diffusion._debug_output_path = path

class stPromptEncoder(PromptEncoder):
    def __init__(
        self,
        embed_dim: int,
        n_latent,
        image_embedding_size: Tuple[int, int],
        input_image_size: Tuple[int, int],
        mask_in_chans: int,
        activation: Type[nn.Module] = nn.GELU,
    ):
        super().__init__(
            embed_dim=embed_dim,
            image_embedding_size=image_embedding_size,
            input_image_size=input_image_size,
            mask_in_chans=mask_in_chans,
            activation=activation,
        )
        self.no_mask_embed = nn.Embedding(1, embed_dim * 2)
        self.mask_downscaling = nn.Sequential(
            nn.Conv2d(1, mask_in_chans // 4, kernel_size=2, stride=2),
            LayerNorm2d(mask_in_chans // 4),
            activation(),
            nn.Conv2d(mask_in_chans // 4, mask_in_chans, kernel_size=2, stride=2),
            LayerNorm2d(mask_in_chans),
            activation(),
            nn.Conv2d(mask_in_chans, embed_dim * 2, kernel_size=1),
        )
        self.pe_layer = PositionEmbeddingRandom(embed_dim // 2)
        self.n_latent = n_latent

    def _embed_points(
        self,
        points: torch.Tensor,
        labels: torch.Tensor,
        latents: torch.Tensor,
        pad: bool,
    ) -> torch.Tensor:
        """Embeds point prompts."""
        if pad:
            padding_point = torch.zeros((points.shape[0], 1, 2), device=points.device)
            padding_label = -torch.ones((labels.shape[0], 1), device=labels.device)
            padding_latent = torch.zeros((latents.shape[0], 1, latents.shape[2]), device=latents.device)
            points = torch.cat([points, padding_point], dim=1)
            labels = torch.cat([labels, padding_label], dim=1)
            latents = torch.cat([latents, padding_latent], dim=1)

        point_embedding = self.pe_layer.forward_with_coords(points, self.input_image_size)

        point_embedding[labels == -1] = 0.0
        point_embedding[labels == -1] += self.not_a_point_embed.weight
        point_embedding[labels == 0] += self.point_embeddings[0].weight
        point_embedding[labels == 1] += self.point_embeddings[1].weight
        point_embedding = torch.cat([point_embedding, latents], dim=2)
        return point_embedding

    def forward(
        self,
        points: Optional[Tuple[torch.Tensor, torch.Tensor, torch.Tensor]],
        boxes: Optional[torch.Tensor],
        masks: Optional[torch.Tensor],
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Embeds different types of prompts, returning both sparse and dense
        embeddings.

        Arguments:
          points (tuple(torch.Tensor, torch.Tensor) or none): 
                 point coordinates, labels, and latent to embed.
          boxes (torch.Tensor or none): boxes to embed
          masks (torch.Tensor or none): masks to embed

        Returns:
          torch.Tensor: sparse embeddings for the points and boxes, with shape
            BxNx(embed_dim), where N is determined by the number of input points
            and boxes.
          torch.Tensor: dense embeddings for the masks, in the shape
            Bx(embed_dim)x(embed_H)x(embed_W)
        """
        bs = self._get_batch_size(points, boxes, masks)
        sparse_embeddings = torch.empty((bs, 0, self.embed_dim * 2), device=self._get_device())
        if points is not None:
            coords, labels, latents = points
            point_embeddings = self._embed_points(coords, labels, latents, pad=(boxes is None))
            sparse_embeddings = torch.cat([sparse_embeddings, point_embeddings], dim=1)
        if boxes is not None:
            box_embeddings = self._embed_boxes(boxes)
            sparse_embeddings = torch.cat([sparse_embeddings, box_embeddings], dim=1)

        if masks is not None:
            dense_embeddings = self._embed_masks(masks)
            dense_embeddings = F.interpolate(
                dense_embeddings.unsqueeze(0),
                (
                    self.image_embedding_size[0],
                    self.image_embedding_size[1]
                ),
                mode="bilinear",
                align_corners=False,
            )
        else:
            dense_embeddings = self.no_mask_embed.weight.reshape(1, -1, 1, 1).expand(
                bs, -1, self.image_embedding_size[0], self.image_embedding_size[1]
            )

        return sparse_embeddings, dense_embeddings

class siTransformer(nn.Module):
    def __init__(self, *,
        gene_dim: int,
        n_hidden:int,
        encoder_backend: Literal['sam','hipt'] = 'sam',
        si_to_st_method: Literal['softmax', 'softplus', 'sigmoid', 'deconvolution'] = 'softmax',
        si_to_st_function: Optional[Callable] = None,
        si_to_st_loss: Literal['mse', 'bce'] = 'mse',
        si_to_st_reconstruction_method: Literal['sum', 'mean'] = 'sum',
        st_deconvolution_method: Literal['softmax', 'softplus'] = 'softplus',
        encoder_embed_dim: int = 768,
        encoder_depth: int = 6,
        encoder_num_heads: int = 4,
        encoder_global_attn_indexes: int = [2,5],
        prompt_embed_dim: int = 128,
        decoder_num_heads: int = 4,
        pixel_mean: List[float] = [123.675, 116.28, 103.53],
        pixel_std: List[float] = [58.395, 57.12, 57.375],
        num_multimask_outputs: int = 3,
        iou_head_depth: int = 3,
        iou_head_hidden_dim: int = 256,
        n_label: Optional[int] = None,
        image_size: int = 1024,
        _debug: bool = False,
        _debug_output_path: str = '/tmp',
        _adata: Optional[sc.AnnData] = None,
        _st_adatas: Optional[Dict[str, sc.AnnData]] = None,
        device: str = 'cpu'
    ):
        super(siTransformer, self).__init__()
        
        vit_patch_size = 16

        self.pixel_mean = torch.tensor(pixel_mean, device=device).view(1, -1, 1, 1).float()
        self.pixel_std = torch.tensor(pixel_std, device=device).view(1, -1, 1, 1).float()
        self.encoder_backend = encoder_backend
        self.si_to_st_method = si_to_st_method
        self.si_to_st_loss = si_to_st_loss
        self.si_to_st_reconstruction_method = si_to_st_reconstruction_method
        self.st_deconvolution_method = st_deconvolution_method
        self.n_hidden = n_hidden
        self.gene_dim = gene_dim
        self._debug = _debug
        self._debug_output_path = _debug_output_path
        self._adata = _adata
        self._st_adatas = _st_adatas
        self.image_size = image_size
        self.n_label = n_label
        self.si_to_st_function = si_to_st_function

        if si_to_st_method == 'deconvolution':
            if n_label is None:
                raise ValueError("n_label should be provided when si_to_st_method is 'deconvolution'.")
            if si_to_st_function is None:
                raise ValueError("si_to_st_function should be provided when si_to_st_method is 'deconvolution'.")
            

        if encoder_backend == 'sam':
            self.image_encoder = ImageEncoderViT(
                depth=encoder_depth,
                embed_dim=encoder_embed_dim,
                img_size=self.image_size,
                mlp_ratio=4,
                norm_layer=partial(torch.nn.LayerNorm, eps=1e-6),
                num_heads=encoder_num_heads,
                patch_size=vit_patch_size,
                qkv_bias=True,
                use_rel_pos=True,
                global_attn_indexes=encoder_global_attn_indexes,
                window_size=14,
                out_chans=prompt_embed_dim * 2,
            )
            self.image_encoder_transition = nn.Linear(
                256, prompt_embed_dim * 2
            )

        elif encoder_backend == 'hipt':
            self.image_encoder = HIPT_4K(device256=device, device4k=device)
            self.image_encoder_transition = nn.Linear(
                384, prompt_embed_dim * 2
            )
        else:
            raise ValueError("encoder_backend should either be 'sam' or 'hipt'.")
        
        self.image_encoder.img_size = self.image_size
        image_embedding_size = self.image_size // vit_patch_size
        self.image_decoder = nn.Linear(prompt_embed_dim // 8, 3)


        self.prompt_encoder = stPromptEncoder(
            embed_dim=prompt_embed_dim,
            n_latent=prompt_embed_dim,
            image_embedding_size=(image_embedding_size, image_embedding_size),
            input_image_size=(self.image_size, self.image_size),
            mask_in_chans=16,
        )

        self.transform = ResizeLongestSide(self.image_encoder.img_size)

        self.twowaytransformer = TwoWayTransformer(
            depth=2,
            embedding_dim=prompt_embed_dim * 2,
            mlp_dim=2048,
            num_heads=decoder_num_heads
        )
        
        transformer_dim = prompt_embed_dim * 2
        
        self.output_upscaling = nn.Sequential(
            nn.ConvTranspose2d(transformer_dim, transformer_dim // 4, kernel_size=2, stride=2),
            LayerNorm2d(transformer_dim // 4),
            nn.GELU(),
            nn.ConvTranspose2d(transformer_dim // 4, transformer_dim // 8, kernel_size=2, stride=2),
            LayerNorm2d(transformer_dim // 8),
            nn.GELU(),
            nn.ConvTranspose2d(transformer_dim // 8, transformer_dim // 16, kernel_size=2, stride=2),
            nn.GELU(),
        )

        self.iou_token = nn.Embedding(1, prompt_embed_dim * 2)
        self.mask_tokens = nn.Embedding(1, prompt_embed_dim * 2)
        self.num_mask_tokens = num_multimask_outputs + 1
        
        self.output_hypernetworks_mlps = nn.ModuleList(
            [
                MLP(transformer_dim, transformer_dim, transformer_dim // 8, 3)
                for i in range(self.num_mask_tokens)
            ]
        )

        self.iou_prediction_head = MLP(
            transformer_dim, iou_head_hidden_dim, self.num_mask_tokens, iou_head_depth
        )
        
        if self.si_to_st_method == 'deconvolution':
            self.si_upscaled_embedding_to_n_label_fc = nn.Linear(
                self.n_hidden // 8,
                n_label
            )


            
        else:
            self.si_upscaled_embedding_to_px_rna = nn.Linear(
                self.n_hidden // 8,
                128
            )
            self.si_upscaled_embedding_to_gex_scale = nn.Linear(
                128,
                self.gene_dim
            )
            self.si_upscaled_embedding_to_gex_rate = nn.Linear(
                128,
                self.gene_dim
            )
            self.si_upscaled_embedding_to_gex_dropout = nn.Linear(
                128,
                self.gene_dim
            )

        self.device = device
    
    def set_pixel_mean_std(self, pixel_mean, pixel_std):
        self.pixel_mean = torch.tensor(pixel_mean, device=self.device).view(1, -1, 1, 1).float()
        self.pixel_std = torch.tensor(pixel_std, device=self.device).view(1, -1, 1, 1).float()
    
    def forward(
        self,
        input_image: torch.Tensor,
        spatial_coord: torch.Tensor,
        latent_embedding: torch.Tensor,
        X: torch.Tensor,
        st_loss_weight: torch.Tensor = None,
        n_neighbor: int = 1,
        upscaled_diameter: float = 40,
        k: str = None,
        batch_indices: Optional[List[int]] = None,
        progress_callback: Optional[Callable] = None,
    ):
        preprocessed_image = input_image
        preprocessed_image = preprocessed_image.to(self.device)
        if self.encoder_backend == 'sam':
            image_embedding = self.image_encoder(preprocessed_image)
            image_embedding = einops.rearrange(
                image_embedding,
                'n e a b -> n a b e'
            )
            image_embedding = self.image_encoder_transition(image_embedding)
            image_embedding = einops.rearrange(
                image_embedding,
                'n w h e -> n e w h'
            )
            
        else:
            image_embedding = self.image_encoder.forward_all256(preprocessed_image)
            image_embedding = einops.rearrange(
                image_embedding[1],
                'n e a b c d -> n (a c) (b d) e'
            )
            image_embedding = self.image_encoder_transition(image_embedding)
            image_embedding = einops.rearrange(
                image_embedding,
                'n w h e -> n e w h'
            )
        
        # Start computing the image/ST mask
        coordinates = np.indices((
            self.image_encoder.img_size, 
            self.image_encoder.img_size
        )).transpose(1, 2, 0)
        coordinates_flat = einops.rearrange(coordinates, 'a b c -> (b a) c')

        neighbors = NearestNeighbors(n_neighbors=n_neighbor)
        neighbors.fit(spatial_coord.detach().cpu().numpy())

        D, I = neighbors.kneighbors(coordinates_flat)

        mask_d = (D.min(1) > 20 * (self.image_encoder.img_size // 1024)).reshape((
            self.image_encoder.img_size, 
            self.image_encoder.img_size
        )).astype(np.uint8)

        mask = np.zeros(mask_d.shape, dtype=np.bool)
        mask_final = np.zeros(mask_d.shape)
        
        hull = Delaunay(spatial_coord.detach().cpu().numpy())
        mask[(hull.find_simplex(coordinates) == -1).reshape((
            self.image_encoder.img_size, 
            self.image_encoder.img_size
        ))] = True

        contours, _ = cv2.findContours(mask_d, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(mask_final, contours, -1, (255,255,255), cv2.FILLED)
        mask = ~np.bitwise_and(~mask.astype(np.bool).T, mask_final.astype(np.bool)) 


        original_mask = mask.copy()
        # Finish computing the image/ST mask
        progress_callback(dict(progress = "Finished computing the image/ST mask"))

        sparse_embedding, dense_embedding = self.prompt_encoder(
            points=(
                torch.tensor(spatial_coord).unsqueeze(0),
                torch.ones(spatial_coord.shape[0], device=self.device).unsqueeze(0),
                torch.tensor(latent_embedding, device=self.device).unsqueeze(0),
            ),
            boxes=None,
            masks=torch.tensor(~mask, device=self.device).unsqueeze(0).float(),
        )
        output_tokens = torch.cat([
            self.iou_token.weight,
            self.mask_tokens.weight
        ], dim=0)

        output_tokens = output_tokens.unsqueeze(0).expand(sparse_embedding.size(0), -1, -1)
        tokens = torch.cat((output_tokens, sparse_embedding), dim=1)

        # Expand per-image data in batch direction to be per-mask
        src = torch.repeat_interleave(image_embedding, tokens.shape[0], dim=0)
        post_src = src + dense_embedding
        image_pe = self.prompt_encoder.get_dense_pe()
        pos_src = torch.repeat_interleave(image_pe, tokens.shape[0], dim=0)
        pos_src = torch.cat([pos_src,pos_src],dim=1)
        b, c, h, w = src.shape

        hs, post_src = self.twowaytransformer(post_src, pos_src, tokens)
        post_src = post_src.transpose(1, 2).view(b, c, h, w)

        upscaled_embedding = self.output_upscaling(post_src)
        upscaled_embedding_pre = self.output_upscaling(src)
        
        upscaled_embedding = F.interpolate(
            upscaled_embedding,
            (
                self.image_encoder.img_size, 
                self.image_encoder.img_size
            ),
            mode="bilinear",
            align_corners=False,
        )

        upscaled_image_reconstruction = self.image_decoder(
            einops.rearrange(upscaled_embedding_pre, 'a b c d -> a c d b')
        )
        
        # if self.encoder_backend == 'hipt':
        # upscaled_image_reconstruction = F.sigmoid(upscaled_image_reconstruction)


        mask = (D.min(1) > (upscaled_diameter / 2)).reshape((
            self.image_encoder.img_size, 
            self.image_encoder.img_size
        ))    
        indices = np.argwhere(~mask)
        for i in indices[
            np.random.choice(
                list(range(indices.shape[0])), 
                size=indices.shape[0] - min(100000, (~mask).sum()), 
                replace=False
            )
        ]:
            mask[i[0],i[1]] = True
        indices = np.argwhere(~mask)
        
        I_for_loss = I[einops.rearrange(~mask, 'a b -> (a b)')] 
        D_for_loss = D[einops.rearrange(~mask, 'a b -> (a b)')]
        uindices = np.unique(I_for_loss)
        I_for_loss_aggr = sorted( zip(
            uindices, 
            [np.argwhere(I_for_loss == i)[:,0] for i in uindices]
        ), key=lambda x: x[0])
        m = max(list(map(lambda x: x[1].shape[0], I_for_loss_aggr)))
        I_for_loss_spatial_coords = torch.tensor(list(map(lambda x: x[0], I_for_loss_aggr)))
        I_for_loss_image_indices = torch.vstack(list(map(lambda x: F.pad(x[0], (0, m-x[1]), value=-1), zip(
            list(map(lambda x: torch.tensor(x[1]), I_for_loss_aggr)), 
            list(map(lambda x: x[1].shape[0], I_for_loss_aggr))
        ))))
        I_for_loss_image_mask = I_for_loss_image_indices != -1
        I_for_loss_image_indices[I_for_loss_image_indices==-1] = 0

        X_for_loss = X[I_for_loss].unsqueeze(0).to(self.device)
        lib_size = X[I_for_loss].unsqueeze(0).to(self.device).sum(-1)

        upscaled_embedding_within_splots = einops.rearrange(upscaled_embedding[:,:,~mask], 'b d n -> b n d')
                

        if self.si_to_st_method == "deconvolution":
            upscaled_x_within_spots_v = self.si_upscaled_embedding_to_n_label_fc(
                upscaled_embedding_within_splots
            )
            if self.st_deconvolution_method == 'softmax':
                upscaled_x_within_spots_v = F.softmax(upscaled_x_within_spots_v)
            elif self.st_deconvolution_method == 'softplus':
                upscaled_x_within_spots_v = F.softplus(upscaled_x_within_spots_v)
                upscaled_x_within_spots_v = upscaled_x_within_spots_v / upscaled_x_within_spots_v.sum(axis=-1).reshape(-1,1)
                upscaled_x_within_spots_v = upscaled_x_within_spots_v.view(-1, self.n_label)

            upscaled_x_within_spots_scale = self.si_to_st_function(upscaled_x_within_spots_v, batch_indices)
            
        else:
            upscaled_embedding_within_spots_px = self.si_upscaled_embedding_to_px_rna(
                upscaled_embedding_within_splots
            )

            upscaled_x_within_spots_scale = self.si_upscaled_embedding_to_gex_scale(
                upscaled_embedding_within_spots_px
            )

            if self.si_to_st_loss == "bce":
                if self.si_to_st_method == "softmax":
                    upscaled_x_within_spots_scale = nn.Softmax(dim=-1)(upscaled_x_within_spots_scale)
                elif self.si_to_st_method == "softplus":
                    upscaled_x_within_spots_scale = F.softplus(upscaled_x_within_spots_scale)
                    upscaled_x_within_spots_scale = upscaled_x_within_spots_scale / \
                        upscaled_x_within_spots_scale.sum(axis=-1).unsqueeze(-1)
                elif self.si_to_st_method == "sigmoid":
                    upscaled_x_within_spots_scale = torch.sigmoid(upscaled_x_within_spots_scale)
                else:
                    raise ValueError("si_to_st_method should either be 'softmax', 'softplus', or 'sigmoid'.")

        

        mask_tokens_out = hs[:, 1 : (1 + self.num_mask_tokens), :]
        iou_token_out = hs[:, 0, :]
        hyper_in_list: List[torch.Tensor] = []
        for i in range(self.num_mask_tokens):
            hyper_in_list.append(self.output_hypernetworks_mlps[i](mask_tokens_out[:, i, :]))
        hyper_in = torch.stack(hyper_in_list, dim=1)
        b, c, h, w = upscaled_embedding.shape
        # masks = (hyper_in @ upscaled_embedding.view(b, c, h * w)).view(b, -1, h, w)
        # Generate mask quality predictions
        # iou_pred = self.iou_prediction_head(iou_token_out)


        if self.si_to_st_loss == "mse":
            upscaled_x_within_spots_scale_repeated = einops.repeat(
                upscaled_x_within_spots_scale, 
                'b n d -> b n k d', k = n_neighbor
            )
            if self.si_to_st_reconstruction_method == "sum":
                loss_st = LossFunction.mse(
                    einops.rearrange(
                        X_for_loss,
                        'a b c d -> (a b c) d'
                    ),
                    einops.rearrange(
                        upscaled_x_within_spots_scale_repeated,
                        'a b c d -> (a b c) d'
                    ),
                    reduction = 'none'
                )
            else: 
                upscaled_x_within_spots_scale_averaged = ((upscaled_x_within_spots_scale[0][I_for_loss_image_indices] * \
                    I_for_loss_image_mask.unsqueeze(-1)
                ).sum(1) / I_for_loss_image_mask.sum(1).unsqueeze(1))
                loss_st = LossFunction.mse(
                    X,
                    upscaled_x_within_spots_scale_averaged,
                    reduction = 'none'
                )
            
        elif self.si_to_st_loss == "bce":
            loss_st = LossFunction.bce_reconstruction_loss(
                X,
                upscaled_x_within_spots_scale_averaged,
                reduction = 'none'
            )
            loss_st = loss_st.mean(0)
        else:
            raise ValueError("si_to_st_loss should either be 'mse' or 'bce'.")

        if st_loss_weight is not None:
            loss_st = (loss_st * st_loss_weight).mean()
        else:
            loss_st = loss_st.mean()

        loss_si = (
            ( 255 * upscaled_image_reconstruction ) - 
            ( 255 * einops.rearrange(
                F.interpolate(
                    preprocessed_image,
                    (
                        self.image_encoder.img_size // 2,
                        self.image_encoder.img_size // 2,
                    ),
                    mode="bilinear",
                    align_corners=False,
                ), 'b c w h -> b w h c'))
        ) ** 2
        mask_torch = F.interpolate(
            torch.from_numpy(~original_mask).to(upscaled_image_reconstruction.device)
            .unsqueeze(0).unsqueeze(0).float(),
            (
                self.image_encoder.img_size // 2,
                self.image_encoder.img_size // 2,
            ),
            mode="bilinear",
            align_corners=False,
        ).squeeze().bool()
        loss_si = (loss_si * mask_torch.unsqueeze(-1).float()).sum() / (mask_torch).sum()

        if self._debug and k is not None:
            import matplotlib
            import matplotlib.pyplot as plt

            for i in ['COL3A1','S100A9']:
                fig,ax=plt.subplots()
                upscaled_x = np.zeros((
                    upscaled_embedding.shape[2],
                    upscaled_embedding.shape[3]
                ))
                x = MaxAbsScaler().fit_transform(
                    upscaled_x_within_spots_scale_repeated[
                        :,:,0,
                        list(self._adata.var.index).index(i)
                    ].detach().cpu().numpy().T
                ).T[0]
                upscaled_x[~mask] = x
                plt.imshow(
                    matplotlib.cm.viridis(upscaled_x), 
                    vmin=upscaled_x[~mask].min(), 
                    vmax=upscaled_x[~mask].max()
                )
                if self.encoder_backend == 'hipt':
                    fig.savefig(f'{self._debug_output_path}/hipt_{k}_tmp_{i}.png', dpi=150)
                else:
                    fig.savefig(f'{self._debug_output_path}/sam_{k}_tmp_{i}.png', dpi=150)
                plt.close()

            fig,ax=plt.subplots()
            upscaled_x = np.zeros((
                upscaled_embedding.shape[2],
                upscaled_embedding.shape[3]
            ))
            upscaled_x[~mask] = MaxAbsScaler().fit_transform(
                upscaled_x_within_spots_scale_repeated[
                    :,:,0,
                    [list(self._adata.var.index).index(x) for x in get_spatial_gene_set(self._adata, 'TLS')]
                ].mean(-1).detach().cpu().numpy().T
            ).T[0]
            plt.imshow(
                matplotlib.cm.viridis(upscaled_x), 
                vmin=upscaled_x[~mask].min(), 
                vmax=upscaled_x[~mask].max()
            )

            if self.encoder_backend == 'hipt':
                fig.savefig(f'{self._debug_output_path}/hipt_{k}_tmp_TLS.png', dpi=150)
            else:
                fig.savefig(f'{self._debug_output_path}/sam_{k}_tmp_TLS.png', dpi=150)
            plt.close()

            
        return dict(
            loss_st = loss_st,
            loss_si = loss_si,
            upscaled_x_within_spots_scale = upscaled_x_within_spots_scale,
            upscaled_embedding = upscaled_embedding,
            upscaled_embedding_within_splots = upscaled_embedding_within_splots,
            mask = mask,
            # predicted_mask = masks,
            # iou_pred = iou_pred,
        )

class sitDiffusion(nn.Module):
    def __init__(
        self,
        latent_dim: int,
        px_rna_dim: int,
        gene_dim: int, 
        image_size: int,
        image_embedding_size: int,
        si_autoencoder_config,
        si_diffusion_config,
        prompt_embed_dim: int,
        si_to_st_method: Literal['deconvolution','none'] = 'none',
        si_to_st_n_labels: Optional[int] = None,
        si_to_st_function: Optional[Callable] = None,
        si_to_st_reconstruction_method: Literal['sum', 'mean'] = 'sum',
        device: Optional[Union[str, torch.device]] = None,
        cond_stage_function: Optional[Callable] = None,
        _debug: bool = False,
        _debug_output_path: str = '/tmp',
        _adata: sc.AnnData = None,
        _st_adatas: Dict[str, sc.AnnData] = None,
    ):
        super().__init__()
        self.first_stage_model = stAutoEncoderKL(
            latent_dim = latent_dim,
            px_rna_dim = px_rna_dim,
            gene_dim = gene_dim,
            ddconfig = si_autoencoder_config['ddconfig'],
            lossconfig = si_autoencoder_config['lossconfig'],
            embed_dim = prompt_embed_dim * 2,
            si_to_st_method = si_to_st_method,
            si_to_st_n_labels = si_to_st_n_labels,
        )
        self.second_stage_model = stLatentDiffusion(
            unet_config = si_diffusion_config['unet_config'],
            cond_stage_function=cond_stage_function,
            **{k:v for k,v in 
               si_diffusion_config.items() 
               if type(v) != omegaconf.dictconfig.DictConfig
            }
        )
        self.image_size = image_size
        self.prompt_encoder = stPromptEncoder(
            embed_dim=prompt_embed_dim,
            n_latent=prompt_embed_dim,
            image_embedding_size=(image_embedding_size, image_embedding_size),
            input_image_size=(self.image_size, self.image_size),
            mask_in_chans=16,
        )

        self.twowaytransformer = TwoWayTransformer(
            depth=2,
            embedding_dim=prompt_embed_dim * 2,
            mlp_dim=32,
            num_heads=8
        )

        self.si_to_st_method = si_to_st_method
        if si_to_st_method == 'deconvolution':
            if si_to_st_function is None:
                raise ValueError("si_to_st_function should be provided when si_to_st_method is 'deconvolution'.")
            self.si_to_st_function = si_to_st_function
        self.si_to_st_reconstruction_method = si_to_st_reconstruction_method

        self.device = device
        self._debug = _debug
        self._debug_output_path = _debug_output_path
        self._adata = _adata
        self._st_adatas = _st_adatas

    def set_cond_stage_function(self, cond_stage_function):
        self.second_stage_model.set_cond_stage_function(cond_stage_function)

    def forward_first_stage(
        self,
        input_image: torch.Tensor,
        spatial_coord: torch.Tensor,
        latent_embedding: torch.Tensor,
        latent_embedding_original: torch.Tensor,
        X: torch.Tensor,
        st_loss_weight: torch.Tensor = None,
        n_neighbor: int = 1,
        upscaled_diameter: float = 40,
        k: str = None,
        batch_indices: Optional[List[int]] = None,
        optimizer_idx: str = 0,
        progress_callback: Optional[Callable] = None,
    ):
        posterior = self.first_stage_model.encode(input_image)
        src = posterior.sample() 

        img_size = input_image.shape[-2:]

        coordinates = np.indices((
            img_size[0],
            img_size[1]
        )).transpose(1, 2, 0)
        coordinates_flat = einops.rearrange(coordinates, 'a b c -> (b a) c')

        neighbors = NearestNeighbors(n_neighbors=n_neighbor)
        neighbors.fit(spatial_coord.detach().cpu().numpy())
        D, I = neighbors.kneighbors(coordinates_flat)
        mask_d = (D.min(1) < 10 * (img_size[0] // 512)).reshape((
            img_size[0],
            img_size[1]
        )).astype(np.uint8)

        mask = np.zeros(mask_d.shape, dtype=np.bool)
        mask_final = np.zeros(mask_d.shape)

        hull = Delaunay(spatial_coord.detach().cpu().numpy())

        mask[(hull.find_simplex(coordinates) == -1).reshape((
            img_size[0],
            img_size[1]
        ))] = True

        contours, _ = cv2.findContours(mask_d, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(mask_final, contours, -1, (255,255,255), cv2.FILLED)
        mask = ~np.bitwise_and(~mask.astype(np.bool).T, mask_final.astype(np.bool)) 

        original_mask = mask.copy()

        sparse_embedding, dense_embedding = self.prompt_encoder(
            points=(
                torch.tensor(spatial_coord).unsqueeze(0),
                torch.ones(spatial_coord.shape[0], device=self.device).unsqueeze(0),
                torch.tensor(latent_embedding, device=self.device).unsqueeze(0),
            ),
            boxes=None,
            masks=torch.tensor(~mask, device=self.device).unsqueeze(0).float(),
        )

        b, c, h, w = dense_embedding.shape
        image_pe = self.prompt_encoder.get_dense_pe()
        pos_src = torch.repeat_interleave(image_pe, sparse_embedding.shape[0], dim=0)
        pos_src = torch.cat([pos_src,pos_src],dim=1)
        hs, post_src = self.twowaytransformer(src + dense_embedding, pos_src, sparse_embedding)
        post_src = post_src.transpose(1, 2).view(b, c, h, w)

        z = self.first_stage_model.post_quant_conv(post_src)

        dec = self.first_stage_model.decoder(z)
        dec_pc = None

        if self.si_to_st_method  == 'deconvolution':
            dec_pc, dec_latent = self.first_stage_model.gene_decoder(z)
            b, c, h, w = dec_pc.shape
        else:
            dec_gene, dec_latent = self.first_stage_model.gene_decoder(z)

        mask = (D.min(1) > (upscaled_diameter / 2)).reshape((
            img_size[0],
            img_size[1]
        ))
        raw_mask = mask.copy()
        indices = np.argwhere(~mask)
        if self.si_to_st_method == 'deconvolution':
            subset = 10000
        else:
            subset = 100000

        for i in indices[
            np.random.choice(
                list(range(indices.shape[0])), 
                size=indices.shape[0] - min(subset, (~mask).sum()), 
                replace=False
            )
        ]:
            mask[i[0],i[1]] = True
        indices = np.argwhere(~mask)

        def create_mask_indices(mask):
            I_for_loss = I[einops.rearrange(~mask, "a b -> (a b)")]
            D_for_loss = D[einops.rearrange(~mask, "a b -> (a b)")]
            uindices = np.unique(I_for_loss)
            I_for_loss_aggr = sorted(
                zip(uindices, [np.argwhere(I_for_loss == i)[:, 0] for i in uindices]),
                key=lambda x: x[0],
            )
            m = max(list(map(lambda x: x[1].shape[0], I_for_loss_aggr)))
            I_for_loss_spatial_coords = torch.tensor(
                list(map(lambda x: x[0], I_for_loss_aggr))
            )
            I_for_loss_image_indices = torch.vstack(
                list(
                    map(
                        lambda x: F.pad(x[0], (0, m - x[1]), value=-1),
                        zip(
                            list(map(lambda x: torch.tensor(x[1]), I_for_loss_aggr)),
                            list(map(lambda x: x[1].shape[0], I_for_loss_aggr)),
                        ),
                    )
                )
            ).to(self.device)
            I_for_loss_image_mask = I_for_loss_image_indices != -1
            I_for_loss_image_indices[I_for_loss_image_indices == -1] = 0

            return (
                I_for_loss,
                D_for_loss,
                I_for_loss_aggr,
                I_for_loss_spatial_coords,
                I_for_loss_image_indices,
                I_for_loss_image_mask,
                uindices
            )

        (
            I_for_loss,
            D_for_loss,
            I_for_loss_aggr,
            I_for_loss_spatial_coords,
            I_for_loss_image_indices,
            I_for_loss_image_mask,
            uindices
        ) = create_mask_indices(mask)
        X_for_loss = X[I_for_loss].unsqueeze(0).to(self.device)

        (
            I_for_loss_original,
            D_for_loss_original,
            I_for_loss_aggr_original,
            I_for_loss_spatial_coords_original,
            I_for_loss_image_indices_original,
            I_for_loss_image_mask_original,
            uindices_original
        ) = create_mask_indices(raw_mask)

        dec_latent_within_spot = einops.rearrange(dec_latent[:,:,~mask], 'b d n -> b n d')
        dec_latent_averaged = ((dec_latent_within_spot[0][I_for_loss_image_indices] * \
            I_for_loss_image_mask.unsqueeze(-1)
        ).sum(1) / I_for_loss_image_mask.sum(1).unsqueeze(1))

        loss_latent = LossFunction.mse(
            latent_embedding_original[uindices], 
            dec_latent_averaged
        ).sum()

        if self._debug:
            import matplotlib.pyplot as plt 
            plt.rcParams['font.size']= 2
            fig,axes=plt.subplots(2,3,figsize=(7,3))
            axes[0][0].imshow(
                einops.rearrange(torch.clamp(dec[0], 0.0, 1.0), "c w h -> w h c")
                .detach()
                .cpu()
                .numpy()
            )

            x = dec_latent[0].mean(0).detach().cpu().numpy()
            vmin, vmax = x[~original_mask].min(), x[~original_mask].max()
            x[original_mask] = vmin
            axes[0][1].imshow(x, vmin=vmin, vmax=vmax)

            if self.si_to_st_method != 'deconvolution':

                x = dec_gene[0][list(self._adata.var.index).index('COL3A1')].detach().cpu().numpy()
                vmin, vmax = x[~original_mask].min(), x[~original_mask].max()
                x[original_mask] = vmin
                axes[0][2].imshow(x, vmin=vmin, vmax=vmax)

                sc.pl.spatial(
                    self._st_adatas[k],
                    color='COL3A1',
                    show=False,
                    ax=axes[1][0],
                    layer='normalized',
                    alpha_img=0.25,
                )

            if self.si_to_st_method == 'deconvolution':
                pass
            else:
                dec_gene_within_spot = einops.rearrange(
                    dec_gene.detach().cpu()[:, :, ~raw_mask], "b d n -> b n d"
                )
                I_for_loss_image_indices_original = I_for_loss_image_indices_original.cpu()
                I_for_loss_image_mask_original = I_for_loss_image_mask_original.cpu()
                dec_gene_averaged = (
                    dec_gene_within_spot[0][I_for_loss_image_indices_original]
                    * I_for_loss_image_mask_original.unsqueeze(-1)
                ).sum(1) / I_for_loss_image_mask_original.sum(1).unsqueeze(1)
                self._st_adatas[k].layers["decoded"] = (
                    dec_gene_averaged.detach().cpu().numpy()
                )

                sc.pl.spatial(
                    self._st_adatas[k],
                    color='COL3A1',
                    show=False,
                    ax=axes[1][1],
                    layer='decoded',
                    alpha_img=0.25,
                )

            fig.savefig(f"{self._debug_output_path}/tmp_{k}.png")
            plt.close()

        if self.si_to_st_method == "deconvolution":
            dec_pc_within_spot = einops.rearrange(dec_pc[:,:,~mask], 'b d n -> b n d')
            dec_gene_within_spot = self.si_to_st_function(dec_pc_within_spot, batch_indices).unsqueeze(2)

            if self.si_to_st_reconstruction_method == "sum":
                loss_st = LossFunction.mse(
                    einops.rearrange(
                        X_for_loss,
                        'a b c d -> (a b c) d'
                    ),
                    dec_gene_within_spot,
                    reduction = 'none'
                ).sum()

            elif self.si_to_st_reconstruction_method == "mean":
                print(dec_gene_within_spot.shape, I_for_loss_image_indices.shape, I_for_loss_image_mask.shape)
                dec_gene_averaged = ((dec_gene_within_spot[0][I_for_loss_image_indices] * \
                    I_for_loss_image_mask.unsqueeze(-1)
                ).sum(1) / I_for_loss_image_mask.sum(1).unsqueeze(1))
                print(dec_gene_averaged.shape, X.shape)
                loss_st = LossFunction.mse(
                    X,
                    dec_gene_averaged,
                    reduction = 'none'
                )

            if st_loss_weight is not None:
                loss_st = (loss_st * st_loss_weight).mean()
            else:
                loss_st = loss_st.sum()

        else:
            if self.si_to_st_reconstruction_method == "sum":
                loss_st = LossFunction.mse(
                    einops.rearrange(
                        X_for_loss,
                        'a b c d -> (a b c) d'
                    ),
                    einops.rearrange(
                        dec_gene[:,:,~mask],
                        'b d n -> b n d'
                    ),
                    reduction = 'none'
                ).sum()

            elif self.si_to_st_reconstruction_method == "mean":
                dec_gene_within_spot = einops.rearrange(
                    dec_gene[:, :, ~mask], "b d n -> b n d"
                )
                dec_gene_averaged = (
                    dec_gene_within_spot[0][I_for_loss_image_indices]
                    * I_for_loss_image_mask.unsqueeze(-1)
                ).sum(1) / I_for_loss_image_mask.sum(1).unsqueeze(1)

                loss_st = LossFunction.mse(
                    X,
                    dec_gene_averaged,
                    reduction = 'none'
                )

            if st_loss_weight is not None:
                loss_st = (loss_st * st_loss_weight).mean()
            else:
                loss_st = loss_st.sum()

        if optimizer_idx == 0:
            aeloss, log_dict_ae = self.first_stage_model.loss(
                input_image, 
                dec, 
                posterior, 
                optimizer_idx, 
                self.first_stage_model.global_step,
                last_layer=self.first_stage_model.get_last_layer(), 
                split="train"
            )
            return {
                'posterior': post_src,
                'dec': dec,
                'dec_pc': dec_pc,
                'dec_gene': dec_gene,
                'dec_latent': dec_latent,
                'loss_st': loss_st,
                'loss_latent': loss_latent,
                'loss_ae': aeloss,
                'loss_disc': torch.tensor(0., device=self.device),
                'I_for_loss_image_indices': I_for_loss_image_indices,
                'I_for_loss_image_mask': I_for_loss_image_mask,
                'I_for_loss_spatial_coords': I_for_loss_spatial_coords,
                'I_for_loss': I_for_loss,
                'D_for_loss': D_for_loss,
                'mask': mask,
                'original_mask': original_mask,
            }
        else:
            discloss, log_dict_disc = self.first_stage_model.loss(
                input_image, 
                dec, 
                posterior, 
                optimizer_idx, 
                self.first_stage_model.global_step,
                last_layer=self.first_stage_model.get_last_layer(), 
                split="train"
            )
            return {
                'posterior': post_src,
                'dec': dec,
                'dec_pc': dec_pc,
                'dec_gene': dec_gene,
                'dec_latent': dec_latent,
                'loss_st': loss_st,
                'loss_latent': loss_latent,
                'loss_ae': torch.tensor(0., device=self.device),
                'loss_disc': discloss,
                'I_for_loss_image_indices': I_for_loss_image_indices,
                'I_for_loss_image_mask': I_for_loss_image_mask,
                'I_for_loss_spatial_coords': I_for_loss_spatial_coords,
                'I_for_loss': I_for_loss,
                'D_for_loss': D_for_loss,
                'mask': mask,
                'original_mask': original_mask,
            }

    def forward_second_stage(
        self,
        input_image: torch.Tensor,
        spatial_coord: torch.Tensor,
        latent_embedding: torch.Tensor,
        latent_embedding_original: torch.Tensor,
        X: torch.Tensor,
        st_loss_weight: torch.Tensor = None,
        n_neighbor: int = 1,
        upscaled_diameter: float = 40,
        k: str = None,
        c: str = None,
    ):
        first_stage_output = self.get_first_stage_output(
            input_image,
            spatial_coord,
            latent_embedding,
            latent_embedding_original,
            X,
            st_loss_weight,
            n_neighbor,
            upscaled_diameter,
            k,
        )
        z = first_stage_output['z']

        loss = self.second_stage_model(z, c)

        return loss 

    @torch.no_grad()
    def get_first_stage_output(
        self,
        input_image: torch.Tensor,
        spatial_coord: torch.Tensor,
        latent_embedding: torch.Tensor,
        latent_embedding_original: torch.Tensor,
        X: torch.Tensor,
        st_loss_weight: torch.Tensor = None,
        n_neighbor: int = 1,
        upscaled_diameter: float = 40,
        k: str = None,
        batch_indices = None
    ):
        with torch.no_grad():
            first_stage_output = self.forward_first_stage(
                input_image,
                spatial_coord,
                latent_embedding,
                latent_embedding_original,
                X,
                st_loss_weight,
                n_neighbor,
                upscaled_diameter,
                k,
                batch_indices
            )

        return dict(
            z = first_stage_output['posterior'],
            xrec = first_stage_output['dec'],
            xrec_gene = first_stage_output['dec_gene'],
        )
