# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.evmerc20_account_order import EVMERC20AccountOrder
from openapi_server.models.evmerc20_account_response import EVMERC20AccountResponse
from openapi_server.models.evmerc20_token_order import EVMERC20TokenOrder
from openapi_server.models.evmerc20_token_response import EVMERC20TokenResponse
from openapi_server.models.evmerc20_transfer_order import EVMERC20TransferOrder
from openapi_server.models.evmerc20_transfer_response import EVMERC20TransferResponse
from openapi_server.security_api import get_token_api_key

class BaseErc20Api:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseErc20Api.subclasses = BaseErc20Api.subclasses + (cls,)
    async def get_evm_erc20_account(
        self,
        address: Optional[StrictStr],
        token_name: Optional[StrictStr],
        token_symbol: Optional[StrictStr],
        token_address: Optional[StrictStr],
        balance_min: Annotated[Optional[StrictStr], Field(description="Minimum balance (inclusive)")],
        balance_max: Annotated[Optional[StrictStr], Field(description="Maximum balance (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[EVMERC20AccountOrder],
    ) -> EVMERC20AccountResponse:
        ...


    async def get_evm_erc20_token(
        self,
        address: Optional[StrictStr],
        name: Optional[StrictStr],
        symbol: Optional[StrictStr],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[EVMERC20TokenOrder],
    ) -> EVMERC20TokenResponse:
        ...


    async def get_evm_erc20_transfer(
        self,
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        address: Optional[StrictStr],
        to: Optional[StrictStr],
        var_from: Optional[StrictStr],
        transaction_hash: Optional[StrictStr],
        token_name: Optional[StrictStr],
        token_symbol: Optional[StrictStr],
        token_address: Optional[StrictStr],
        amount_min: Annotated[Optional[StrictStr], Field(description="Minimum amount (inclusive)")],
        amount_max: Annotated[Optional[StrictStr], Field(description="Maximum amount (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[EVMERC20TransferOrder],
    ) -> EVMERC20TransferResponse:
        ...
