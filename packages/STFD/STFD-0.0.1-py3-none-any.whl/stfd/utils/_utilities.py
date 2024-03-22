import os
import argparse
import sys
import numpy as np
import random
import pandas as pd
from typing import Iterable
import torch
import torch.nn.functional as F
from collections import Counter
import scanpy as sc
import numba
from umap.distances import euclidean
import scipy 

import warnings
import tqdm

from scatlasvae.utils._parallelizer import Parallelizer

from ._logger import Colors
from ._decorators import deprecated


def FLATTEN(x): 
    return [i for s in x for i in s]

def dict_update_and_return(d1, d2):
    d1.update(d2)
    return d1

def _nearest_neighbor_eucliean_distances(
    X,
    queue
):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)    
        out = []
        for d in X:
            x1, x2 = d
            if queue is not None:
                queue.put(None)
            ret = []
            for x in x2:
                ret.append(euclidean(x1, x))
            out.append(np.array(ret, dtype=np.float32))
        return np.vstack(out)

def nearest_neighbor_eucliean_distances_parallel(
    X: np.ndarray, 
    neigh_indices: np.ndarray,
    sel_indices: np.ndarray = None,
    n_jobs: int = os.cpu_count()
):
    data = np.array(list(zip(X, X[neigh_indices])))
    if sel_indices is not None:
        data = data[sel_indices]
    p = Parallelizer(n_jobs=n_jobs)
    result = p.parallelize(map_func=_nearest_neighbor_eucliean_distances, map_data=data, reduce_func=FLATTEN)()
    return np.vstack(result)

def nearest_neighbor_eucliean_distances(
    X: np.ndarray, 
    neigh_indices: np.ndarray,
    sel_indices: np.ndarray = None
):
    np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)    
    return nearest_neighbor_eucliean_distances_parallel(
        X, 
        neigh_indices, 
        sel_indices
    )


def multi_values_dict(keys, values):
    ret = {}
    for k,v in zip(keys, values):
        if k not in ret.keys():
            ret[k] = [v]
        else:
            ret[k].append(v)
    return ret

def mafft_alignment(sequences):
    result = []
    import sys
    from Bio.Align.Applications import MafftCommandline
    import tempfile
    with tempfile.NamedTemporaryFile() as temp:
        temp.write('\n'.join(list(map(lambda x: '>seq{}\n'.format(x[0]) + x[1], enumerate(sequences)))).encode())
        temp.seek(0)
        mafft_cline = MafftCommandline(input=temp.name)
        stdout,stderr=mafft_cline()
    for i,j in enumerate(stdout.split("\n")):
        if i % 2 != 0:
            result.append(j.replace("-","."))
    return result

def seqs2mat(sequences, char_set = list('ACDEFGHIKLMNPQRSTVWY'), gap_character = '.'):
    mat = np.zeros((len(sequences[0]), len(char_set)))
    for i in range(len(sequences[0])):
        count = Counter(list(map(lambda x:x[i], sequences)))
        for k,v in count.items():
            if k != gap_character:
                mat[i][char_set.index(k)] = v
    mat = pd.DataFrame(mat, columns = char_set)
    return mat

@deprecated(ymd = (2023, 12, 31), optional_message = "Use random_subset_by_key_fast instead for better performance")
def random_subset_by_key(adata, key, n):
    from collections import Counter
    counts = {k:v/len(adata) for k,v in Counter(adata.obs[key]).items()}
    ns = [(k,int(v*n)) for k,v in counts.items()]
    adatas = []
    for k,v in ns:
        view = adata[adata.obs[key] == k]
        view_subset = view[np.random.choice(list(range(len(view))), v, replace=False)]
        if view_subset.shape[0] > 0:
            adatas.append(view_subset)
        else:
            adatas.append(
                view[:1]
            )
    return sc.concat(adatas)

def random_subset_by_key_fast(adata, key, n):
    from collections import Counter
    counts = {k:v/len(adata) for k,v in Counter(adata.obs[key]).items()}
    ns = [(k,int(v*n)) for k,v in counts.items()]
    all_indices = []
    for k,v in ns:
        indices = np.argwhere(np.array(adata.obs[key] == k)).flatten()
        if len(indices) > 0:
            indices = np.random.choice(indices, v, replace=False)
            all_indices.append(indices)
    all_indices = np.hstack(all_indices)
    return adata[all_indices]

def exists(x):
    return x != None

def sliceSimutaneuously(a, index):
    return pd.DataFrame(a).iloc[index,index].to_numpy()

def mask_split(tensor, indices):
    sorter = torch.argsort(indices)
    _, counts = torch.unique(indices, return_counts=True)
    return torch.split(tensor[sorter], counts.tolist())


def print_version():
    print(Colors.YELLOW)
    print('Python VERSION:{}\n'.format(Colors.NC), sys.version)
    print(Colors.YELLOW)
    print('PyTorch VERSION:{}\n'.format(Colors.NC), torch.__version__)
    print(Colors.YELLOW)
    print('CUDA VERSION{}\n'.format(Colors.NC))
    from subprocess import call
    try: call(["nvcc", "--version"])
    except: pass
    print(Colors.YELLOW)
    print('CUDNN VERSION:{}\n'.format(Colors.NC), torch.backends.cudnn.version())
    print(Colors.YELLOW)
    print('Number CUDA Devices:{}\n'.format(Colors.NC), torch.cuda.device_count())
    try:
        print('Devices             ')
        call(["nvidia-smi", "--format=csv", "--query-gpu=index,name,driver_version,memory.total,memory.used,memory.free"])
    except FileNotFoundError:
        # There is no nvidia-smi in this machine
        pass
    if torch.cuda.is_available():
        print('Active CUDA Device: GPU', torch.cuda.current_device())
        print ('Available devices     ', torch.cuda.device_count())
        print ('Current cuda device   ', torch.cuda.current_device())
    else:
        # cuda not available
        pass

def read_tsv(path, header:bool = True, skip_first_line: bool = False, return_pandas: bool = True):
    result = []
    if os.path.exists(path):
        f = open(path)
        if skip_first_line:
            line = f.readline()
        header_length = None
        if header:
            header = f.readline().strip().split('\t')
            header_length = len(header)

        while 1:
            line = f.readline()
            if not line:
                break
            line = line.strip().split('\t')
            if not header_length:
                header_length = len(line)
            result.append(line[:header_length])
        f.close()
        if return_pandas:
            if header:
                return pd.DataFrame(result, columns = header)
            else:
                return pd.DataFrame(result)
        else:
            return result
    else:
        it = iter(path.split('\n'))
        if skip_first_line:
            line = next(it)
        header_length = None
        if header:
            header = next(it).strip().split('\t')
            header_length = len(header)

        while 1:
            try:
                line = next(it)
                if not line:
                    break
                line = line.strip().split('\t')
                if not header_length:
                    header_length = len(line)
                result.append(line[:header_length])
            except:
                break 
        if return_pandas:
            if header:
                return pd.DataFrame(list(filter(lambda x: len(x) == 125, result)), columns = header)
            else:
                return pd.DataFrame(list(filter(lambda x: len(x) == 125, result)))
        else:
            return result


def default_aggrf(i):
    if len(np.unique(i)) == 1:
        return i[0]
    if len(i) == 2:
        return "Ambiguous"
    else:
        c = Counter(i)
        return sorted(c.items(), key=lambda x: -x[1])[0][0]
            
def default_pure_criteria(x,y):
    return (Counter(x).most_common()[0][1] / len(x) > 0.8) and Counter(x).most_common()[0][0] == y


def readMM(path):
    f = open(path)
    while 1:
        line = f.readline()
        if not line.startswith("%"):
            break 

    n,m,total=line.strip().split(" ")
    n = int(n)
    m = int(m)
    total = int(total)
    z = np.zeros((n,m),dtype=np.int32)
    pbar = tqdm.tqdm(total=total)
    while 1:
        line = f.readline()
        if not line:
            break
        a,b,c = line.split(' ')
        a = int(a)
        b = int(b)
        c = int(c)
        z[a-1,b-1]=c
        pbar.update(1)
    pbar.close()
    return scipy.sparse.csr_matrix(z.T)

def iter_spmatrix(matrix):
    """ Iterator for iterating the elements in a ``scipy.sparse.*_matrix`` 

    This will always return:
    >>> (row, column, matrix-element)

    Currently this can iterate `coo`, `csc`, `lil` and `csr`, others may easily be added.

    Parameters
    ----------
    matrix : ``scipy.sparse.sp_matrix``
      the sparse matrix to iterate non-zero elements
    """
    from scipy.sparse import isspmatrix_coo, isspmatrix_csc, isspmatrix_csr, isspmatrix_lil
    if isspmatrix_coo(matrix):
        for r, c, m in zip(matrix.row, matrix.col, matrix.data):
            yield r, c, m

    elif isspmatrix_csc(matrix):
        for c in range(matrix.shape[1]):
            for ind in range(matrix.indptr[c], matrix.indptr[c+1]):
                yield matrix.indices[ind], c, matrix.data[ind]

    elif isspmatrix_csr(matrix):
        for r in range(matrix.shape[0]):
            for ind in range(matrix.indptr[r], matrix.indptr[r+1]):
                yield r, matrix.indices[ind], matrix.data[ind]

    elif isspmatrix_lil(matrix):
        for r in range(matrix.shape[0]):
            for c, d in zip(matrix.rows[r], matrix.data[r]):
                yield r, c, d

    else:
        raise NotImplementedError("The iterator for this sparse matrix has not been implemented")

def writeMM(mat, path):
    with open(path, 'w') as f:
        f.write("%%MatrixMarket matrix coordinate integer general\n")
        f.write("% Generated by Snowxue\n")
        f.write("% \n")
        f.write(str(mat.shape[1]) + " " + str(mat.shape[0]) + " " + str(int(mat.nnz)) + "\n")
        pbar = tqdm.tqdm(total=mat.nnz,bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}',desc="writing matrix")
        for i,j,v in iter_spmatrix(mat):
            f.write(str(j+1) + " " + str(i+1) + " " + str(v) + "\n")
            pbar.update(1)
        pbar.close()
