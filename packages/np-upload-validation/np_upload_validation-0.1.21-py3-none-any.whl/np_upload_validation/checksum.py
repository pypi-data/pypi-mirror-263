import logging
import math
import zlib

from . import exceptions

logger = logging.getLogger(__name__)


def _slice_generator(
    arr,
    chunk_size: int,
):
    """Iteratively steps through numpy array without reading whole thing
    into memory, hopefully...
    """
    if len(arr.shape) > 2:
        raise Exception("Unsupported shape: %s" % arr.shape)

    # idx = 0
    n_steps = math.ceil(arr.shape[0] / chunk_size)
    # logger.debug("N steps: %s" % n_steps)
    for i in range(0, n_steps):
        start = i * chunk_size
        yield arr[start : start + chunk_size]


def _array_slicer(
    arr,
    chunk_size_0: int,
    chunk_size_1: int,
):
    if len(arr.shape) > 2:
        raise Exception(f"Unsupported shape: {arr.shape}")

    for chunk in _slice_generator(arr, chunk_size_0):
        for s_chunk in _slice_generator(chunk, chunk_size_1):
            yield s_chunk


def checksum_array(
    arr,
    chunk_size_0: int = 1000,
    chunk_size_1: int = 1,
    initial: int = 0,
) -> str:
    """Generates a CR32 checksum from a slice of a 2d array.

    Parameters
    ----------
    arr: input array
    chunk_size_0: step size for 1st dimension of array
    chunk_size_1: step size for 2nd dimension of array
    initial: seed value

    Notes
    -----
    - Steps through the array and calculates a rolling checksum
    - Changes to chunk sizes will yield different results due to changes
    in the traversal of the array
    - Checksum value is iteratively generated as a cr32 of bytes of current slice (seed is rolling):
    https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tobytes.html
    """
    if len(arr.shape) > 2:
        raise exceptions.ValidationException(f"Unsupported array shape: {arr.shape}")

    logger.debug(f"Starting checksum for arr shape: {arr.shape}")
    checksum = initial
    for idx, slice in enumerate(_array_slicer(arr, chunk_size_0, chunk_size_1)):
        bytes_repr = slice.tobytes()
        if idx < 5:  # only log for the first 5 slices
            logger.debug(f"Checksum initial: {checksum}")
            logger.debug(f"Slice: {slice}")
            logger.debug("Slice bytes: %s" % bytes_repr)
        # logger.debug("Slice bytes: %s" % bytes_repr)
        checksum = zlib.crc32(bytes_repr, checksum)
        if idx < 5:
            logger.debug(f"Checksum post: {checksum}")
    # logger.debug(f"Final checksum: {checksum}")

    return f"{checksum:08X}"
