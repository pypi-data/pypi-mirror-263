"""Pure PyTorch implementations of various functions"""
import torch
import torch.nn.functional as F
import struct
from jaxtyping import Float
from torch import Tensor

def spherical_projection(
    tile_bounds,
    block,
    img_size,
    gaussian_ids_sorted,
    tile_bins,
    xys,
    conics,
    colors,
    opacities,
    background,
):
    out_img = None
    final_Ts = None
    final_idx = None
    return out_img, final_Ts, final_idx
