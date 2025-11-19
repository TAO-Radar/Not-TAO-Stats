# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictBool, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.extrinsic_order import ExtrinsicOrder
from openapi_server.models.extrinsic_response import ExtrinsicResponse
from openapi_server.models.network_with_testnet import NetworkWithTestnet
from openapi_server.security_api import get_token_api_key

class BaseExtrinsicApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseExtrinsicApi.subclasses = BaseExtrinsicApi.subclasses + (cls,)
    async def get_extrinsic(
        self,
        network: Optional[NetworkWithTestnet],
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        hash: Optional[StrictStr],
        full_name: Optional[StrictStr],
        id: Optional[StrictStr],
        success: Optional[StrictBool],
        signer_address: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[ExtrinsicOrder],
    ) -> ExtrinsicResponse:
        ...
