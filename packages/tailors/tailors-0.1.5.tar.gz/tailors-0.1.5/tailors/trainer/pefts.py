# -*- coding: utf-8 -*-
import hao
from hao.namespaces import attr, from_args
from peft import (
    LoraConfig,
    PeftConfig,
    PeftType,
    PrefixTuningConfig,
    PromptEncoderConfig,
    PromptTuningConfig,
    TaskType,
    get_peft_config,
    get_peft_model,
)

LOGGER = hao.logs.get_logger(__name__)


@from_args(prefix='lora')
class LoraConf:
    inference_mode: bool = attr(bool, default=False)
    r: int = attr(int, default=8)
    alpha: int = attr(int, default=16)
    dropout: int = attr(float, default=0.1)
    modules_to_save: list = attr(list)


@from_args(prefix='prefix_tuning')
class PrefixTuningConf:
    inference_mode: bool = attr(bool, default=False)
    num_virtual_tokens: int = attr(int, default=20)
    token_dim: int = attr(int)
    encoder_hidden_size: int = attr(int)
    prefix_projection: list = attr(list)


@from_args(prefix='prompt_tuning')
class PromptTuningConf:
    inference_mode: bool = attr(bool, default=False)
    num_virtual_tokens: int = attr(int, default=10)
    prompt_tuning_init_text: int = attr(int)


@from_args(prefix='p_tuning')
class PTuningConf:
    inference_mode: bool = attr(bool, default=False)
    num_virtual_tokens: int = attr(int, default=20)
    encoder_hidden_size: int = attr(int, default=128)


def get_lora_config(task_type: str):
    conf = LoraConf()
    LOGGER.info(conf)
    return LoraConfig(
        task_type=task_type,
        inference_mode=conf.inference_mode,
        r=conf.r,
        lora_alpha=conf.alpha,
        lora_dropout=conf.dropout,
        modules_to_save=conf.modules_to_save,
    )


def get_prefix_tuning_config(task_type: str):
    conf = PrefixTuningConf()
    LOGGER.info(conf)
    return PrefixTuningConfig(
        task_type=task_type,
        inference_mode=conf.inference_mode,
        num_virtual_tokens=conf.num_virtual_tokens,
        token_dim=conf.token_dim,
        encoder_hidden_size=conf.encoder_hidden_size,
        prefix_projection=conf.prefix_projection,
    )


def get_prompt_tuning_config(task_type: str):
    conf = PromptTuningConf()
    LOGGER.info(conf)
    return PromptTuningConfig(
        task_type=task_type,
        inference_mode=conf.inference_mode,
        num_virtual_tokens=conf.num_virtual_tokens,
        prompt_tuning_init_text=conf.prompt_tuning_init_text,
    )


def get_p_tuning_config(task_type: str):
    conf = PTuningConf()
    LOGGER.info(conf)
    return PromptEncoderConfig(
        task_type=task_type,
        inference_mode=conf.inference_mode,
        num_virtual_tokens=conf.num_virtual_tokens,
        encoder_hidden_size=conf.encoder_hidden_size,
    )


_PEFT_CONFIGURATERS = {
    PeftType.LORA: get_lora_config,
    PeftType.PREFIX_TUNING: get_prefix_tuning_config,
    PeftType.PROMPT_TUNING: get_prompt_tuning_config,
    PeftType.P_TUNING: get_p_tuning_config,
}


def peftify(model, peft_type: str, task_type: str):
    if peft_type is None:
        return model
    assert task_type is not None, f"[peft] {peft_type}, missing [peft_task_type], options: {[t.name for t in TaskType]}"
    peft_type = PeftType[peft_type.upper()]
    peft_config = _PEFT_CONFIGURATERS.get(peft_type)(task_type.upper())
    model = get_peft_model(model, peft_config)
    model.print_trainable_parameters()
    return model
