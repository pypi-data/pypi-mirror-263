import os
import random

import gpustat
import hao

LOGGER = hao.logs.get_logger(__name__)


def set_auto():
    stats = gpustat.GPUStatCollection.new_query()
    ids = map(lambda gpu: int(gpu.entry['index']), stats)
    ratios = map(lambda gpu: float(gpu.entry['memory.used'])/float(gpu.entry['memory.total']), stats)
    pairs = list(zip(ids, ratios))
    random.shuffle(pairs)
    gpu_id = min(pairs, key=lambda x: x[1])[0]

    os.environ['CUDA_DEVICE_ORDER'] = 'PCI_BUS_ID'
    os.environ['CUDA_VISIBLE_DEVICES'] = str(gpu_id)
    LOGGER.info(f"[devices] set CUDA_VISIBLE_DEVICES={gpu_id}")
