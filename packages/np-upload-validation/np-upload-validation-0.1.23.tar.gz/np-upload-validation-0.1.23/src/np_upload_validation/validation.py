import datetime
import logging
import pathlib
import typing

from . import local as local_utils
from . import models, npc, utils

logger = logging.getLogger(__name__)


def validate(
    session_id: str, exp_dir_root: pathlib.Path
) -> typing.Union[list[models.UploadIntegrity], None]:
    uploaded = npc.get_uploaded_timing_data_paths(session_id)
    if uploaded is None:
        return None

    local = local_utils.get_local_timing_data_paths(exp_dir_root, session_id)
    paired = utils.pair_timing_data(uploaded, local)

    validated = []
    for paired_uploaded, paired_local in paired:
        validated.append(
            models.UploadIntegrity(
                session_id=session_id,
                timestamp=datetime.datetime.now().isoformat(),
                local=[utils.get_dat_info(path) for path in paired_local],
                uploaded=utils.get_zarr_info(paired_uploaded.path),
            )
        )

    return validated
