import numpy as np
import upath
import zarr

from . import models


def timing_data_from_dat(path: str) -> models.TimingData:
    return models.TimingData(
        data=np.memmap(
            path,
            dtype=np.int16,
            mode="r",
        ).reshape(-1, 384),
        path=path,
    )


def timing_data_from_zarr(path: upath.UPath) -> models.TimingData:
    return models.TimingData(
        data=zarr.open(path, mode="r")["traces_seg0"],
        path=path.path,
    )
