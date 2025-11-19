# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.proxy_call_order import ProxyCallOrder
from openapi_server.models.proxy_call_response import ProxyCallResponse
from openapi_server.security_api import get_token_api_key

class BaseProxyCallApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseProxyCallApi.subclasses = BaseProxyCallApi.subclasses + (cls,)
    async def get_proxy_call(
        self,
        id: Optional[StrictStr],
        signer_address: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        real_address: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        network: Optional[StrictStr],
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        extrinsic_hash: Optional[StrictStr],
        extrinsic_id: Optional[StrictStr],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[ProxyCallOrder],
    ) -> ProxyCallResponse:
        ...
