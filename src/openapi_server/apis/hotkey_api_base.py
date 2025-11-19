# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.hotkey_family_history_order import HotkeyFamilyHistoryOrder
from openapi_server.models.hotkey_family_response import HotkeyFamilyResponse
from openapi_server.security_api import get_token_api_key

class BaseHotkeyApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseHotkeyApi.subclasses = BaseHotkeyApi.subclasses + (cls,)
    async def get_hotkey_family_history(
        self,
        hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex formatted public key")],
        netuid: Annotated[Optional[int], Field(description="Subnet ID")],
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[HotkeyFamilyHistoryOrder],
    ) -> HotkeyFamilyResponse:
        ...


    async def get_hotkey_family_latest(
        self,
        hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        netuid: Annotated[Optional[int], Field(description="Subnet ID")],
        page: Optional[int],
        limit: Optional[int],
    ) -> HotkeyFamilyResponse:
        ...
