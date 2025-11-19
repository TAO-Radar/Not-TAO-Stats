# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.account_history_order import AccountHistoryOrder
from openapi_server.models.account_history_response import AccountHistoryResponse
from openapi_server.models.account_order import AccountOrder
from openapi_server.models.account_response import AccountResponse
from openapi_server.security_api import get_token_api_key

class BaseAccountApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseAccountApi.subclasses = BaseAccountApi.subclasses + (cls,)
    async def get_account_history(
        self,
        address: Annotated[StrictStr, Field(description="SS58 or hex format")],
        network: Annotated[Optional[StrictStr], Field(description="finney, nakamoto, kusanagi")],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[AccountHistoryOrder],
    ) -> AccountHistoryResponse:
        ...


    async def get_account_latest(
        self,
        address: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        balance_free_min: Optional[StrictStr],
        balance_free_max: Optional[StrictStr],
        balance_staked_min: Optional[StrictStr],
        balance_staked_max: Optional[StrictStr],
        balance_staked_root_min: Optional[StrictStr],
        balance_staked_root_max: Optional[StrictStr],
        balance_staked_alpha_as_tao_min: Optional[StrictStr],
        balance_staked_alpha_as_tao_max: Optional[StrictStr],
        balance_total_min: Optional[StrictStr],
        balance_total_max: Optional[StrictStr],
        rank: Optional[int],
        created_on_network: Annotated[Optional[StrictStr], Field(description="finney, nakamoto, kusanagi")],
        created_on_timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        created_on_timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[AccountOrder],
    ) -> AccountResponse:
        ...
