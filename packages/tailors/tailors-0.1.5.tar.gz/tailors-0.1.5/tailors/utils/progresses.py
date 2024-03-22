import logging
import sys
from collections.abc import Iterable
from contextlib import contextmanager

from tqdm.auto import tqdm
from tqdm.contrib.logging import logging_redirect_tqdm
from tqdm.utils import _screen_shape_wrapper


@contextmanager
def progressive(iterable: Iterable | None = None,
                total: int | float | None = None,
                desc: str | None = None,
                ncols: int | float | None = 0.9,
                leave: bool | None = None,
                ascii: bool | str | None = '░▒▓',
                unit: str | None = None,
                unit_scale: bool | int | float | None = None,
                position: int | None = None,
                postfix: dict | None = None,
                unit_divisor: float | None = None,
                colour: str | None = 'cyan',
                margin_end: int | None = 10,
                loggers: list[logging.Logger] | None = None,
                **kwargs):
    params = {
        'total': total,
        'desc': desc,
        'ncols': ncols,
        'leave': leave,
        'ascii': ascii,
        'unit': unit,
        'unit_scale': unit_scale,
        'position': position,
        'postfix': postfix,
        'unit_divisor': unit_divisor,
        'colour': colour,
        **kwargs
    }
    params = {k: v for k, v in params.items() if v is not None}
    if params.get('dynamic_ncols') is None:
        ncols = params.get('ncols')
        screen_width = get_screen_width()
        if ncols is None:
            params['ncols'] = screen_width - margin_end
        if isinstance(ncols, float):
            params['ncols'] = int(screen_width * ncols)
    with tqdm(iterable, **params) as pbar:
        with logging_redirect_tqdm(loggers=loggers):
            yield pbar


def get_screen_width():
    screen_shaper = _screen_shape_wrapper()
    return screen_shaper(sys.stdout)[0] or 160
