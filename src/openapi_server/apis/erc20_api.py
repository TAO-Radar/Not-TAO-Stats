# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.erc20_api_base import BaseErc20Api
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
from openapi_server.models.evmerc20_account_order import EVMERC20AccountOrder
from openapi_server.models.evmerc20_account_response import EVMERC20AccountResponse
from openapi_server.models.evmerc20_token_order import EVMERC20TokenOrder
from openapi_server.models.evmerc20_token_response import EVMERC20TokenResponse
from openapi_server.models.evmerc20_transfer_order import EVMERC20TransferOrder
from openapi_server.models.evmerc20_transfer_response import EVMERC20TransferResponse
from openapi_server.security_api import get_token_api_key

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/evm/erc20/account/v1",
    responses={
        200: {"model": EVMERC20AccountResponse, "description": "Accounts retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Accounts not found"},
        500: {"description": "Internal server error"},
    },
    tags=["erc20"],
    response_model_by_alias=True,
)
async def get_evm_erc20_account(
    address: Optional[StrictStr] = Query(None, description="", alias="address"),
    token_name: Optional[StrictStr] = Query(None, description="", alias="token_name"),
    token_symbol: Optional[StrictStr] = Query(None, description="", alias="token_symbol"),
    token_address: Optional[StrictStr] = Query(None, description="", alias="token_address"),
    balance_min: Annotated[Optional[StrictStr], Field(description="Minimum balance (inclusive)")] = Query(None, description="Minimum balance (inclusive)", alias="balance_min"),
    balance_max: Annotated[Optional[StrictStr], Field(description="Maximum balance (inclusive)")] = Query(None, description="Maximum balance (inclusive)", alias="balance_max"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[EVMERC20AccountOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> EVMERC20AccountResponse:
    if not BaseErc20Api.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseErc20Api.subclasses[0]().get_evm_erc20_account(address, token_name, token_symbol, token_address, balance_min, balance_max, page, limit, order)


@router.get(
    "/api/evm/erc20/token/v1",
    responses={
        200: {"model": EVMERC20TokenResponse, "description": "Tokens retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Tokens not found"},
        500: {"description": "Internal server error"},
    },
    tags=["erc20"],
    response_model_by_alias=True,
)
async def get_evm_erc20_token(
    address: Optional[StrictStr] = Query(None, description="", alias="address"),
    name: Optional[StrictStr] = Query(None, description="", alias="name"),
    symbol: Optional[StrictStr] = Query(None, description="", alias="symbol"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[EVMERC20TokenOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> EVMERC20TokenResponse:
    if not BaseErc20Api.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseErc20Api.subclasses[0]().get_evm_erc20_token(address, name, symbol, page, limit, order)


@router.get(
    "/api/evm/erc20/transfer/v1",
    responses={
        200: {"model": EVMERC20TransferResponse, "description": "Transfers retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Transfers not found"},
        500: {"description": "Internal server error"},
    },
    tags=["erc20"],
    response_model_by_alias=True,
)
async def get_evm_erc20_transfer(
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    address: Optional[StrictStr] = Query(None, description="", alias="address"),
    to: Optional[StrictStr] = Query(None, description="", alias="to"),
    var_from: Optional[StrictStr] = Query(None, description="", alias="from"),
    transaction_hash: Optional[StrictStr] = Query(None, description="", alias="transaction_hash"),
    token_name: Optional[StrictStr] = Query(None, description="", alias="token_name"),
    token_symbol: Optional[StrictStr] = Query(None, description="", alias="token_symbol"),
    token_address: Optional[StrictStr] = Query(None, description="", alias="token_address"),
    amount_min: Annotated[Optional[StrictStr], Field(description="Minimum amount (inclusive)")] = Query(None, description="Minimum amount (inclusive)", alias="amount_min"),
    amount_max: Annotated[Optional[StrictStr], Field(description="Maximum amount (inclusive)")] = Query(None, description="Maximum amount (inclusive)", alias="amount_max"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[EVMERC20TransferOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> EVMERC20TransferResponse:
    if not BaseErc20Api.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseErc20Api.subclasses[0]().get_evm_erc20_transfer(block_number, block_start, block_end, timestamp_start, timestamp_end, address, to, var_from, transaction_hash, token_name, token_symbol, token_address, amount_min, amount_max, page, limit, order)
