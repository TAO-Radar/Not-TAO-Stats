# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictBool, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.dtao_liquidity_distribution_response import DtaoLiquidityDistributionResponse
from openapi_server.models.dtao_liquidity_position_event_order import DtaoLiquidityPositionEventOrder
from openapi_server.models.dtao_liquidity_position_event_response import DtaoLiquidityPositionEventResponse
from openapi_server.models.dtao_liquidity_position_history_order import DtaoLiquidityPositionHistoryOrder
from openapi_server.models.dtao_liquidity_position_history_response import DtaoLiquidityPositionHistoryResponse
from openapi_server.models.dtao_liquidity_position_order import DtaoLiquidityPositionOrder
from openapi_server.models.dtao_liquidity_position_response import DtaoLiquidityPositionResponse
from openapi_server.models.dtao_tick_to_price_response import DtaoTickToPriceResponse
from openapi_server.models.liquidity_position_status import LiquidityPositionStatus
from openapi_server.models.liquidity_position_type import LiquidityPositionType
from openapi_server.security_api import get_token_api_key

class BaseLiquidityApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseLiquidityApi.subclasses = BaseLiquidityApi.subclasses + (cls,)
    async def get_dtao_liquidity_distribution(
        self,
        netuid: int,
        min_price: Optional[StrictStr],
        max_price: Optional[StrictStr],
        num_points: Annotated[Optional[int], Field(description="Number of data points to return (default: 200, max: 1000)")],
        log_scale: Annotated[Optional[StrictBool], Field(description="Use logarithmic scale for price distribution (default: true)")],
    ) -> DtaoLiquidityDistributionResponse:
        ...


    async def get_dtao_liquidity_position_history(
        self,
        position_id: StrictStr,
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[DtaoLiquidityPositionHistoryOrder],
    ) -> DtaoLiquidityPositionHistoryResponse:
        ...


    async def get_dtao_liquidity_position(
        self,
        id: Optional[StrictStr],
        coldkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        netuid: Optional[int],
        status: Optional[LiquidityPositionStatus],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[DtaoLiquidityPositionOrder],
    ) -> DtaoLiquidityPositionResponse:
        ...


    async def get_dtao_liquidity_position_event(
        self,
        id: Optional[StrictStr],
        position_id: Optional[StrictStr],
        coldkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        netuid: Optional[int],
        position_type: Optional[LiquidityPositionType],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[DtaoLiquidityPositionEventOrder],
    ) -> DtaoLiquidityPositionEventResponse:
        ...


    async def get_dtao_liquidity_tick_to_price(
        self,
        tick: int,
    ) -> DtaoTickToPriceResponse:
        ...
