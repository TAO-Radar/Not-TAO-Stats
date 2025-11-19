# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.runtime_version_api_base import BaseRuntimeVersionApi
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
from openapi_server.models.runtime_version_history_order import RuntimeVersionHistoryOrder
from openapi_server.models.runtime_version_response import RuntimeVersionResponse
from openapi_server.security_api import get_token_api_key

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/runtime_version/history/v1",
    responses={
        200: {"model": RuntimeVersionResponse, "description": "Runtime version history retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Runtime version history not found"},
        500: {"description": "Internal server error"},
    },
    tags=["runtime_version"],
    response_model_by_alias=True,
)
async def get_runtime_version_history(
    block_start: Optional[int] = Query(None, description="", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[RuntimeVersionHistoryOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> RuntimeVersionResponse:
    if not BaseRuntimeVersionApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseRuntimeVersionApi.subclasses[0]().get_runtime_version_history(block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/runtime_version/latest/v1",
    responses={
        200: {"model": RuntimeVersionResponse, "description": "Runtime version retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Runtime version not found"},
        500: {"description": "Internal server error"},
    },
    tags=["runtime_version"],
    response_model_by_alias=True,
)
async def get_runtime_version_latest(
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> RuntimeVersionResponse:
    if not BaseRuntimeVersionApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseRuntimeVersionApi.subclasses[0]().get_runtime_version_latest()
