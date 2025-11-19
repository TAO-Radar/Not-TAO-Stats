# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.metagraph_api_base import BaseMetagraphApi
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
from openapi_server.models.metagraph_history_order import MetagraphHistoryOrder
from openapi_server.models.metagraph_history_response import MetagraphHistoryResponse
from openapi_server.models.metagraph_order import MetagraphOrder
from openapi_server.models.metagraph_response import MetagraphResponse
from openapi_server.models.root_metagraph_history_order import RootMetagraphHistoryOrder
from openapi_server.models.root_metagraph_history_response import RootMetagraphHistoryResponse
from openapi_server.models.root_metagraph_order import RootMetagraphOrder
from openapi_server.models.root_metagraph_response import RootMetagraphResponse
from openapi_server.security_api import get_token_api_key

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/metagraph/history/v1",
    responses={
        200: {"model": MetagraphHistoryResponse, "description": "Metagraph history retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Metagraph history not found"},
        500: {"description": "Internal server error"},
    },
    tags=["metagraph"],
    response_model_by_alias=True,
)
async def get_metagraph_history(
    netuid: Annotated[Optional[int], Field(description="Subnet ID")] = Query(None, description="Subnet ID", alias="netuid"),
    uid: Annotated[Optional[int], Field(description="Neuron ID")] = Query(None, description="Neuron ID", alias="uid"),
    hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="hotkey"),
    coldkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="coldkey"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[MetagraphHistoryOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> MetagraphHistoryResponse:
    if not BaseMetagraphApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMetagraphApi.subclasses[0]().get_metagraph_history(netuid, uid, hotkey, coldkey, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/metagraph/latest/v1",
    responses={
        200: {"model": MetagraphResponse, "description": "Metagraph retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Metagraph not found"},
        500: {"description": "Internal server error"},
    },
    tags=["metagraph"],
    response_model_by_alias=True,
)
async def get_metagraph_latest(
    netuid: Annotated[Optional[int], Field(description="Subnet ID")] = Query(None, description="Subnet ID", alias="netuid"),
    search: Annotated[Optional[StrictStr], Field(description="Search across UID, hotkey, coldkey, axon_ip")] = Query(None, description="Search across UID, hotkey, coldkey, axon_ip", alias="search"),
    uid: Annotated[Optional[int], Field(description="Neuron ID")] = Query(None, description="Neuron ID", alias="uid"),
    active: Optional[StrictBool] = Query(None, description="", alias="active"),
    hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="hotkey"),
    coldkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="coldkey"),
    validator_permit: Optional[StrictBool] = Query(None, description="", alias="validator_permit"),
    is_immunity_period: Optional[StrictBool] = Query(None, description="", alias="is_immunity_period"),
    is_child_key: Optional[StrictBool] = Query(None, description="", alias="is_child_key"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[MetagraphOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> MetagraphResponse:
    if not BaseMetagraphApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMetagraphApi.subclasses[0]().get_metagraph_latest(netuid, search, uid, active, hotkey, coldkey, validator_permit, is_immunity_period, is_child_key, page, limit, order)


@router.get(
    "/api/metagraph/root/history/v1",
    responses={
        200: {"model": RootMetagraphHistoryResponse, "description": "Metagraph history retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Metagraph history not found"},
        500: {"description": "Internal server error"},
    },
    tags=["metagraph"],
    response_model_by_alias=True,
)
async def get_metagraph_root_history(
    hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="hotkey"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[RootMetagraphHistoryOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> RootMetagraphHistoryResponse:
    if not BaseMetagraphApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMetagraphApi.subclasses[0]().get_metagraph_root_history(hotkey, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/metagraph/root/latest/v1",
    responses={
        200: {"model": RootMetagraphResponse, "description": "Metagraph retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Metagraph not found"},
        500: {"description": "Internal server error"},
    },
    tags=["metagraph"],
    response_model_by_alias=True,
)
async def get_metagraph_root_latest(
    hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="hotkey"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[RootMetagraphOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> RootMetagraphResponse:
    if not BaseMetagraphApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMetagraphApi.subclasses[0]().get_metagraph_root_latest(hotkey, page, limit, order)
