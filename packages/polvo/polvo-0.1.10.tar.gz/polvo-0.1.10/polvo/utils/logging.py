# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/01b_utils.logging.ipynb.

# %% auto 0
__all__ = ['pbar']

# %% ../../nbs/01b_utils.logging.ipynb 2
from time import sleep
from tqdm.autonotebook import tqdm

# %% ../../nbs/01b_utils.logging.ipynb 3
def pbar(*args, show=True, total=None, **kwargs): 
    return tqdm(*args, total=total, **kwargs) if show else iter
