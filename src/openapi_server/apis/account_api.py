# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.account_api_base import BaseAccountApi
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
from openapi_server.models.account_history_order import AccountHistoryOrder
from openapi_server.models.account_history_response import AccountHistoryResponse
from openapi_server.models.account_order import AccountOrder
from openapi_server.models.account_response import AccountResponse
from openapi_server.security_api import get_token_api_key

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/account/history/v1",
    responses={
        200: {"model": AccountHistoryResponse, "description": "Account history retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Account history not found"},
        500: {"description": "Internal server error"},
    },
    tags=["account"],
    response_model_by_alias=True,
)
async def get_account_history(
    address: Annotated[StrictStr, Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="address"),
    network: Annotated[Optional[StrictStr], Field(description="finney, nakamoto, kusanagi")] = Query(None, description="finney, nakamoto, kusanagi", alias="network"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[AccountHistoryOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> AccountHistoryResponse:
    if not BaseAccountApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAccountApi.subclasses[0]().get_account_history(address, network, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/account/latest/v1",
    responses={
        200: {"model": AccountResponse, "description": "Accounts retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Accounts not found"},
        500: {"description": "Internal server error"},
    },
    tags=["account"],
    response_model_by_alias=True,
)
async def get_account_latest(
    address: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="address"),
    balance_free_min: Optional[StrictStr] = Query(None, description="", alias="balance_free_min"),
    balance_free_max: Optional[StrictStr] = Query(None, description="", alias="balance_free_max"),
    balance_staked_min: Optional[StrictStr] = Query(None, description="", alias="balance_staked_min"),
    balance_staked_max: Optional[StrictStr] = Query(None, description="", alias="balance_staked_max"),
    balance_staked_root_min: Optional[StrictStr] = Query(None, description="", alias="balance_staked_root_min"),
    balance_staked_root_max: Optional[StrictStr] = Query(None, description="", alias="balance_staked_root_max"),
    balance_staked_alpha_as_tao_min: Optional[StrictStr] = Query(None, description="", alias="balance_staked_alpha_as_tao_min"),
    balance_staked_alpha_as_tao_max: Optional[StrictStr] = Query(None, description="", alias="balance_staked_alpha_as_tao_max"),
    balance_total_min: Optional[StrictStr] = Query(None, description="", alias="balance_total_min"),
    balance_total_max: Optional[StrictStr] = Query(None, description="", alias="balance_total_max"),
    rank: Optional[int] = Query(None, description="", alias="rank"),
    created_on_network: Annotated[Optional[StrictStr], Field(description="finney, nakamoto, kusanagi")] = Query(None, description="finney, nakamoto, kusanagi", alias="created_on_network"),
    created_on_timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="created_on_timestamp_start"),
    created_on_timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="created_on_timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[AccountOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> AccountResponse:
    if not BaseAccountApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAccountApi.subclasses[0]().get_account_latest(address, balance_free_min, balance_free_max, balance_staked_min, balance_staked_max, balance_staked_root_min, balance_staked_root_max, balance_staked_alpha_as_tao_min, balance_staked_alpha_as_tao_max, balance_total_min, balance_total_max, rank, created_on_network, created_on_timestamp_start, created_on_timestamp_end, page, limit, order)
