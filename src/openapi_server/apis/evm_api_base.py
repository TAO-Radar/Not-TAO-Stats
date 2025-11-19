# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.evm_block_order import EVMBlockOrder
from openapi_server.models.evm_block_response import EVMBlockResponse
from openapi_server.models.evm_contract_order import EVMContractOrder
from openapi_server.models.evm_contract_response import EVMContractResponse
from openapi_server.models.evm_log_order import EVMLogOrder
from openapi_server.models.evm_log_response import EVMLogResponse
from openapi_server.models.evm_transaction_order import EVMTransactionOrder
from openapi_server.models.evm_transaction_response import EVMTransactionResponse
from openapi_server.security_api import get_token_api_key

class BaseEvmApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseEvmApi.subclasses = BaseEvmApi.subclasses + (cls,)
    async def get_evm_address_from_ss58(
        self,
        ss58_address: StrictStr,
    ) -> str:
        ...


    async def get_evm_block(
        self,
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[EVMBlockOrder],
    ) -> EVMBlockResponse:
        ...


    async def get_evm_contract(
        self,
        address: Optional[StrictStr],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[EVMContractOrder],
    ) -> EVMContractResponse:
        ...


    async def get_evm_log(
        self,
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        transaction_hash: Optional[StrictStr],
        address: Optional[StrictStr],
        event_name: Optional[StrictStr],
        topic0: Optional[StrictStr],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[EVMLogOrder],
    ) -> EVMLogResponse:
        ...


    async def get_evm_transaction(
        self,
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        hash: Optional[StrictStr],
        address: Optional[StrictStr],
        to: Optional[StrictStr],
        var_from: Optional[StrictStr],
        method_name: Optional[StrictStr],
        method_id: Optional[StrictStr],
        contract_created: Optional[StrictStr],
        index: Optional[int],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[EVMTransactionOrder],
    ) -> EVMTransactionResponse:
        ...
