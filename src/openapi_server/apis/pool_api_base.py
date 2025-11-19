# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.dtao_pool_history_order import DtaoPoolHistoryOrder
from openapi_server.models.dtao_pool_history_response import DtaoPoolHistoryResponse
from openapi_server.models.dtao_pool_order import DtaoPoolOrder
from openapi_server.models.dtao_pool_response import DtaoPoolResponse
from openapi_server.models.dtao_pool_total_price_history_order import DtaoPoolTotalPriceHistoryOrder
from openapi_server.models.dtao_pool_total_price_history_response import DtaoPoolTotalPriceHistoryResponse
from openapi_server.models.dtao_pool_total_price_latest_response import DtaoPoolTotalPriceLatestResponse
from openapi_server.models.frequency_block_hour_day import FrequencyBlockHourDay
from openapi_server.security_api import get_token_api_key

class BasePoolApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BasePoolApi.subclasses = BasePoolApi.subclasses + (cls,)
    async def get_dtao_pool_history(
        self,
        netuid: Optional[int],
        frequency: Optional[FrequencyBlockHourDay],
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[DtaoPoolHistoryOrder],
    ) -> DtaoPoolHistoryResponse:
        ...


    async def get_dtao_pool_latest(
        self,
        netuid: Optional[int],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[DtaoPoolOrder],
    ) -> DtaoPoolResponse:
        ...


    async def get_dtao_pool_total_price_history(
        self,
        frequency: Optional[FrequencyBlockHourDay],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[DtaoPoolTotalPriceHistoryOrder],
    ) -> DtaoPoolTotalPriceHistoryResponse:
        ...


    async def get_dtao_pool_total_price_latest(
        self,
    ) -> DtaoPoolTotalPriceLatestResponse:
        ...


    async def get_dtao_pool_total_price(
        self,
        frequency: Optional[FrequencyBlockHourDay],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[DtaoPoolTotalPriceHistoryOrder],
    ) -> DtaoPoolTotalPriceHistoryResponse:
        ...


    async def get_dtao_pool(
        self,
        netuid: Optional[int],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[DtaoPoolOrder],
    ) -> DtaoPoolResponse:
        ...
