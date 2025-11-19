# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.trades_api_base import BaseTradesApi
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
from openapi_server.models.dtao_trade_order import DtaoTradeOrder
from openapi_server.models.dtao_trade_response import DtaoTradeResponse
from openapi_server.security_api import get_token_api_key

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/dtao/trade/v1",
    responses={
        200: {"model": DtaoTradeResponse, "description": "Dtao trades retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Dtao trades not found"},
        500: {"description": "Internal server error"},
    },
    tags=["trades"],
    response_model_by_alias=True,
)
async def get_dtao_trade(
    coldkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="coldkey"),
    extrinsic_id: Optional[StrictStr] = Query(None, description="", alias="extrinsic_id"),
    from_name: Optional[StrictStr] = Query(None, description="", alias="from_name"),
    to_name: Optional[StrictStr] = Query(None, description="", alias="to_name"),
    tao_value_min: Annotated[Optional[StrictStr], Field(description="Minimum amount (inclusive)")] = Query(None, description="Minimum amount (inclusive)", alias="tao_value_min"),
    tao_value_max: Annotated[Optional[StrictStr], Field(description="Maximum amount (inclusive)")] = Query(None, description="Maximum amount (inclusive)", alias="tao_value_max"),
    usd_value_min: Annotated[Optional[StrictStr], Field(description="Minimum amount (inclusive)")] = Query(None, description="Minimum amount (inclusive)", alias="usd_value_min"),
    usd_value_max: Annotated[Optional[StrictStr], Field(description="Maximum amount (inclusive)")] = Query(None, description="Maximum amount (inclusive)", alias="usd_value_max"),
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[DtaoTradeOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoTradeResponse:
    if not BaseTradesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTradesApi.subclasses[0]().get_dtao_trade(coldkey, extrinsic_id, from_name, to_name, tao_value_min, tao_value_max, usd_value_min, usd_value_max, block_number, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)
