# import datetime
# import logging
# import typing

# from spikeinterface.preprocessing import correct_lsb

# from . import checksum, models, npc

# logger = logging.getLogger(__name__)


# def _validate_upload_integrity(
#     timing_data_isilon: models.TimingData,
#     timing_data_s3: models.TimingData,
#     session_id: str,
#     chunk_size: int,
# ) -> models.UploadIntegrity:
#     logger.debug("Calculating checksum for: %s" % timing_data_isilon.path)
#     isilon_checksum = checksum.checksum_array(
#         correct_lsb(timing_data_isilon.data),
#         chunk_size,
#         1,
#     )
#     logger.debug("Calculating checksum for: %s" % timing_data_s3.path)
#     s3_checksum = checksum.checksum_array(
#         timing_data_s3.data,
#         chunk_size,
#         1,
#     )
#     return models.UploadIntegrity(
#         session_id=session_id,
#         isilon_path=timing_data_isilon.path,
#         isilon_checksum=isilon_checksum,
#         s3_path=timing_data_s3.path,
#         s3_checksum=s3_checksum,
#         timestamp=datetime.datetime.now().isoformat(),
#     )


# def validate_npc_session(
#     session_id: str,
#     chunk_size: int = 1000,
# ) -> typing.Generator[models.UploadIntegrity, None, None]:
#     for (
#         timing_data_isilon,
#         timing_data_s3,
#     ) in npc.generate_timing_data(session_id):
#         yield _validate_upload_integrity(
#             timing_data_isilon,
#             timing_data_s3,
#             session_id,
#             chunk_size,
#         )
