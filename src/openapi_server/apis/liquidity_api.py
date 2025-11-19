# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.liquidity_api_base import BaseLiquidityApi
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
from pydantic import Field, StrictBool, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.dtao_liquidity_distribution_response import DtaoLiquidityDistributionResponse
from openapi_server.models.dtao_liquidity_position_event_order import DtaoLiquidityPositionEventOrder
from openapi_server.models.dtao_liquidity_position_event_response import DtaoLiquidityPositionEventResponse
from openapi_server.models.dtao_liquidity_position_history_order import DtaoLiquidityPositionHistoryOrder
from openapi_server.models.dtao_liquidity_position_history_response import DtaoLiquidityPositionHistoryResponse
from openapi_server.models.dtao_liquidity_position_order import DtaoLiquidityPositionOrder
from openapi_server.models.dtao_liquidity_position_response import DtaoLiquidityPositionResponse
from openapi_server.models.dtao_tick_to_price_response import DtaoTickToPriceResponse
from openapi_server.models.liquidity_position_status import LiquidityPositionStatus
from openapi_server.models.liquidity_position_type import LiquidityPositionType
from openapi_server.security_api import get_token_api_key

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/dtao/liquidity/distribution/v1",
    responses={
        200: {"model": DtaoLiquidityDistributionResponse, "description": "Active liquidity distribution data retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "No liquidity data found for netuid"},
        500: {"description": "Internal server error"},
    },
    tags=["liquidity"],
    response_model_by_alias=True,
)
async def get_dtao_liquidity_distribution(
    netuid: int = Query(None, description="", alias="netuid"),
    min_price: Optional[StrictStr] = Query(None, description="", alias="min_price"),
    max_price: Optional[StrictStr] = Query(None, description="", alias="max_price"),
    num_points: Annotated[Optional[int], Field(description="Number of data points to return (default: 200, max: 1000)")] = Query(None, description="Number of data points to return (default: 200, max: 1000)", alias="num_points"),
    log_scale: Annotated[Optional[StrictBool], Field(description="Use logarithmic scale for price distribution (default: true)")] = Query(None, description="Use logarithmic scale for price distribution (default: true)", alias="log_scale"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoLiquidityDistributionResponse:
    if not BaseLiquidityApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLiquidityApi.subclasses[0]().get_dtao_liquidity_distribution(netuid, min_price, max_price, num_points, log_scale)


@router.get(
    "/api/dtao/liquidity/position/history/v1",
    responses={
        200: {"model": DtaoLiquidityPositionHistoryResponse, "description": "Liquidity position history retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Liquidity position history not found"},
        500: {"description": "Internal server error"},
    },
    tags=["liquidity"],
    response_model_by_alias=True,
)
async def get_dtao_liquidity_position_history(
    position_id: StrictStr = Query(None, description="", alias="position_id"),
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[DtaoLiquidityPositionHistoryOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoLiquidityPositionHistoryResponse:
    if not BaseLiquidityApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLiquidityApi.subclasses[0]().get_dtao_liquidity_position_history(position_id, block_number, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/dtao/liquidity/position/v1",
    responses={
        200: {"model": DtaoLiquidityPositionResponse, "description": "Liquidity positions retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Liquidity positions not found"},
        500: {"description": "Internal server error"},
    },
    tags=["liquidity"],
    response_model_by_alias=True,
)
async def get_dtao_liquidity_position(
    id: Optional[StrictStr] = Query(None, description="", alias="id"),
    coldkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="coldkey"),
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    status: Optional[LiquidityPositionStatus] = Query(None, description="", alias="status"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[DtaoLiquidityPositionOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoLiquidityPositionResponse:
    if not BaseLiquidityApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLiquidityApi.subclasses[0]().get_dtao_liquidity_position(id, coldkey, netuid, status, page, limit, order)


@router.get(
    "/api/dtao/liquidity/position_event/v1",
    responses={
        200: {"model": DtaoLiquidityPositionEventResponse, "description": "Liquidity position events retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Liquidity position events not found"},
        500: {"description": "Internal server error"},
    },
    tags=["liquidity"],
    response_model_by_alias=True,
)
async def get_dtao_liquidity_position_event(
    id: Optional[StrictStr] = Query(None, description="", alias="id"),
    position_id: Optional[StrictStr] = Query(None, description="", alias="position_id"),
    coldkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="coldkey"),
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    position_type: Optional[LiquidityPositionType] = Query(None, description="", alias="position_type"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[DtaoLiquidityPositionEventOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoLiquidityPositionEventResponse:
    if not BaseLiquidityApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLiquidityApi.subclasses[0]().get_dtao_liquidity_position_event(id, position_id, coldkey, netuid, position_type, page, limit, order)


@router.get(
    "/api/dtao/liquidity/tick_to_price/v1",
    responses={
        200: {"model": DtaoTickToPriceResponse, "description": "Tick prices retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Tick prices total price not found"},
        500: {"description": "Internal server error"},
    },
    tags=["liquidity"],
    response_model_by_alias=True,
)
async def get_dtao_liquidity_tick_to_price(
    tick: int = Query(None, description="", alias="tick"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoTickToPriceResponse:
    if not BaseLiquidityApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLiquidityApi.subclasses[0]().get_dtao_liquidity_tick_to_price(tick)
