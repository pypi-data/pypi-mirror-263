import typing

import pydantic


class TimingData(pydantic.BaseModel):

    data: typing.Any
    path: str


class UploadIntegrity(pydantic.BaseModel):

    session_id: str
    isilon_paths: list[str]
    s3_path: str
    isilon_checksums: list[str]
    s3_checksum: str
    timestamp: str
