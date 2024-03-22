# -*- coding: utf-8 -*-
import importlib
import inspect
import os
from abc import ABC, abstractmethod
from collections.abc import Iterator

import hao
import torch
import torch.nn as nn
from hao.namespaces import attr, from_args
from hao.stopwatch import Stopwatch
from peft import get_peft_config, get_peft_model, set_peft_model_state_dict
from torch.nn import DataParallel
from torch.nn.parallel import DistributedDataParallel
from transformers import PreTrainedTokenizerFast

import tailors
from tailors.domains import Factor, Tags
from tailors.exceptions import TailorsError
from tailors.utils.collates import tailors_collate
from tailors.utils.progresses import progressive

LOGGER = hao.logs.get_logger(__name__)


@from_args
class TailorsConf:
    exp: str = attr(str, help='experiment name')
    meta: dict = None


class TailorsTextConf(TailorsConf):
    seq_len: int = attr(int, default=192)
    freeze_embedding: bool = attr(bool, default=False)


class TailorsIO(ABC):
    def __init__(self, model_conf: TailorsConf, **kwargs) -> None:
        self.model_conf = model_conf
        self.init()

    def init(self):
        pass

    def from_files(self, files) -> Iterator:
        for file in files:
            yield from self.from_file(file)

    def from_file(self, file) -> Iterator:
        filepath = hao.paths.get(file)
        if not os.path.exists(filepath):
            raise TailorsError(f"[dataset] file not found, file: {file}")

        desc = f"[dataset] {os.path.basename(filepath): <20}"
        if (examples := self.from_lines(open(filepath, 'r').read())) is not None:
            with progressive(examples, desc=desc, loggers=[LOGGER]) as entries:
                for data in entries:
                    yield data

        else:
            n_lines = hao.files.count_lines(filepath)
            with open(filepath, "r") as f:
                with progressive(f, total=n_lines, desc=desc, loggers=[LOGGER]) as entries:
                    for line in entries:
                        line = hao.strings.strip_to_none(line)
                        if line is None:
                            continue
                        data = self.from_line(line)
                        if isinstance(data, list):
                            yield from data
                        else:
                            yield data

    def from_lines(self, text: str):
        return None

    def from_line(self, line: str):
        raise NotImplementedError()

    def transform_example(self, item, **kwargs):
        return item

    @abstractmethod
    def for_inference(self, paths: list[str], bz: int = 32, *args, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    def post_inference(self, *args, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def collate(batch):
        try:
            return tailors_collate(batch)
        except RuntimeError as e:
            LOGGER.error(f"[collate] {str(e)}")
            raise e


class TailorsTextIO(TailorsIO, ABC):
    def __init__(self, model_conf: TailorsConf, tokenizer: PreTrainedTokenizerFast) -> None:
        self.model_conf = model_conf
        self.tokenizer = tokenizer
        self.tags: Tags = self.build_tags()
        self.empty_sample = self.build_empty_sample()
        self.init()
        self.empty_input = self.build_empty_input()

    @abstractmethod
    def build_tags(self) -> Tags:
        raise NotImplementedError()

    def build_empty_sample(self) -> Tags:
        return self.encode('', self.tokenizer, self.model_conf.seq_len)

    def init(self):
        pass

    @abstractmethod
    def build_empty_input(self):
        raise NotImplementedError()

    @staticmethod
    def encode(text_or_tokens: str | list[str],
               tokenizer: PreTrainedTokenizerFast,
               seq_len: int,
               add_special_tokens=True,
               padding: bool | str = 'max_length',
               truncation: bool | str = True,
               return_offsets_mapping: bool = True,
               return_tensors: str = 'pt'):
        is_text = isinstance(text_or_tokens, str)
        if is_text:
            encoder = tokenizer.encode_plus
        else:
            encoder = tokenizer.prepare_for_model
            if text_or_tokens and isinstance(text_or_tokens[0], str):
                text_or_tokens = tokenizer.convert_tokens_to_ids(text_or_tokens)
        encoded = encoder(
            text_or_tokens,
            add_special_tokens=add_special_tokens,
            max_length=seq_len,
            padding=padding,
            truncation=truncation,
            return_attention_mask=True,
            return_token_type_ids=True,
            return_offsets_mapping=return_offsets_mapping,
            return_tensors=return_tensors,
        )
        input_ids = encoded.get("input_ids")
        attention_mask = encoded.get("attention_mask")
        token_type_ids = encoded.get("token_type_ids")

        if return_tensors:
            input_ids = input_ids.squeeze()
            attention_mask = attention_mask.squeeze()
            token_type_ids = token_type_ids.squeeze()

        if is_text and return_offsets_mapping:
            offset_mapping = encoded.get("offset_mapping")
            if return_tensors:
                offset_mapping = offset_mapping[0].tolist() if offset_mapping is not None else None
            return input_ids, attention_mask, token_type_ids, offset_mapping
        else:
            return input_ids, attention_mask, token_type_ids


class Tailors(nn.Module, ABC):

    def __init__(self, model_conf: TailorsConf):
        super().__init__()
        self.device = None
        self.model_conf = model_conf

        self.io: TailorsIO = self.get_io()

    def freeze(self):
        tailors.freeze(self)
        self.eval()

    def unfreeze(self) -> None:
        tailors.unfreeze(self)
        self.train()

    def use_device(self, device):
        if device:
            self.to(device)
            self.device = device
        return self

    def on_save_checkpoint(self):
        pass

    def get_io(self):
        class_name = f"{self.__class__.__name__}IO"
        module_name = self.__class__.__module__
        try:
            module = importlib.import_module(module_name)
            io_class = getattr(module, class_name)
        except AttributeError:
            raise TailorsError(f"[io] expecting io class: `{module_name}.{class_name}`")
        except Exception as e:
            raise TailorsError(f"[io] failed to init io class: `{module_name}.{class_name}`", e)
        if (tokenizer := getattr(self, 'build_tokenizer', None)) is not None:
            tokenizer = tokenizer()
            return io_class(self.model_conf, tokenizer)
        else:
            return io_class(self.model_conf)

    @abstractmethod
    def train_step(self, *args, **kwargs):
        """calculate loss and metrics"""
        raise NotImplementedError()

    def val_step(self, *args, **kwargs):
        return self.train_step(*args, **kwargs)

    @abstractmethod
    def compute_metrics(self, *args, **kwargs):
        # classification_metrics.calculate(targets[0], outs[0], self.model.io.tags.id2tag)
        raise NotImplementedError()

    def lr_factors(self) -> dict[str, Factor]:
        return {
            'embedding': Factor(factor=0.1, max_val=1e-4),
            'crf': Factor(factor=1000, max_val=5e-2),
        }

    @classmethod
    def from_pretrained(cls, path_or_key: str, use_gpu = True):
        if inspect.isabstract(cls):
            raise TailorsError(f"Not supported call from abstract class: {cls.__name__}")

        if ".local" in path_or_key:  # do not use SEQUE_CONFIG, since it's not called in this lib project
            hao.oss.init(path_or_key[: path_or_key.rfind(".")])
            model_path = hao.config.get(path_or_key)
        else:
            model_path = path_or_key
        fullpath = hao.paths.get(model_path)

        if model_path is None or not os.path.isfile(fullpath):
            raise TailorsError(f"model not found: {model_path}")

        LOGGER.info(f"[{cls.__name__}] loading from: {model_path}")
        sw = Stopwatch()
        state_dicts = torch.load(fullpath)
        state_dict = state_dicts.get('state_dict')
        model = cls(state_dicts.get('model_conf'))
        if (peft_config := state_dicts.get('peft_config')) is None:
            model.load_state_dict(state_dict)
        else:
            model = get_peft_model(model, get_peft_config(peft_config))
            set_peft_model_state_dict(model, state_dict)

        model.freeze()
        LOGGER.info(f"[{cls.__name__}] loaded, took: {sw.took()}")

        if use_gpu:
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            model.use_device(device)
        return model

    @abstractmethod
    def predict(self, *args, **kwargs):
        raise NotImplementedError()

    def export_to_model(self, output_path):
        is_dp_module = isinstance(self, (DistributedDataParallel, DataParallel))
        model = self.module if is_dp_module else self

        model.on_save_checkpoint()
        checkpoint = {'state_dict': model.state_dict(), 'model_conf': model.model_conf}
        hao.paths.make_parent_dirs(output_path)
        torch.save(checkpoint, output_path)

    def export_to_onnx(self, output_path):
        input_names = ['input_ids', 'attention_mask', 'token_type_id']
        output_names = ['tag', 'score']
        dynamic_axes = {
            'input_ids': {0: 'batch_size', 1: 'sequence'},  # 第0维是batch dimension
            'attention_mask': {0: 'batch_size', 1: 'sequence'},  # 第0维是batch dimension
            'token_type_id': {0: 'batch_size', 1: 'sequence'},  # 第0维是batch dimension
            'tag': {0: 'batch_size', 1: 'sequence'},
            'score': {0: 'batch_size', 1: 'sequence'},
        }
        torch.onnx.export(
            self,
            self.io.empty_input,
            output_path,
            verbose=False,
            input_names=input_names,
            output_names=output_names,
            dynamic_axes=dynamic_axes,
            export_params=True,
            opset_version=13,
            do_constant_folding=True,
        )
        LOGGER.info(f'saved onnx to: {output_path}')

    @classmethod
    def to_model(cls, model_path, output_path=None):
        if model_path is None:
            raise TailorsError('empty output_path')
        model_path = hao.paths.get_path(model_path)
        if not os.path.exists(model_path):
            raise TailorsError(f'model_path not exist: {model_path}')

        model = cls.from_pretrained(model_path)
        if output_path is None:
            path_base, _ = os.path.splitext(os.path.basename(model_path))
            output_path = hao.paths.get_path('data', 'model', f"{path_base}.bin")
        hao.paths.make_parent_dirs(output_path)
        model.export_to_model(output_path)
        return output_path

    @classmethod
    def to_onnx(cls, model_path, output_path=None):
        if model_path is None:
            raise TailorsError('empty output_path')
        model_path = hao.paths.get_path(model_path)
        if not os.path.exists(model_path):
            raise TailorsError(f'model_path not exist: {model_path}')

        model = cls.from_pretrained(model_path)
        if output_path is None:
            path_base, _ = os.path.splitext(os.path.basename(model_path))
            output_path = hao.paths.get_path('data', 'model', f"{path_base}.onnx")
        hao.paths.make_parent_dirs(output_path)
        model.export_to_onnx(output_path)
        return output_path
