import scanpy as sc 
import datasets
import torch 
import torch.nn.functional as F
import numpy as np
import pandas as pd
import math 
import tabulate 
from typing import Iterable

def get_k_elements(arr: Iterable, k:int):
    return list(map(lambda x: x[k], arr))

def get_last_k_elements(arr: Iterable, k:int):
    return list(map(lambda x: x[k:], arr))

def get_elements(arr: Iterable, a:int, b:int):
    return list(map(lambda x: x[a:a+b], arr))

def one_hot_(labels, return_dict = False):
    n_labels_ = np.unique(labels)
    n_labels = dict(zip(n_labels_, range(len(n_labels_))))
    if return_dict:
        return {"one_hot": F.one_hot( torch.tensor(list(map(lambda x: n_labels[x], labels)))), "labels": n_labels}
    return F.one_hot( torch.tensor(list(map(lambda x: n_labels[x], labels))))

def one_hot(index: torch.Tensor, n_cat: int) -> torch.Tensor:
    """One hot a tensor of categories."""
    onehot = torch.zeros(index.size(0), n_cat, device=index.device)
    onehot.scatter_(1, index.type(torch.long), 1)
    return onehot.type(torch.float32)

    

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def print_gpu_mem(i):
    try:
        import nvidia_smi
    except:
        print("install nvidia_smi for automatically select cuda device by memory usage.")
        return np.nan, np.nan, np.nan
    nvidia_smi.nvmlInit()
    handle = nvidia_smi.nvmlDeviceGetHandleByIndex(i)
    info = nvidia_smi.nvmlDeviceGetMemoryInfo(handle)
    return convert_size(info.used), convert_size(info.total), '%.2f' % ((info.used / info.total) * 100) + ' %'

def print_cpu_mem():
    import os
    import psutil
    process = psutil.Process(os.getpid())
    return (
        convert_size(process.memory_info().rss), 
        convert_size(psutil.virtual_memory().total), 
        '%.2f' % (process.memory_info().rss / psutil.virtual_memory().total * 100) + ' %'
    )

def get_default_device():
    devices = {}
    n_cuda_device = torch.cuda.device_count()
    if n_cuda_device > 0:
        for i in range(n_cuda_device):
            used, total, perc = print_gpu_mem(i)
            devices['cuda:' + str(i)] = {
                'name': torch.cuda.get_device_name(i),
                'used': used,
                'total': total,
                'used %': perc
            }
    else:
        return 'cpu'
    selected_device = sorted(devices.items(), key=lambda x: float(x[1]['used %'].split(" ")[0]))[0][0]
    for k,v in devices.items():
        if k == selected_device:
            v['selected'] = '*'
        else:
            v['selected'] = ' '
    print(tabulate.tabulate(pd.DataFrame(devices).T))
    return selected_device

#https://github.com/Bjarten/early-stopping-pytorch/blob/master/pytorchtools.py
class EarlyStopping:
    """
    Early stops the training if validation loss doesn't improve after a given patience.
    >>> early_stopping = EarlyStopping(patience=patience, verbose=True)
    >>> early_stopping(valid_loss, model)
    """
    def __init__(self, patience=7, verbose=False, delta=0, path='checkpoint.pt', trace_func=print):
        """
        Args:
            patience (int): How long to wait after last time validation loss improved.
                            Default: 7
            verbose (bool): If True, prints a message for each validation loss improvement. 
                            Default: False
            delta (float): Minimum change in the monitored quantity to qualify as an improvement.
                            Default: 0
            path (str): Path for the checkpoint to be saved to.
                            Default: 'checkpoint.pt'
            trace_func (function): trace print function.
                            Default: print            
        """
        self.patience = patience
        self.verbose = verbose
        self.counter = 0
        self.best_score = None
        self.early_stop = False
        self.val_loss_min = np.Inf
        self.delta = delta
        self.path = path
        self.trace_func = trace_func
    def __call__(self, val_loss, model):

        score = -val_loss

        if self.best_score is None:
            self.best_score = score
            self.save_checkpoint(val_loss, model)
        elif score < self.best_score + self.delta:
            self.counter += 1
            self.trace_func(f'EarlyStopping counter: {self.counter} out of {self.patience}')
            if self.counter >= self.patience:
                self.early_stop = True
        else:
            self.best_score = score
            self.save_checkpoint(val_loss, model)
            self.counter = 0

    def save_checkpoint(self, val_loss, model):
        '''Saves model when validation loss decrease.'''
        if self.verbose:
            self.trace_func(f'Validation loss decreased ({self.val_loss_min:.6f} --> {val_loss:.6f}).  Saving model ...')
        torch.save(model.state_dict(), self.path)
        self.val_loss_min = val_loss
