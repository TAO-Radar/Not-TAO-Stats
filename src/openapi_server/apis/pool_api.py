# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.pool_api_base import BasePoolApi
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
from pydantic import Field
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.dtao_pool_history_order import DtaoPoolHistoryOrder
from openapi_server.models.dtao_pool_history_response import DtaoPoolHistoryResponse
from openapi_server.models.dtao_pool_order import DtaoPoolOrder
from openapi_server.models.dtao_pool_response import DtaoPoolResponse
from openapi_server.models.dtao_pool_total_price_history_order import DtaoPoolTotalPriceHistoryOrder
from openapi_server.models.dtao_pool_total_price_history_response import DtaoPoolTotalPriceHistoryResponse
from openapi_server.models.dtao_pool_total_price_latest_response import DtaoPoolTotalPriceLatestResponse
from openapi_server.models.frequency_block_hour_day import FrequencyBlockHourDay
from openapi_server.security_api import get_token_api_key

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/dtao/pool/history/v1",
    responses={
        200: {"model": DtaoPoolHistoryResponse, "description": "Dtao pools retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Dtao pools not found"},
        500: {"description": "Internal server error"},
    },
    tags=["pool"],
    response_model_by_alias=True,
)
async def get_dtao_pool_history(
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    frequency: Optional[FrequencyBlockHourDay] = Query(None, description="", alias="frequency"),
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[DtaoPoolHistoryOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoPoolHistoryResponse:
    if not BasePoolApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePoolApi.subclasses[0]().get_dtao_pool_history(netuid, frequency, block_number, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/dtao/pool/latest/v1",
    responses={
        200: {"model": DtaoPoolResponse, "description": "Dtao pools retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Dtao pools not found"},
        500: {"description": "Internal server error"},
    },
    tags=["pool"],
    response_model_by_alias=True,
)
async def get_dtao_pool_latest(
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[DtaoPoolOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoPoolResponse:
    if not BasePoolApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePoolApi.subclasses[0]().get_dtao_pool_latest(netuid, page, limit, order)


@router.get(
    "/api/dtao/pool/total_price/history/v1",
    responses={
        200: {"model": DtaoPoolTotalPriceHistoryResponse, "description": "Pool total price retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Pool total price not found"},
        500: {"description": "Internal server error"},
    },
    tags=["pool"],
    response_model_by_alias=True,
)
async def get_dtao_pool_total_price_history(
    frequency: Optional[FrequencyBlockHourDay] = Query(None, description="", alias="frequency"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[DtaoPoolTotalPriceHistoryOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoPoolTotalPriceHistoryResponse:
    if not BasePoolApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePoolApi.subclasses[0]().get_dtao_pool_total_price_history(frequency, page, limit, order)


@router.get(
    "/api/dtao/pool/total_price/latest/v1",
    responses={
        200: {"model": DtaoPoolTotalPriceLatestResponse, "description": "Pool total price retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Pool total price not found"},
        500: {"description": "Internal server error"},
    },
    tags=["pool"],
    response_model_by_alias=True,
)
async def get_dtao_pool_total_price_latest(
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoPoolTotalPriceLatestResponse:
    if not BasePoolApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePoolApi.subclasses[0]().get_dtao_pool_total_price_latest()


@router.get(
    "/api/dtao/pool/total_price/v1",
    responses={
        200: {"model": DtaoPoolTotalPriceHistoryResponse, "description": "Pool total price retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Pool total price not found"},
        500: {"description": "Internal server error"},
    },
    tags=["pool"],
    response_model_by_alias=True,
)
async def get_dtao_pool_total_price(
    frequency: Optional[FrequencyBlockHourDay] = Query(None, description="", alias="frequency"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[DtaoPoolTotalPriceHistoryOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoPoolTotalPriceHistoryResponse:
    if not BasePoolApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePoolApi.subclasses[0]().get_dtao_pool_total_price(frequency, page, limit, order)


@router.get(
    "/api/dtao/pool/v1",
    responses={
        200: {"model": DtaoPoolResponse, "description": "Dtao pools retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Dtao pools not found"},
        500: {"description": "Internal server error"},
    },
    tags=["pool"],
    response_model_by_alias=True,
)
async def get_dtao_pool(
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[DtaoPoolOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoPoolResponse:
    if not BasePoolApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePoolApi.subclasses[0]().get_dtao_pool(netuid, page, limit, order)
