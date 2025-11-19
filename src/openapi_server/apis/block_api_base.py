# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.block_emission_order import BlockEmissionOrder
from openapi_server.models.block_emission_response import BlockEmissionResponse
from openapi_server.models.block_interval_order import BlockIntervalOrder
from openapi_server.models.block_interval_response import BlockIntervalResponse
from openapi_server.models.block_order import BlockOrder
from openapi_server.models.block_response import BlockResponse
from openapi_server.models.frequency_hour_day import FrequencyHourDay
from openapi_server.security_api import get_token_api_key

class BaseBlockApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseBlockApi.subclasses = BaseBlockApi.subclasses + (cls,)
    async def get_block_emission(
        self,
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[BlockEmissionOrder],
    ) -> BlockEmissionResponse:
        ...


    async def get_block_interval(
        self,
        timestamp_start: Annotated[int, Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[int, Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        frequency: Annotated[Optional[FrequencyHourDay], Field(description="Default by_day")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[BlockIntervalOrder],
    ) -> BlockIntervalResponse:
        ...


    async def get_block(
        self,
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        hash: Optional[StrictStr],
        spec_version: Optional[int],
        validator: Optional[StrictStr],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[BlockOrder],
    ) -> BlockResponse:
        ...
