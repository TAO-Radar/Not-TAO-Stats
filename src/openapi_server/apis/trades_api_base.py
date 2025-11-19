# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.dtao_trade_order import DtaoTradeOrder
from openapi_server.models.dtao_trade_response import DtaoTradeResponse
from openapi_server.security_api import get_token_api_key

class BaseTradesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseTradesApi.subclasses = BaseTradesApi.subclasses + (cls,)
    async def get_dtao_trade(
        self,
        coldkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        extrinsic_id: Optional[StrictStr],
        from_name: Optional[StrictStr],
        to_name: Optional[StrictStr],
        tao_value_min: Annotated[Optional[StrictStr], Field(description="Minimum amount (inclusive)")],
        tao_value_max: Annotated[Optional[StrictStr], Field(description="Maximum amount (inclusive)")],
        usd_value_min: Annotated[Optional[StrictStr], Field(description="Minimum amount (inclusive)")],
        usd_value_max: Annotated[Optional[StrictStr], Field(description="Maximum amount (inclusive)")],
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[DtaoTradeOrder],
    ) -> DtaoTradeResponse:
        ...
