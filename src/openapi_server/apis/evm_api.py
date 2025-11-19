# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.evm_api_base import BaseEvmApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
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

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/evm/address_from_ss58/v1",
    responses={
        200: {"model": str, "description": "Address retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Address not found"},
        500: {"description": "Internal server error"},
    },
    tags=["evm"],
    response_model_by_alias=True,
)
async def get_evm_address_from_ss58(
    ss58_address: StrictStr = Query(None, description="", alias="ss58_address"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> str:
    if not BaseEvmApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseEvmApi.subclasses[0]().get_evm_address_from_ss58(ss58_address)


@router.get(
    "/api/evm/block/v1",
    responses={
        200: {"model": EVMBlockResponse, "description": "Blocks retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Blocks not found"},
        500: {"description": "Internal server error"},
    },
    tags=["evm"],
    response_model_by_alias=True,
)
async def get_evm_block(
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[EVMBlockOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> EVMBlockResponse:
    if not BaseEvmApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseEvmApi.subclasses[0]().get_evm_block(block_number, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/evm/contract/v1",
    responses={
        200: {"model": EVMContractResponse, "description": "Contracts retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Contracts not found"},
        500: {"description": "Internal server error"},
    },
    tags=["evm"],
    response_model_by_alias=True,
)
async def get_evm_contract(
    address: Optional[StrictStr] = Query(None, description="", alias="address"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[EVMContractOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> EVMContractResponse:
    if not BaseEvmApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseEvmApi.subclasses[0]().get_evm_contract(address, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/evm/log/v1",
    responses={
        200: {"model": EVMLogResponse, "description": "Logs retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Logs not found"},
        500: {"description": "Internal server error"},
    },
    tags=["evm"],
    response_model_by_alias=True,
)
async def get_evm_log(
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    transaction_hash: Optional[StrictStr] = Query(None, description="", alias="transaction_hash"),
    address: Optional[StrictStr] = Query(None, description="", alias="address"),
    event_name: Optional[StrictStr] = Query(None, description="", alias="event_name"),
    topic0: Optional[StrictStr] = Query(None, description="", alias="topic0"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[EVMLogOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> EVMLogResponse:
    if not BaseEvmApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseEvmApi.subclasses[0]().get_evm_log(block_number, block_start, block_end, timestamp_start, timestamp_end, transaction_hash, address, event_name, topic0, page, limit, order)


@router.get(
    "/api/evm/transaction/v1",
    responses={
        200: {"model": EVMTransactionResponse, "description": "Transactions retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Transactions not found"},
        500: {"description": "Internal server error"},
    },
    tags=["evm"],
    response_model_by_alias=True,
)
async def get_evm_transaction(
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    hash: Optional[StrictStr] = Query(None, description="", alias="hash"),
    address: Optional[StrictStr] = Query(None, description="", alias="address"),
    to: Optional[StrictStr] = Query(None, description="", alias="to"),
    var_from: Optional[StrictStr] = Query(None, description="", alias="from"),
    method_name: Optional[StrictStr] = Query(None, description="", alias="method_name"),
    method_id: Optional[StrictStr] = Query(None, description="", alias="method_id"),
    contract_created: Optional[StrictStr] = Query(None, description="", alias="contract_created"),
    index: Optional[int] = Query(None, description="", alias="index"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[EVMTransactionOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> EVMTransactionResponse:
    if not BaseEvmApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseEvmApi.subclasses[0]().get_evm_transaction(block_number, block_start, block_end, timestamp_start, timestamp_end, hash, address, to, var_from, method_name, method_id, contract_created, index, page, limit, order)
