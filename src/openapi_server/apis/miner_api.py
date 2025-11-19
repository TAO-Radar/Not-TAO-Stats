# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.miner_api_base import BaseMinerApi
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
from openapi_server.models.miner_autostake_order import MinerAutostakeOrder
from openapi_server.models.miner_autostake_response import MinerAutostakeResponse
from openapi_server.models.miner_coldkey_response import MinerColdkeyResponse
from openapi_server.models.miner_weights_history_order import MinerWeightsHistoryOrder
from openapi_server.models.miner_weights_latest_order import MinerWeightsLatestOrder
from openapi_server.models.miner_weights_response import MinerWeightsResponse
from openapi_server.security_api import get_token_api_key

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/miner/autostake/v1",
    responses={
        200: {"model": MinerAutostakeResponse, "description": "Miner autostake events retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Miner autostake events not found"},
        500: {"description": "Internal server error"},
    },
    tags=["miner"],
    response_model_by_alias=True,
)
async def get_miner_autostake(
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="hotkey"),
    coldkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="coldkey"),
    destination_hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="destination_hotkey"),
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[MinerAutostakeOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> MinerAutostakeResponse:
    if not BaseMinerApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMinerApi.subclasses[0]().get_miner_autostake(netuid, hotkey, coldkey, destination_hotkey, block_number, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/miner/coldkey/v1",
    responses={
        200: {"model": MinerColdkeyResponse, "description": "Miner coldkey retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Miner coldkey not found"},
        500: {"description": "Internal server error"},
    },
    tags=["miner"],
    response_model_by_alias=True,
)
async def get_miner_coldkey(
    coldkey: Annotated[StrictStr, Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="coldkey"),
    days: int = Query(None, description="", alias="days"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> MinerColdkeyResponse:
    if not BaseMinerApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMinerApi.subclasses[0]().get_miner_coldkey(coldkey, days)


@router.get(
    "/api/miner/weights/history/v1",
    responses={
        200: {"model": MinerWeightsResponse, "description": "Miner weights retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Miner weights not found"},
        500: {"description": "Internal server error"},
    },
    tags=["miner"],
    response_model_by_alias=True,
)
async def get_miner_weights_history(
    netuid: int = Query(None, description="", alias="netuid"),
    miner_uid: Optional[int] = Query(None, description="", alias="miner_uid"),
    validator_uid: Optional[int] = Query(None, description="", alias="validator_uid"),
    miner_hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="miner_hotkey"),
    validator_hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="validator_hotkey"),
    block_number: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[MinerWeightsHistoryOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> MinerWeightsResponse:
    if not BaseMinerApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMinerApi.subclasses[0]().get_miner_weights_history(netuid, miner_uid, validator_uid, miner_hotkey, validator_hotkey, block_number, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/miner/weights/latest/v1",
    responses={
        200: {"model": MinerWeightsResponse, "description": "Miner weights retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Miner weights not found"},
        500: {"description": "Internal server error"},
    },
    tags=["miner"],
    response_model_by_alias=True,
)
async def get_miner_weights_latest(
    netuid: int = Query(None, description="", alias="netuid"),
    miner_uid: Optional[int] = Query(None, description="", alias="miner_uid"),
    validator_uid: Optional[int] = Query(None, description="", alias="validator_uid"),
    miner_hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="miner_hotkey"),
    validator_hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="validator_hotkey"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[MinerWeightsLatestOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> MinerWeightsResponse:
    if not BaseMinerApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMinerApi.subclasses[0]().get_miner_weights_latest(netuid, miner_uid, validator_uid, miner_hotkey, validator_hotkey, page, limit, order)
