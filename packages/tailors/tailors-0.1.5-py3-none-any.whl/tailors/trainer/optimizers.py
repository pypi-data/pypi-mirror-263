# -*- coding: utf-8 -*-
import hao
from hao.namespaces import attr, from_args
from torch.optim import SGD, Adadelta, Adam, AdamW
from torch_optimizer import SGDW, Lamb, RAdam

from tailors.exceptions import TailorsError

LOGGER = hao.logs.get_logger('trainer.optimizers')


@from_args
class AdadeltaConf:
    rho: float = attr(float)
    eps: float = attr(float, default=1e-8)
    lr: float = attr(float)
    weight_decay: float = attr(float)
    foreach: bool = attr(bool)
    maximize: bool = attr(bool)


@from_args
class AdamConf:
    lr: float = attr(float)
    weight_decay: float = attr(float, default=0)
    amsgrad: bool = attr(bool, default=True)


@from_args
class AdamWConf:
    lr: float = attr(float)
    betas: tuple[float, float] = attr(float, default=(0.9, 0.999))
    eps: float = attr(float, default=1e-8)
    weight_decay: float = attr(float, default=1e-2)
    amsgrad: bool = attr(bool, default=False)
    no_deprecation_warning: bool = attr(bool)


@from_args
class LambConf:
    lr: float = attr(float)
    betas: tuple[float, float] = attr(float)
    eps: float = attr(float)
    weight_decay: float = attr(float)
    clamp_value: int = attr(float)
    adam: bool = attr(bool)
    debias: bool = attr(bool)


@from_args
class RAdamConf:
    lr: float = attr(float)
    betas: tuple[float, float] = attr(float)
    eps: float = attr(float)
    weight_decay: float = attr(float)


@from_args
class SGDWConf:
    lr: float = attr(float, required=True)
    momentum: float = attr(float, default=0)
    weight_decay: float = attr(float, default=0)
    dampening: float = attr(float, default=0)
    nesterov: bool = attr(bool, default=False)


@from_args
class SGDConf:
    lr: float = attr(float, required=True)
    momentum: float = attr(float, default=0)
    weight_decay: float = attr(float, default=0)
    dampening: float = attr(float, default=0)
    nesterov: bool = attr(bool, default=False)
    maximize: bool = attr(bool, default=False)
    foreach: bool = attr(bool)


OPTIMIZERS = {
    'adam': (Adam, AdamConf),
    'adamw': (AdamW, AdamWConf),
    'adadelta': (Adadelta, AdadeltaConf),
    'lamb': (Lamb, LambConf),
    'radam': (RAdam, RAdamConf),
    'sgdw': (SGDW, SGDWConf),
    'sgd': (SGD, SGDConf),
}


def get(optimizer: str, model_parameters: list):
    entry = OPTIMIZERS.get(optimizer)
    if entry is None:
        raise TailorsError(f"Unsupported optimizer: {optimizer}")
    Optimizer, Conf = entry
    optimizer_conf = Conf()
    LOGGER.info(f'[optimizer] {Optimizer.__name__}')
    LOGGER.info(optimizer_conf)

    params = hao.dicts.remove_fields({
        'params': model_parameters,
        **optimizer_conf.to_dict()
    }, remove_empty=False)
    return hao.invoker.invoke(Optimizer, **params), optimizer_conf
