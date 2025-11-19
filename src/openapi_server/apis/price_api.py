# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.price_api_base import BasePriceApi
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
from openapi_server.models.price_history_order import PriceHistoryOrder
from openapi_server.models.price_ohlc_period import PriceOHLCPeriod
from openapi_server.models.price_ohlc_response import PriceOHLCResponse
from openapi_server.models.price_response import PriceResponse
from openapi_server.models.price_simple_response import PriceSimpleResponse
from openapi_server.security_api import get_token_api_key

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/price/history/v1",
    responses={
        200: {"model": PriceResponse, "description": "Prices retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Prices not found"},
        500: {"description": "Internal server error"},
    },
    tags=["price"],
    response_model_by_alias=True,
)
async def get_price_history(
    asset: StrictStr = Query(None, description="", alias="asset"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[PriceHistoryOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> PriceResponse:
    if not BasePriceApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePriceApi.subclasses[0]().get_price_history(asset, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/price/latest/v1",
    responses={
        200: {"model": PriceResponse, "description": "Price retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Price not found"},
        500: {"description": "Internal server error"},
    },
    tags=["price"],
    response_model_by_alias=True,
)
async def get_price_latest(
    asset: StrictStr = Query(None, description="", alias="asset"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> PriceResponse:
    if not BasePriceApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePriceApi.subclasses[0]().get_price_latest(asset)


@router.get(
    "/api/price/ohlc/v1",
    responses={
        200: {"model": PriceOHLCResponse, "description": "Price OHLCs retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Price OHLCs not found"},
        500: {"description": "Internal server error"},
    },
    tags=["price"],
    response_model_by_alias=True,
)
async def get_price_ohlc(
    asset: StrictStr = Query(None, description="", alias="asset"),
    period: PriceOHLCPeriod = Query(None, description="", alias="period"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> PriceOHLCResponse:
    if not BasePriceApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePriceApi.subclasses[0]().get_price_ohlc(asset, period, timestamp_start, timestamp_end, page, limit)


@router.get(
    "/api/price/simple/latest/v1",
    responses={
        200: {"model": PriceSimpleResponse, "description": "Price retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Price not found"},
        500: {"description": "Internal server error"},
    },
    tags=["price"],
    response_model_by_alias=True,
)
async def get_price_simple_latest(
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> PriceSimpleResponse:
    if not BasePriceApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePriceApi.subclasses[0]().get_price_simple_latest()
