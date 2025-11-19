# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.stake_balance_history_order import StakeBalanceHistoryOrder
from openapi_server.models.stake_balance_response import StakeBalanceResponse
from openapi_server.security_api import get_token_api_key

class BaseStakeBalanceApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseStakeBalanceApi.subclasses = BaseStakeBalanceApi.subclasses + (cls,)
    async def get_stake_balance_history(
        self,
        coldkey: Annotated[StrictStr, Field(description="SS58 or hex format")],
        hotkey: Annotated[StrictStr, Field(description="SS58 or hex format")],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[StakeBalanceHistoryOrder],
    ) -> StakeBalanceResponse:
        ...
