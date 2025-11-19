# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.stake_balance_api_base import BaseStakeBalanceApi
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
from openapi_server.models.stake_balance_history_order import StakeBalanceHistoryOrder
from openapi_server.models.stake_balance_response import StakeBalanceResponse
from openapi_server.security_api import get_token_api_key

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/stake_balance/history/v1",
    responses={
        200: {"model": StakeBalanceResponse, "description": "Stake balances retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Stake balances not found"},
        500: {"description": "Internal server error"},
    },
    tags=["stake_balance"],
    response_model_by_alias=True,
)
async def get_stake_balance_history(
    coldkey: Annotated[StrictStr, Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="coldkey"),
    hotkey: Annotated[StrictStr, Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="hotkey"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[StakeBalanceHistoryOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> StakeBalanceResponse:
    if not BaseStakeBalanceApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseStakeBalanceApi.subclasses[0]().get_stake_balance_history(coldkey, hotkey, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)
