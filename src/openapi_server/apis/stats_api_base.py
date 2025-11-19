# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.stats_history_order import StatsHistoryOrder
from openapi_server.models.stats_response import StatsResponse
from openapi_server.security_api import get_token_api_key

class BaseStatsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseStatsApi.subclasses = BaseStatsApi.subclasses + (cls,)
    async def get_stats_history(
        self,
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[StatsHistoryOrder],
    ) -> StatsResponse:
        ...


    async def get_stats_latest(
        self,
    ) -> StatsResponse:
        ...
