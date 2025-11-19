# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.neuron_api_base import BaseNeuronApi
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
from openapi_server.models.neuron_aggregated_history_order import NeuronAggregatedHistoryOrder
from openapi_server.models.neuron_aggregated_latest_order import NeuronAggregatedLatestOrder
from openapi_server.models.neuron_aggregated_response import NeuronAggregatedResponse
from openapi_server.models.neuron_history_order import NeuronHistoryOrder
from openapi_server.models.neuron_incentive_distribution_response import NeuronIncentiveDistributionResponse
from openapi_server.models.neuron_latest_order import NeuronLatestOrder
from openapi_server.models.neuron_response import NeuronResponse
from openapi_server.security_api import get_token_api_key

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/neuron/aggregated/history/v1",
    responses={
        200: {"model": NeuronAggregatedResponse, "description": "Neuron history retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Neuron history not found"},
        500: {"description": "Internal server error"},
    },
    tags=["neuron"],
    response_model_by_alias=True,
)
async def get_neuron_aggregated_history(
    netuid: Annotated[Optional[int], Field(description="Subnet ID")] = Query(None, description="Subnet ID", alias="netuid"),
    block_start: Optional[int] = Query(None, description="", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[NeuronAggregatedHistoryOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> NeuronAggregatedResponse:
    if not BaseNeuronApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseNeuronApi.subclasses[0]().get_neuron_aggregated_history(netuid, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/neuron/aggregated/latest/v1",
    responses={
        200: {"model": NeuronAggregatedResponse, "description": "Neuron retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Neuron not found"},
        500: {"description": "Internal server error"},
    },
    tags=["neuron"],
    response_model_by_alias=True,
)
async def get_neuron_aggregated_latest(
    netuid: Annotated[Optional[int], Field(description="Subnet ID")] = Query(None, description="Subnet ID", alias="netuid"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[NeuronAggregatedLatestOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> NeuronAggregatedResponse:
    if not BaseNeuronApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseNeuronApi.subclasses[0]().get_neuron_aggregated_latest(netuid, page, limit, order)


@router.get(
    "/api/neuron/history/v1",
    responses={
        200: {"model": NeuronResponse, "description": "Neuron history retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Neuron history not found"},
        500: {"description": "Internal server error"},
    },
    tags=["neuron"],
    response_model_by_alias=True,
)
async def get_neuron_history(
    netuid: Annotated[Optional[int], Field(description="Subnet ID")] = Query(None, description="Subnet ID", alias="netuid"),
    uid: Annotated[Optional[int], Field(description="Neuron ID")] = Query(None, description="Neuron ID", alias="uid"),
    hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="hotkey"),
    coldkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="coldkey"),
    is_immune: Annotated[Optional[StrictBool], Field(description="Start of block range (inclusive) Is immune")] = Query(None, description="Start of block range (inclusive) Is immune", alias="is_immune"),
    in_danger: Annotated[Optional[StrictBool], Field(description="Is in danger")] = Query(None, description="Is in danger", alias="in_danger"),
    has_dividends: Annotated[Optional[StrictBool], Field(description="Has dividends")] = Query(None, description="Has dividends", alias="has_dividends"),
    has_incentive: Annotated[Optional[StrictBool], Field(description="Has incentive")] = Query(None, description="Has incentive", alias="has_incentive"),
    block_start: Optional[int] = Query(None, description="", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[NeuronHistoryOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> NeuronResponse:
    if not BaseNeuronApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseNeuronApi.subclasses[0]().get_neuron_history(netuid, uid, hotkey, coldkey, is_immune, in_danger, has_dividends, has_incentive, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/neuron/incentive_distribution/v1",
    responses={
        200: {"model": NeuronIncentiveDistributionResponse, "description": "Neuron history retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Neuron history not found"},
        500: {"description": "Internal server error"},
    },
    tags=["neuron"],
    response_model_by_alias=True,
)
async def get_neuron_incentive_distribution(
    netuid: Annotated[int, Field(description="Subnet ID")] = Query(None, description="Subnet ID", alias="netuid"),
    days: Annotated[int, Field(description="Integer between 1 and 7")] = Query(None, description="Integer between 1 and 7", alias="days"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> NeuronIncentiveDistributionResponse:
    if not BaseNeuronApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseNeuronApi.subclasses[0]().get_neuron_incentive_distribution(netuid, days)


@router.get(
    "/api/neuron/latest/v1",
    responses={
        200: {"model": NeuronResponse, "description": "Neuron retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Neuron not found"},
        500: {"description": "Internal server error"},
    },
    tags=["neuron"],
    response_model_by_alias=True,
)
async def get_neuron_latest(
    netuid: Annotated[Optional[int], Field(description="Subnet ID")] = Query(None, description="Subnet ID", alias="netuid"),
    uid: Annotated[Optional[int], Field(description="Neuron ID")] = Query(None, description="Neuron ID", alias="uid"),
    hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="hotkey"),
    coldkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="coldkey"),
    is_immune: Annotated[Optional[StrictBool], Field(description="Start of block range (inclusive) Is immune")] = Query(None, description="Start of block range (inclusive) Is immune", alias="is_immune"),
    in_danger: Annotated[Optional[StrictBool], Field(description="Is in danger")] = Query(None, description="Is in danger", alias="in_danger"),
    has_dividends: Annotated[Optional[StrictBool], Field(description="Has dividends")] = Query(None, description="Has dividends", alias="has_dividends"),
    has_incentive: Annotated[Optional[StrictBool], Field(description="Has incentive")] = Query(None, description="Has incentive", alias="has_incentive"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[NeuronLatestOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> NeuronResponse:
    if not BaseNeuronApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseNeuronApi.subclasses[0]().get_neuron_latest(netuid, uid, hotkey, coldkey, is_immune, in_danger, has_dividends, has_incentive, page, limit, order)
