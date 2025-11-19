# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.miner_autostake_order import MinerAutostakeOrder
from openapi_server.models.miner_autostake_response import MinerAutostakeResponse
from openapi_server.models.miner_coldkey_response import MinerColdkeyResponse
from openapi_server.models.miner_weights_history_order import MinerWeightsHistoryOrder
from openapi_server.models.miner_weights_latest_order import MinerWeightsLatestOrder
from openapi_server.models.miner_weights_response import MinerWeightsResponse
from openapi_server.security_api import get_token_api_key

class BaseMinerApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseMinerApi.subclasses = BaseMinerApi.subclasses + (cls,)
    async def get_miner_autostake(
        self,
        netuid: Optional[int],
        hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        coldkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        destination_hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[MinerAutostakeOrder],
    ) -> MinerAutostakeResponse:
        ...


    async def get_miner_coldkey(
        self,
        coldkey: Annotated[StrictStr, Field(description="SS58 or hex format")],
        days: int,
    ) -> MinerColdkeyResponse:
        ...


    async def get_miner_weights_history(
        self,
        netuid: int,
        miner_uid: Optional[int],
        validator_uid: Optional[int],
        miner_hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        validator_hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        block_number: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[MinerWeightsHistoryOrder],
    ) -> MinerWeightsResponse:
        ...


    async def get_miner_weights_latest(
        self,
        netuid: int,
        miner_uid: Optional[int],
        validator_uid: Optional[int],
        miner_hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        validator_hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[MinerWeightsLatestOrder],
    ) -> MinerWeightsResponse:
        ...
