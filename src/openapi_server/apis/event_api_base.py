# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.event_order import EventOrder
from openapi_server.models.event_response import EventResponse
from openapi_server.models.network import Network
from openapi_server.security_api import get_token_api_key

class BaseEventApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseEventApi.subclasses = BaseEventApi.subclasses + (cls,)
    async def get_event(
        self,
        network: Optional[Network],
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        pallet: Optional[StrictStr],
        name: Optional[StrictStr],
        full_name: Annotated[Optional[StrictStr], Field(description="Full name of the event, e.g. \"SubtensorModule.AxonServed\"")],
        extrinsic_id: Optional[StrictStr],
        call_id: Optional[StrictStr],
        id: Optional[StrictStr],
        phase: Optional[StrictStr],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[EventOrder],
    ) -> EventResponse:
        ...
