# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.subnet_api_base import BaseSubnetApi
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
from datetime import datetime
from pydantic import Field, StrictBool, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.frequency_block_hour_day import FrequencyBlockHourDay
from openapi_server.models.subnet_distribution_coldkey_response import SubnetDistributionColdkeyResponse
from openapi_server.models.subnet_distribution_ip_response import SubnetDistributionIPResponse
from openapi_server.models.subnet_distribution_incentive_response import SubnetDistributionIncentiveResponse
from openapi_server.models.subnet_history_order import SubnetHistoryOrder
from openapi_server.models.subnet_identity_response import SubnetIdentityResponse
from openapi_server.models.subnet_identity_set_order import SubnetIdentitySetOrder
from openapi_server.models.subnet_identity_set_response import SubnetIdentitySetResponse
from openapi_server.models.subnet_latest_response import SubnetLatestResponse
from openapi_server.models.subnet_metadata_response import SubnetMetadataResponse
from openapi_server.models.subnet_neuron_deregistration_order import SubnetNeuronDeregistrationOrder
from openapi_server.models.subnet_neuron_deregistration_response import SubnetNeuronDeregistrationResponse
from openapi_server.models.subnet_neuron_registration_order import SubnetNeuronRegistrationOrder
from openapi_server.models.subnet_neuron_registration_response import SubnetNeuronRegistrationResponse
from openapi_server.models.subnet_order import SubnetOrder
from openapi_server.models.subnet_owner_order import SubnetOwnerOrder
from openapi_server.models.subnet_owner_response import SubnetOwnerResponse
from openapi_server.models.subnet_pruning_history_order import SubnetPruningHistoryOrder
from openapi_server.models.subnet_pruning_latest_order import SubnetPruningLatestOrder
from openapi_server.models.subnet_pruning_response import SubnetPruningResponse
from openapi_server.models.subnet_registration_cost_history_order import SubnetRegistrationCostHistoryOrder
from openapi_server.models.subnet_registration_cost_response import SubnetRegistrationCostResponse
from openapi_server.models.subnet_registration_order import SubnetRegistrationOrder
from openapi_server.models.subnet_registration_response import SubnetRegistrationResponse
from openapi_server.models.subnet_response import SubnetResponse
from openapi_server.security_api import get_token_api_key

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/subnet/distribution/coldkey/v1",
    responses={
        200: {"model": SubnetDistributionColdkeyResponse, "description": "Subnet coldkey distribution retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Subnet coldkey distribution not found"},
        500: {"description": "Internal server error"},
    },
    tags=["subnet"],
    response_model_by_alias=True,
)
async def get_subnet_distribution_coldkey(
    netuid: int = Query(None, description="", alias="netuid"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> SubnetDistributionColdkeyResponse:
    if not BaseSubnetApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSubnetApi.subclasses[0]().get_subnet_distribution_coldkey(netuid)


@router.get(
    "/api/subnet/distribution/incentive/v1",
    responses={
        200: {"model": SubnetDistributionIncentiveResponse, "description": "Subnet incentive distribution retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Subnet incentive distribution not found"},
        500: {"description": "Internal server error"},
    },
    tags=["subnet"],
    response_model_by_alias=True,
)
async def get_subnet_distribution_incentive(
    netuid: int = Query(None, description="", alias="netuid"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> SubnetDistributionIncentiveResponse:
    if not BaseSubnetApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSubnetApi.subclasses[0]().get_subnet_distribution_incentive(netuid)


@router.get(
    "/api/subnet/distribution/ip/v1",
    responses={
        200: {"model": SubnetDistributionIPResponse, "description": "Subnet IP distribution retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Subnet IP distribution not found"},
        500: {"description": "Internal server error"},
    },
    tags=["subnet"],
    response_model_by_alias=True,
)
async def get_subnet_distribution_ip(
    netuid: int = Query(None, description="", alias="netuid"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> SubnetDistributionIPResponse:
    if not BaseSubnetApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSubnetApi.subclasses[0]().get_subnet_distribution_ip(netuid)


@router.get(
    "/api/subnet/history/v1",
    responses={
        200: {"model": SubnetResponse, "description": "Subnets retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Subnets not found"},
        500: {"description": "Internal server error"},
    },
    tags=["subnet"],
    response_model_by_alias=True,
)
async def get_subnet_history(
    netuid: int = Query(None, description="", alias="netuid"),
    frequency: Optional[FrequencyBlockHourDay] = Query(None, description="", alias="frequency"),
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[SubnetHistoryOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> SubnetResponse:
    if not BaseSubnetApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSubnetApi.subclasses[0]().get_subnet_history(netuid, frequency, block_number, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/subnet/identity/v1",
    responses={
        200: {"model": SubnetIdentityResponse, "description": "Subnet identities retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Subnet identities not found"},
        500: {"description": "Internal server error"},
    },
    tags=["subnet"],
    response_model_by_alias=True,
)
async def get_subnet_identity(
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> SubnetIdentityResponse:
    if not BaseSubnetApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSubnetApi.subclasses[0]().get_subnet_identity(netuid, page, limit)


@router.get(
    "/api/subnet/identity_set/v1",
    responses={
        200: {"model": SubnetIdentitySetResponse, "description": "Subnet identity set events retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Subnet identity set events not found"},
        500: {"description": "Internal server error"},
    },
    tags=["subnet"],
    response_model_by_alias=True,
)
async def get_subnet_identity_set(
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    owner: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="owner"),
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[SubnetIdentitySetOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> SubnetIdentitySetResponse:
    if not BaseSubnetApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSubnetApi.subclasses[0]().get_subnet_identity_set(netuid, owner, block_number, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/subnet/latest/v1",
    responses={
        200: {"model": SubnetLatestResponse, "description": "Subnets retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Subnets not found"},
        500: {"description": "Internal server error"},
    },
    tags=["subnet"],
    response_model_by_alias=True,
)
async def get_subnet_latest(
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[SubnetOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> SubnetLatestResponse:
    if not BaseSubnetApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSubnetApi.subclasses[0]().get_subnet_latest(netuid, page, limit, order)


@router.get(
    "/api/subnet/metadata/v1",
    responses={
        200: {"model": SubnetMetadataResponse, "description": "Subnet metadata retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Subnet metadata not found"},
        500: {"description": "Internal server error"},
    },
    tags=["subnet"],
    response_model_by_alias=True,
)
async def get_subnet_metadata(
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> SubnetMetadataResponse:
    if not BaseSubnetApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSubnetApi.subclasses[0]().get_subnet_metadata(netuid, page, limit)


@router.get(
    "/api/subnet/neuron/deregistration/v1",
    responses={
        200: {"model": SubnetNeuronDeregistrationResponse, "description": "Subnet neuron deregistrations retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Subnet neuron deregistrations not found"},
        500: {"description": "Internal server error"},
    },
    tags=["subnet"],
    response_model_by_alias=True,
)
async def get_subnet_neuron_deregistration(
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    uid: Optional[int] = Query(None, description="", alias="uid"),
    hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="hotkey"),
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[SubnetNeuronDeregistrationOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> SubnetNeuronDeregistrationResponse:
    if not BaseSubnetApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSubnetApi.subclasses[0]().get_subnet_neuron_deregistration(netuid, uid, hotkey, block_number, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/subnet/neuron/registration/v1",
    responses={
        200: {"model": SubnetNeuronRegistrationResponse, "description": "Subnet neuron registrations retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Subnet neuron registrations not found"},
        500: {"description": "Internal server error"},
    },
    tags=["subnet"],
    response_model_by_alias=True,
)
async def get_subnet_neuron_registration(
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    uid: Optional[int] = Query(None, description="", alias="uid"),
    hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="hotkey"),
    coldkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="coldkey"),
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[SubnetNeuronRegistrationOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> SubnetNeuronRegistrationResponse:
    if not BaseSubnetApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSubnetApi.subclasses[0]().get_subnet_neuron_registration(netuid, uid, hotkey, coldkey, block_number, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/subnet/owner/v1",
    responses={
        200: {"model": SubnetOwnerResponse, "description": "Subnet owners retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Subnet owners not found"},
        500: {"description": "Internal server error"},
    },
    tags=["subnet"],
    response_model_by_alias=True,
)
async def get_subnet_owner(
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    owner: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="owner"),
    is_coldkey_swap: Optional[StrictBool] = Query(None, description="", alias="is_coldkey_swap"),
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[SubnetOwnerOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> SubnetOwnerResponse:
    if not BaseSubnetApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSubnetApi.subclasses[0]().get_subnet_owner(netuid, owner, is_coldkey_swap, block_number, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/subnet/pruning/history/v1",
    responses={
        200: {"model": SubnetPruningResponse, "description": "Subnets history retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Subnets history not found"},
        500: {"description": "Internal server error"},
    },
    tags=["subnet"],
    response_model_by_alias=True,
)
async def get_subnet_pruning_history(
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[SubnetPruningHistoryOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> SubnetPruningResponse:
    if not BaseSubnetApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSubnetApi.subclasses[0]().get_subnet_pruning_history(netuid, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/subnet/pruning/latest/v1",
    responses={
        200: {"model": SubnetPruningResponse, "description": "Subnets retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Subnets not found"},
        500: {"description": "Internal server error"},
    },
    tags=["subnet"],
    response_model_by_alias=True,
)
async def get_subnet_pruning_latest(
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    is_immune: Optional[StrictBool] = Query(None, description="", alias="is_immune"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[SubnetPruningLatestOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> SubnetPruningResponse:
    if not BaseSubnetApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSubnetApi.subclasses[0]().get_subnet_pruning_latest(netuid, is_immune, page, limit, order)


@router.get(
    "/api/subnet/registration/v1",
    responses={
        200: {"model": SubnetRegistrationResponse, "description": "Subnet registrations retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Subnet registrations not found"},
        500: {"description": "Internal server error"},
    },
    tags=["subnet"],
    response_model_by_alias=True,
)
async def get_subnet_registration(
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    owner: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="owner"),
    registered_by: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="registered_by"),
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[datetime], Field(description="Start of timestamp range (inclusive)")] = Query(None, description="Start of timestamp range (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[datetime], Field(description="End of timestamp range (inclusive)")] = Query(None, description="End of timestamp range (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[SubnetRegistrationOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> SubnetRegistrationResponse:
    if not BaseSubnetApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSubnetApi.subclasses[0]().get_subnet_registration(netuid, owner, registered_by, block_number, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/subnet/registration_cost/history/v1",
    responses={
        200: {"model": SubnetRegistrationCostResponse, "description": "Subnet registration cost retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Subnet registration cost not found"},
        500: {"description": "Internal server error"},
    },
    tags=["subnet"],
    response_model_by_alias=True,
)
async def get_subnet_registration_cost_history(
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[SubnetRegistrationCostHistoryOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> SubnetRegistrationCostResponse:
    if not BaseSubnetApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSubnetApi.subclasses[0]().get_subnet_registration_cost_history(block_number, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/subnet/registration_cost/latest/v1",
    responses={
        200: {"model": SubnetRegistrationCostResponse, "description": "Subnet registration cost retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Subnet registration cost not found"},
        500: {"description": "Internal server error"},
    },
    tags=["subnet"],
    response_model_by_alias=True,
)
async def get_subnet_registration_cost_latest(
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> SubnetRegistrationCostResponse:
    if not BaseSubnetApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSubnetApi.subclasses[0]().get_subnet_registration_cost_latest()
