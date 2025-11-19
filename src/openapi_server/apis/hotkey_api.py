# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.hotkey_api_base import BaseHotkeyApi
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
from openapi_server.models.hotkey_family_history_order import HotkeyFamilyHistoryOrder
from openapi_server.models.hotkey_family_response import HotkeyFamilyResponse
from openapi_server.security_api import get_token_api_key

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/hotkey/family/history/v1",
    responses={
        200: {"model": HotkeyFamilyResponse, "description": "Hotkey family history retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Hotkey not found"},
        500: {"description": "Internal server error"},
    },
    tags=["hotkey"],
    response_model_by_alias=True,
)
async def get_hotkey_family_history(
    hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex formatted public key")] = Query(None, description="SS58 or hex formatted public key", alias="hotkey"),
    netuid: Annotated[Optional[int], Field(description="Subnet ID")] = Query(None, description="Subnet ID", alias="netuid"),
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[HotkeyFamilyHistoryOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> HotkeyFamilyResponse:
    if not BaseHotkeyApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseHotkeyApi.subclasses[0]().get_hotkey_family_history(hotkey, netuid, block_number, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/hotkey/family/latest/v1",
    responses={
        200: {"model": HotkeyFamilyResponse, "description": "Hotkey family retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Hotkey not found"},
        500: {"description": "Internal server error"},
    },
    tags=["hotkey"],
    response_model_by_alias=True,
)
async def get_hotkey_family_latest(
    hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="hotkey"),
    netuid: Annotated[Optional[int], Field(description="Subnet ID")] = Query(None, description="Subnet ID", alias="netuid"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> HotkeyFamilyResponse:
    if not BaseHotkeyApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseHotkeyApi.subclasses[0]().get_hotkey_family_latest(hotkey, netuid, page, limit)
