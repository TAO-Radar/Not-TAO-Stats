# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.price_history_order import PriceHistoryOrder
from openapi_server.models.price_ohlc_period import PriceOHLCPeriod
from openapi_server.models.price_ohlc_response import PriceOHLCResponse
from openapi_server.models.price_response import PriceResponse
from openapi_server.models.price_simple_response import PriceSimpleResponse
from openapi_server.security_api import get_token_api_key

class BasePriceApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BasePriceApi.subclasses = BasePriceApi.subclasses + (cls,)
    async def get_price_history(
        self,
        asset: StrictStr,
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[PriceHistoryOrder],
    ) -> PriceResponse:
        ...


    async def get_price_latest(
        self,
        asset: StrictStr,
    ) -> PriceResponse:
        ...


    async def get_price_ohlc(
        self,
        asset: StrictStr,
        period: PriceOHLCPeriod,
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
    ) -> PriceOHLCResponse:
        ...


    async def get_price_simple_latest(
        self,
    ) -> PriceSimpleResponse:
        ...
