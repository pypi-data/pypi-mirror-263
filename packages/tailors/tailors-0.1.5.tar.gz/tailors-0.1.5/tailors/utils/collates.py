from collections.abc import Mapping, Sequence

import numpy as np
import regex
import torch

P_NP_STR = regex.compile(r'[SaUO]')


def tailors_collate(batch):
    if batch is None:
        return batch
    elem = batch[0]
    elem_type = type(elem)

    if isinstance(elem, np.ndarray):
        # array of string classes and object
        if P_NP_STR.search(elem[0].dtype.str) is not None:
            return elem
        # return torch.as_tensor(batch)
        return np.stack(batch, 0)

    if isinstance(elem, torch.Tensor):
        out = None
        if torch.utils.data.get_worker_info() is not None:
            # If we're in a background process, concatenate directly into a
            # shared memory tensor to avoid an extra copy
            numel = sum(x.numel() for x in batch)
            storage = elem.storage()._new_shared(numel, device=elem.device)
            out = elem.new(storage).resize_(len(batch), *list(elem.size()))
        return torch.stack(batch, 0, out=out)

    if isinstance(elem, Mapping):
        try:
            return elem_type({key: tailors_collate([d[key] for d in batch]) for key in elem})
        except TypeError:
            return {key: tailors_collate([d[key] for d in batch]) for key in elem}

    if isinstance(elem, tuple) and hasattr(elem, '_fields'):  # namedtuple
        return elem_type(*(tailors_collate(samples) for samples in zip(*batch)))

    if isinstance(elem, Sequence):
        if _is_simple_sequence(batch):
            return batch

        _check_constant_size(batch)

        transposed = list(zip(*batch))
        if isinstance(elem, tuple):
            return [tailors_collate(samples) for samples in transposed]
        else:
            try:
                return elem_type([tailors_collate(samples) for samples in transposed])
            except TypeError:
                return [tailors_collate(samples,) for samples in transposed]

    if isinstance(elem, (str, int, float, bytes)):
        return batch

    if isinstance(batch, tuple):
        return batch

    raise TypeError(f"Can't handle type: {elem_type}")


def _check_constant_size(batch):
    it = iter(batch)
    elem_size = len(next(it))
    if not all(len(elem) == elem_size for elem in it):
        raise RuntimeError('each element in list of batch should be of equal size')


def _is_simple_sequence(batch):
    if isinstance(batch, str):
        return True
    if len(batch) == 0:
        return True
    if len(set(type(ele) for ele in batch)) > 1:
        return False
    if isinstance(batch[0], (str, int, float, bytes, bool)):
        return True
    if isinstance(batch[0], Sequence):
        return _is_simple_sequence(batch[0])
    return False
