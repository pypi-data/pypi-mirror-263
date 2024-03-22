# -*- coding: utf-8 -*-
import torch.nn as nn
from torch.nn.parameter import UninitializedParameter


def model_size(model: nn.Module, precision: int = 32, digits=2) -> str:
    precision_mb = (precision / 8.0) * 1e-6
    total_params = sum(p.numel() for p in model.parameters() if not isinstance(p, UninitializedParameter))
    return f"{(total_params * precision_mb):.{digits}f} MB"
