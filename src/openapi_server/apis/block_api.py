# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.block_api_base import BaseBlockApi
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
from openapi_server.models.block_emission_order import BlockEmissionOrder
from openapi_server.models.block_emission_response import BlockEmissionResponse
from openapi_server.models.block_interval_order import BlockIntervalOrder
from openapi_server.models.block_interval_response import BlockIntervalResponse
from openapi_server.models.block_order import BlockOrder
from openapi_server.models.block_response import BlockResponse
from openapi_server.models.frequency_hour_day import FrequencyHourDay
from openapi_server.security_api import get_token_api_key

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/block/emission/v1",
    responses={
        200: {"model": BlockEmissionResponse, "description": "Blocks retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Blocks not found"},
        500: {"description": "Internal server error"},
    },
    tags=["block"],
    response_model_by_alias=True,
)
async def get_block_emission(
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[BlockEmissionOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> BlockEmissionResponse:
    if not BaseBlockApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseBlockApi.subclasses[0]().get_block_emission(block_number, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/block/interval/v1",
    responses={
        200: {"model": BlockIntervalResponse, "description": "Blocks retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Blocks not found"},
        500: {"description": "Internal server error"},
    },
    tags=["block"],
    response_model_by_alias=True,
)
async def get_block_interval(
    timestamp_start: Annotated[int, Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[int, Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    frequency: Annotated[Optional[FrequencyHourDay], Field(description="Default by_day")] = Query(None, description="Default by_day", alias="frequency"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[BlockIntervalOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> BlockIntervalResponse:
    if not BaseBlockApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseBlockApi.subclasses[0]().get_block_interval(timestamp_start, timestamp_end, frequency, page, limit, order)


@router.get(
    "/api/block/v1",
    responses={
        200: {"model": BlockResponse, "description": "Blocks retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Blocks not found"},
        500: {"description": "Internal server error"},
    },
    tags=["block"],
    response_model_by_alias=True,
)
async def get_block(
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    hash: Optional[StrictStr] = Query(None, description="", alias="hash"),
    spec_version: Optional[int] = Query(None, description="", alias="spec_version"),
    validator: Optional[StrictStr] = Query(None, description="", alias="validator"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[BlockOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> BlockResponse:
    if not BaseBlockApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseBlockApi.subclasses[0]().get_block(block_number, block_start, block_end, timestamp_start, timestamp_end, hash, spec_version, validator, page, limit, order)
