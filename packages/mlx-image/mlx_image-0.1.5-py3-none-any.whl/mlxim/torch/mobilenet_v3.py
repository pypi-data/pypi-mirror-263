from typing import Dict

import mlx.core as mx
import torch

from ..model import create_model, get_weights
from .utils import pth_to_mlx_weights


def mobilenetv3_to_mlx(model_name: str, pth_ckpt_path: str, verbose: bool = False) -> Dict[str, mx.array]:
    """Convert a PyTorch ResNet18 model to a MLX weights dict (key, mx.array).

    Args:
        pth_state_dict (str): path to ResNet18 PyTorch state dict
        verbose (bool, optional): verbose mode. Defaults to False.

    Returns:
        Dict[str, mx.array]: MLX weights dict (key, mx.array)
    """

    # it still has the keys of the original model
    torch_state_dict = pth_to_mlx_weights(pth_ckpt_path)
    model = create_model(model_name, weights=False)
    # getting mlx model keys
    mlx_mobilenetv3_weights = get_weights(model)
    mlx_weights = {}  # type: ignore
    for k, v in torch_state_dict.items():
        if "num_batches_tracked" in k:
            continue
        if "features." in k and "fc" not in k:
            k_split = k.split(".")
            if len(k_split) == 4:
                mlx_k = f"features.layers.{k_split[1]}.layers.{k_split[2]}.{k_split[3]}"
            elif len(k_split) > 5:
                mlx_k = (
                    f"features.layers.{k_split[1]}.{k_split[2]}.layers.{k_split[3]}.layers.{k_split[4]}.{k_split[5]}"
                )

        elif "fc" in k:  #
            k_split = k.split(".")
            mlx_k = f"features.layers.{k_split[1]}.{k_split[2]}.layers.{k_split[3]}.{k_split[4]}.{k_split[5]}"
        elif "classifier" in k:
            k_split = k.split(".")
            mlx_k = f"classifier.layers.{k_split[1]}.{k_split[2]}"

        if mlx_k not in mlx_mobilenetv3_weights.items():
            print(f"[ERROR] {mlx_k} not found in mlx_mobilenetv3_weights")
        else:
            mlx_weights[mlx_k]
            if v.shape == 4:
                if v.transpose(0, 2, 3, 1).shape == v.shape:
                    mlx_weights[mlx_k] = v.transpose(0, 2, 3, 1)
            else:
                mlx_weights[mlx_k] = v

    return mlx_weights
