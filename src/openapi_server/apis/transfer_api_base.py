# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.network_with_all import NetworkWithAll
from openapi_server.models.transfer_order import TransferOrder
from openapi_server.models.transfer_response import TransferResponse
from openapi_server.security_api import get_token_api_key

class BaseTransferApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseTransferApi.subclasses = BaseTransferApi.subclasses + (cls,)
    async def get_transfer(
        self,
        network: Optional[NetworkWithAll],
        address: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        var_from: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        to: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        transaction_hash: Optional[StrictStr],
        extrinsic_id: Optional[StrictStr],
        amount_min: Annotated[Optional[StrictStr], Field(description="Minimum amount (inclusive)")],
        amount_max: Annotated[Optional[StrictStr], Field(description="Maximum amount (inclusive)")],
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[TransferOrder],
    ) -> TransferResponse:
        ...
