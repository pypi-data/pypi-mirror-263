import pydantic
import upath


class UploadedTimingData(pydantic.BaseModel):

    class Config:
        arbitrary_types_allowed = True

    device_name: str
    path: upath.UPath


class ArrayInfo(pydantic.BaseModel):

    path: str
    size: int
    dtype: str


class UploadIntegrity(pydantic.BaseModel):

    session_id: str
    timestamp: str
    local: list[ArrayInfo]
    uploaded: ArrayInfo
