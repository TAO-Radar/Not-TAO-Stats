# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.otc_api_base import BaseOtcApi
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
from pydantic import StrictStr
from typing import Any, Optional
from openapi_server.models.frozen_status import FrozenStatus
from openapi_server.models.listing_event_type import ListingEventType
from openapi_server.models.listing_status import ListingStatus
from openapi_server.models.offer_event_type import OfferEventType
from openapi_server.models.offer_status import OfferStatus
from openapi_server.models.otc_listing_history_order import OtcListingHistoryOrder
from openapi_server.models.otc_listing_history_response import OtcListingHistoryResponse
from openapi_server.models.otc_listing_order import OtcListingOrder
from openapi_server.models.otc_listing_response import OtcListingResponse
from openapi_server.models.otc_offer_history_order import OtcOfferHistoryOrder
from openapi_server.models.otc_offer_history_response import OtcOfferHistoryResponse
from openapi_server.models.otc_offer_order import OtcOfferOrder
from openapi_server.models.otc_offer_response import OtcOfferResponse
from openapi_server.models.otc_subnet_status_order import OtcSubnetStatusOrder
from openapi_server.models.otc_subnet_status_response import OtcSubnetStatusResponse
from openapi_server.models.otc_trade_order import OtcTradeOrder
from openapi_server.models.otc_trade_response import OtcTradeResponse
from openapi_server.models.otc_user_stats_order import OtcUserStatsOrder
from openapi_server.models.otc_user_stats_response import OtcUserStatsResponse
from openapi_server.models.trade_type import TradeType
from openapi_server.security_api import get_token_api_key

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/otc/listing/history/v1",
    responses={
        200: {"model": OtcListingHistoryResponse, "description": "Alpha listing history retrieved successfully"},
        400: {"description": "Bad request"},
        500: {"description": "Internal server error"},
    },
    tags=["otc"],
    response_model_by_alias=True,
)
async def get_otc_listing_history(
    listing_id: Optional[StrictStr] = Query(None, description="", alias="listing_id"),
    event_type: Optional[ListingEventType] = Query(None, description="", alias="event_type"),
    seller: Optional[StrictStr] = Query(None, description="", alias="seller"),
    buyer: Optional[StrictStr] = Query(None, description="", alias="buyer"),
    hotkey: Optional[StrictStr] = Query(None, description="", alias="hotkey"),
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    block_start: Optional[int] = Query(None, description="", alias="block_start"),
    block_end: Optional[int] = Query(None, description="", alias="block_end"),
    timestamp_start: Optional[int] = Query(None, description="", alias="timestamp_start"),
    timestamp_end: Optional[int] = Query(None, description="", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[OtcListingHistoryOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> OtcListingHistoryResponse:
    if not BaseOtcApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseOtcApi.subclasses[0]().get_otc_listing_history(listing_id, event_type, seller, buyer, hotkey, netuid, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/otc/listing/v1",
    responses={
        200: {"model": OtcListingResponse, "description": "Alpha listings retrieved successfully"},
        400: {"description": "Bad request"},
        500: {"description": "Internal server error"},
    },
    tags=["otc"],
    response_model_by_alias=True,
)
async def get_otc_listing(
    listing_id: Optional[StrictStr] = Query(None, description="", alias="listing_id"),
    seller: Optional[StrictStr] = Query(None, description="", alias="seller"),
    hotkey: Optional[StrictStr] = Query(None, description="", alias="hotkey"),
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    status: Optional[ListingStatus] = Query(None, description="", alias="status"),
    price_min: Optional[StrictStr] = Query(None, description="", alias="price_min"),
    price_max: Optional[StrictStr] = Query(None, description="", alias="price_max"),
    amount_min: Optional[StrictStr] = Query(None, description="", alias="amount_min"),
    amount_max: Optional[StrictStr] = Query(None, description="", alias="amount_max"),
    created_block_start: Optional[int] = Query(None, description="", alias="created_block_start"),
    created_block_end: Optional[int] = Query(None, description="", alias="created_block_end"),
    created_timestamp_start: Optional[int] = Query(None, description="", alias="created_timestamp_start"),
    created_timestamp_end: Optional[int] = Query(None, description="", alias="created_timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[OtcListingOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> OtcListingResponse:
    if not BaseOtcApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseOtcApi.subclasses[0]().get_otc_listing(listing_id, seller, hotkey, netuid, status, price_min, price_max, amount_min, amount_max, created_block_start, created_block_end, created_timestamp_start, created_timestamp_end, page, limit, order)


@router.get(
    "/api/otc/offer/history/v1",
    responses={
        200: {"model": OtcOfferHistoryResponse, "description": "TAO offer history retrieved successfully"},
        400: {"description": "Bad request"},
        500: {"description": "Internal server error"},
    },
    tags=["otc"],
    response_model_by_alias=True,
)
async def get_otc_offer_history(
    offer_id: Optional[StrictStr] = Query(None, description="", alias="offer_id"),
    event_type: Optional[OfferEventType] = Query(None, description="", alias="event_type"),
    buyer: Optional[StrictStr] = Query(None, description="", alias="buyer"),
    seller: Optional[StrictStr] = Query(None, description="", alias="seller"),
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    block_start: Optional[int] = Query(None, description="", alias="block_start"),
    block_end: Optional[int] = Query(None, description="", alias="block_end"),
    timestamp_start: Optional[int] = Query(None, description="", alias="timestamp_start"),
    timestamp_end: Optional[int] = Query(None, description="", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[OtcOfferHistoryOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> OtcOfferHistoryResponse:
    if not BaseOtcApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseOtcApi.subclasses[0]().get_otc_offer_history(offer_id, event_type, buyer, seller, netuid, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/otc/offer/v1",
    responses={
        200: {"model": OtcOfferResponse, "description": "TAO offers retrieved successfully"},
        400: {"description": "Bad request"},
        500: {"description": "Internal server error"},
    },
    tags=["otc"],
    response_model_by_alias=True,
)
async def get_otc_offer(
    offer_id: Optional[StrictStr] = Query(None, description="", alias="offer_id"),
    buyer: Optional[StrictStr] = Query(None, description="", alias="buyer"),
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    status: Optional[OfferStatus] = Query(None, description="", alias="status"),
    price_min: Optional[StrictStr] = Query(None, description="", alias="price_min"),
    price_max: Optional[StrictStr] = Query(None, description="", alias="price_max"),
    amount_min: Optional[StrictStr] = Query(None, description="", alias="amount_min"),
    amount_max: Optional[StrictStr] = Query(None, description="", alias="amount_max"),
    created_block_start: Optional[int] = Query(None, description="", alias="created_block_start"),
    created_block_end: Optional[int] = Query(None, description="", alias="created_block_end"),
    created_timestamp_start: Optional[int] = Query(None, description="", alias="created_timestamp_start"),
    created_timestamp_end: Optional[int] = Query(None, description="", alias="created_timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[OtcOfferOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> OtcOfferResponse:
    if not BaseOtcApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseOtcApi.subclasses[0]().get_otc_offer(offer_id, buyer, netuid, status, price_min, price_max, amount_min, amount_max, created_block_start, created_block_end, created_timestamp_start, created_timestamp_end, page, limit, order)


@router.get(
    "/api/otc/subnet/status/v1",
    responses={
        200: {"model": OtcSubnetStatusResponse, "description": "Subnet status retrieved successfully"},
        400: {"description": "Bad request"},
        500: {"description": "Internal server error"},
    },
    tags=["otc"],
    response_model_by_alias=True,
)
async def get_otc_subnet_status(
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    frozen: Optional[FrozenStatus] = Query(None, description="", alias="frozen"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[OtcSubnetStatusOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> OtcSubnetStatusResponse:
    if not BaseOtcApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseOtcApi.subclasses[0]().get_otc_subnet_status(netuid, frozen, page, limit, order)


@router.get(
    "/api/otc/trade/v1",
    responses={
        200: {"model": OtcTradeResponse, "description": "OTC trades retrieved successfully"},
        400: {"description": "Bad request"},
        500: {"description": "Internal server error"},
    },
    tags=["otc"],
    response_model_by_alias=True,
)
async def get_otc_trade(
    trade_type: Optional[TradeType] = Query(None, description="", alias="trade_type"),
    seller: Optional[StrictStr] = Query(None, description="", alias="seller"),
    buyer: Optional[StrictStr] = Query(None, description="", alias="buyer"),
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    listing_id: Optional[StrictStr] = Query(None, description="", alias="listing_id"),
    offer_id: Optional[StrictStr] = Query(None, description="", alias="offer_id"),
    block_start: Optional[int] = Query(None, description="", alias="block_start"),
    block_end: Optional[int] = Query(None, description="", alias="block_end"),
    timestamp_start: Optional[int] = Query(None, description="", alias="timestamp_start"),
    timestamp_end: Optional[int] = Query(None, description="", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[OtcTradeOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> OtcTradeResponse:
    if not BaseOtcApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseOtcApi.subclasses[0]().get_otc_trade(trade_type, seller, buyer, netuid, listing_id, offer_id, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/otc/user/stats/v1",
    responses={
        200: {"model": OtcUserStatsResponse, "description": "User statistics retrieved successfully"},
        400: {"description": "Bad request"},
        500: {"description": "Internal server error"},
    },
    tags=["otc"],
    response_model_by_alias=True,
)
async def get_otc_user_stats(
    account: Optional[StrictStr] = Query(None, description="", alias="account"),
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[OtcUserStatsOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> OtcUserStatsResponse:
    if not BaseOtcApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseOtcApi.subclasses[0]().get_otc_user_stats(account, netuid, page, limit, order)
