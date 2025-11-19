# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.coingecko_api_base import BaseCoingeckoApi
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
from typing import Any
from typing_extensions import Annotated
from openapi_server.models.coin_gecko_asset_response import CoinGeckoAssetResponse
from openapi_server.models.coin_gecko_events_response import CoinGeckoEventsResponse
from openapi_server.models.coin_gecko_latest_block_response import CoinGeckoLatestBlockResponse
from openapi_server.models.coin_gecko_pair_response import CoinGeckoPairResponse
from openapi_server.security_api import get_token_api_key

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/coingecko/asset",
    responses={
        200: {"model": CoinGeckoAssetResponse, "description": "Asset retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Asset not found"},
        500: {"description": "Internal server error"},
    },
    tags=["coingecko"],
    response_model_by_alias=True,
)
async def get_coingecko_asset(
    id: Annotated[StrictStr, Field(description="integer")] = Query(None, description="integer", alias="id"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> CoinGeckoAssetResponse:
    if not BaseCoingeckoApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCoingeckoApi.subclasses[0]().get_coingecko_asset(id)


@router.get(
    "/api/coingecko/events",
    responses={
        200: {"model": CoinGeckoEventsResponse, "description": "Events retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Events not found"},
        500: {"description": "Internal server error"},
    },
    tags=["coingecko"],
    response_model_by_alias=True,
)
async def get_coingecko_events(
    from_block: int = Query(None, description="", alias="fromBlock"),
    to_block: int = Query(None, description="", alias="toBlock"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> CoinGeckoEventsResponse:
    if not BaseCoingeckoApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCoingeckoApi.subclasses[0]().get_coingecko_events(from_block, to_block)


@router.get(
    "/api/coingecko/latest-block",
    responses={
        200: {"model": CoinGeckoLatestBlockResponse, "description": "Latest block retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Latest block not found"},
        500: {"description": "Internal server error"},
    },
    tags=["coingecko"],
    response_model_by_alias=True,
)
async def get_coingecko_latest_block(
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> CoinGeckoLatestBlockResponse:
    if not BaseCoingeckoApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCoingeckoApi.subclasses[0]().get_coingecko_latest_block()


@router.get(
    "/api/coingecko/pair",
    responses={
        200: {"model": CoinGeckoPairResponse, "description": "Pair retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Pair not found"},
        500: {"description": "Internal server error"},
    },
    tags=["coingecko"],
    response_model_by_alias=True,
)
async def get_coingecko_pair(
    id: StrictStr = Query(None, description="", alias="id"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> CoinGeckoPairResponse:
    if not BaseCoingeckoApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCoingeckoApi.subclasses[0]().get_coingecko_pair(id)
