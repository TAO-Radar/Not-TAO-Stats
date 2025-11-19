# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictBool, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.metagraph_history_order import MetagraphHistoryOrder
from openapi_server.models.metagraph_history_response import MetagraphHistoryResponse
from openapi_server.models.metagraph_order import MetagraphOrder
from openapi_server.models.metagraph_response import MetagraphResponse
from openapi_server.models.root_metagraph_history_order import RootMetagraphHistoryOrder
from openapi_server.models.root_metagraph_history_response import RootMetagraphHistoryResponse
from openapi_server.models.root_metagraph_order import RootMetagraphOrder
from openapi_server.models.root_metagraph_response import RootMetagraphResponse
from openapi_server.security_api import get_token_api_key

class BaseMetagraphApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseMetagraphApi.subclasses = BaseMetagraphApi.subclasses + (cls,)
    async def get_metagraph_history(
        self,
        netuid: Annotated[Optional[int], Field(description="Subnet ID")],
        uid: Annotated[Optional[int], Field(description="Neuron ID")],
        hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        coldkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[MetagraphHistoryOrder],
    ) -> MetagraphHistoryResponse:
        ...


    async def get_metagraph_latest(
        self,
        netuid: Annotated[Optional[int], Field(description="Subnet ID")],
        search: Annotated[Optional[StrictStr], Field(description="Search across UID, hotkey, coldkey, axon_ip")],
        uid: Annotated[Optional[int], Field(description="Neuron ID")],
        active: Optional[StrictBool],
        hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        coldkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        validator_permit: Optional[StrictBool],
        is_immunity_period: Optional[StrictBool],
        is_child_key: Optional[StrictBool],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[MetagraphOrder],
    ) -> MetagraphResponse:
        ...


    async def get_metagraph_root_history(
        self,
        hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[RootMetagraphHistoryOrder],
    ) -> RootMetagraphHistoryResponse:
        ...


    async def get_metagraph_root_latest(
        self,
        hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[RootMetagraphOrder],
    ) -> RootMetagraphResponse:
        ...
