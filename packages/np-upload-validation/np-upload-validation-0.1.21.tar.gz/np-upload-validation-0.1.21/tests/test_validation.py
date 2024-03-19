# import os
# import dotenv
# import pytest

# from np_upload_validation import validation, timing_data


# dotenv.load_dotenv()
# import upath


# UNCOMPRESSED_TIMING_DATA_PATH = os.getenv("UNCOMPRESSED_TIMING_DATA_PATH")
# COMPRESSED_TIMING_DATA_PATH = os.getenv("COMPRESSED_TIMING_DATA_PATH")


# @pytest.mark.onprem
# @pytest.mark.skipif(
#     UNCOMPRESSED_TIMING_DATA_PATH is None,
#     reason="No uncompressed timing data path.")
# @pytest.mark.skipif(
#     COMPRESSED_TIMING_DATA_PATH is None,
#     reason="No compressed timing data path.")
# def test__validate_upload_integrity_success() -> None:
#     result = validation._validate_upload_integrity(
#         timing_data.timing_data_from_dat(UNCOMPRESSED_TIMING_DATA_PATH),
#         upath.UPath(
#             timing_data.timing_data_from_zarr(COMPRESSED_TIMING_DATA_PATH)
#         ),
#         "bur",
#         10000,
#     )

#     assert result.s3_checksum == result.isilon_checksum

# @pytest.mark.slow
# @pytest.mark.onprem
# @pytest.mark.parametrize("session_id", [
#     '686176_2023-12-07',
# ])
# def test__validate_upload_integrity_success(session_id: str) -> None:
#     timing_data = next(npc.generate_timing_data(session_id))

#     result = validation._validate_upload_integrity(
#         *timing_data,
#         session_id,
#         10000,
#     )

#     assert result.s3_checksum == result.isilon_checksum


# @pytest.mark.slow
# @pytest.mark.onprem
# @pytest.mark.parametrize("session_id", [
#     '686176_2023-12-07',
# ])
# def test__validate_upload_integrity_failure(session_id: str) -> None:
#     info = npc_lims.get_session_info(
#         session=session_id,
#     )

#     s3 = npc_sessions.Session(info)
#     isilon = npc_sessions.Session(info.allen_path)
#     timing_data = next(isilon.ephys_timing_data)
#     isilon_timing_data = npc._get_timing_data(timing_data.device)
#     s3_timing_data = npc._get_timing_data(
#         next(
#             d.device for d in s3.ephys_timing_data 
#             if d.device.name.lower() != timing_data.device.name.lower()
#         )
#     )

#     result = validation._validate_upload_integrity(
#         isilon_timing_data,
#         s3_timing_data,
#         session_id,
#         10000,
#     )

#     assert result.s3_checksum == result.isilon_checksum
