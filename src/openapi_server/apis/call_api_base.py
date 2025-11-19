# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictBool, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.call_order import CallOrder
from openapi_server.models.call_response import CallResponse
from openapi_server.models.network import Network
from openapi_server.security_api import get_token_api_key

class BaseCallApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseCallApi.subclasses = BaseCallApi.subclasses + (cls,)
    async def get_call(
        self,
        origin_address: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        network: Optional[Network],
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        success: Optional[StrictBool],
        full_name: Optional[StrictStr],
        id: Optional[StrictStr],
        extrinsic_id: Optional[StrictStr],
        parent_id: Optional[StrictStr],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[CallOrder],
    ) -> CallResponse:
        ...
