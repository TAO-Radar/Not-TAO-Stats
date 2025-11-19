# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.validator_api_base import BaseValidatorApi
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
from openapi_server.models.dtao_validator_available_response import DtaoValidatorAvailableResponse
from openapi_server.models.dtao_validator_dividends_history_order import DtaoValidatorDividendsHistoryOrder
from openapi_server.models.dtao_validator_dividends_latest_order import DtaoValidatorDividendsLatestOrder
from openapi_server.models.dtao_validator_dividends_response import DtaoValidatorDividendsResponse
from openapi_server.models.dtao_validator_history_order import DtaoValidatorHistoryOrder
from openapi_server.models.dtao_validator_latest_order import DtaoValidatorLatestOrder
from openapi_server.models.dtao_validator_performance_history_order import DtaoValidatorPerformanceHistoryOrder
from openapi_server.models.dtao_validator_performance_latest_order import DtaoValidatorPerformanceLatestOrder
from openapi_server.models.dtao_validator_performance_response import DtaoValidatorPerformanceResponse
from openapi_server.models.dtao_validator_response import DtaoValidatorResponse
from openapi_server.models.dtao_validator_yield_latest_order import DtaoValidatorYieldLatestOrder
from openapi_server.models.dtao_validator_yield_response import DtaoValidatorYieldResponse
from openapi_server.models.validator_history_order import ValidatorHistoryOrder
from openapi_server.models.validator_identity_order import ValidatorIdentityOrder
from openapi_server.models.validator_identity_response import ValidatorIdentityResponse
from openapi_server.models.validator_metrics_history_order import ValidatorMetricsHistoryOrder
from openapi_server.models.validator_metrics_order import ValidatorMetricsOrder
from openapi_server.models.validator_metrics_response import ValidatorMetricsResponse
from openapi_server.models.validator_order import ValidatorOrder
from openapi_server.models.validator_performance_order import ValidatorPerformanceOrder
from openapi_server.models.validator_performance_response import ValidatorPerformanceResponse
from openapi_server.models.validator_response import ValidatorResponse
from openapi_server.models.validator_weights_history_order import ValidatorWeightsHistoryOrder
from openapi_server.models.validator_weights_order import ValidatorWeightsOrder
from openapi_server.models.validator_weights_response import ValidatorWeightsResponse
from openapi_server.models.validator_weights_v2_history_order import ValidatorWeightsV2HistoryOrder
from openapi_server.models.validator_weights_v2_order import ValidatorWeightsV2Order
from openapi_server.models.validator_weights_v2_response import ValidatorWeightsV2Response
from openapi_server.models.weight_copier_response import WeightCopierResponse
from openapi_server.security_api import get_token_api_key

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/dtao/validator/available/v1",
    responses={
        200: {"model": DtaoValidatorAvailableResponse, "description": "Validators retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Validators not found"},
        500: {"description": "Internal server error"},
    },
    tags=["validator"],
    response_model_by_alias=True,
)
async def get_dtao_validator_available(
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoValidatorAvailableResponse:
    if not BaseValidatorApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseValidatorApi.subclasses[0]().get_dtao_validator_available(netuid)


@router.get(
    "/api/dtao/validator/dividends/history/v1",
    responses={
        200: {"model": DtaoValidatorDividendsResponse, "description": "Validators retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Validators not found"},
        500: {"description": "Internal server error"},
    },
    tags=["validator"],
    response_model_by_alias=True,
)
async def get_dtao_validator_dividends_history(
    hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="hotkey"),
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    frequency: Optional[Any] = Query(None, description="", alias="frequency"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[DtaoValidatorDividendsHistoryOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoValidatorDividendsResponse:
    if not BaseValidatorApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseValidatorApi.subclasses[0]().get_dtao_validator_dividends_history(hotkey, netuid, block_number, block_start, block_end, timestamp_start, timestamp_end, frequency, page, limit, order)


@router.get(
    "/api/dtao/validator/dividends/latest/v1",
    responses={
        200: {"model": DtaoValidatorDividendsResponse, "description": "Validators retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Validators not found"},
        500: {"description": "Internal server error"},
    },
    tags=["validator"],
    response_model_by_alias=True,
)
async def get_dtao_validator_dividends_latest(
    hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="hotkey"),
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[DtaoValidatorDividendsLatestOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoValidatorDividendsResponse:
    if not BaseValidatorApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseValidatorApi.subclasses[0]().get_dtao_validator_dividends_latest(hotkey, netuid, page, limit, order)


@router.get(
    "/api/dtao/validator/history/v1",
    responses={
        200: {"model": DtaoValidatorResponse, "description": "Validators retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Validators not found"},
        500: {"description": "Internal server error"},
    },
    tags=["validator"],
    response_model_by_alias=True,
)
async def get_dtao_validator_history(
    hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="hotkey"),
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[DtaoValidatorHistoryOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoValidatorResponse:
    if not BaseValidatorApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseValidatorApi.subclasses[0]().get_dtao_validator_history(hotkey, block_number, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/dtao/validator/latest/v1",
    responses={
        200: {"model": DtaoValidatorResponse, "description": "Validators retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Validators not found"},
        500: {"description": "Internal server error"},
    },
    tags=["validator"],
    response_model_by_alias=True,
)
async def get_dtao_validator_latest(
    hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="hotkey"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[DtaoValidatorLatestOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoValidatorResponse:
    if not BaseValidatorApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseValidatorApi.subclasses[0]().get_dtao_validator_latest(hotkey, page, limit, order)


@router.get(
    "/api/dtao/validator/performance/history/v1",
    responses={
        200: {"model": DtaoValidatorPerformanceResponse, "description": "Validators retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Validators not found"},
        500: {"description": "Internal server error"},
    },
    tags=["validator"],
    response_model_by_alias=True,
)
async def get_dtao_validator_performance_history(
    hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="hotkey"),
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[DtaoValidatorPerformanceHistoryOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoValidatorPerformanceResponse:
    if not BaseValidatorApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseValidatorApi.subclasses[0]().get_dtao_validator_performance_history(hotkey, netuid, block_number, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/dtao/validator/performance/latest/v1",
    responses={
        200: {"model": DtaoValidatorPerformanceResponse, "description": "Validators retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Validators not found"},
        500: {"description": "Internal server error"},
    },
    tags=["validator"],
    response_model_by_alias=True,
)
async def get_dtao_validator_performance_latest(
    hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="hotkey"),
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    validator_type: Annotated[Optional[StrictStr], Field(description="Validator type: \"running_infra\" or \"childkey\".")] = Query(None, description="Validator type: \&quot;running_infra\&quot; or \&quot;childkey\&quot;.", alias="validator_type"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[DtaoValidatorPerformanceLatestOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoValidatorPerformanceResponse:
    if not BaseValidatorApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseValidatorApi.subclasses[0]().get_dtao_validator_performance_latest(hotkey, netuid, validator_type, page, limit, order)


@router.get(
    "/api/dtao/validator/yield/latest/v1",
    responses={
        200: {"model": DtaoValidatorYieldResponse, "description": "Validators retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Validators not found"},
        500: {"description": "Internal server error"},
    },
    tags=["validator"],
    response_model_by_alias=True,
)
async def get_dtao_validator_yield_latest(
    hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="hotkey"),
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    min_stake: Optional[StrictStr] = Query(None, description="", alias="min_stake"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[DtaoValidatorYieldLatestOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoValidatorYieldResponse:
    if not BaseValidatorApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseValidatorApi.subclasses[0]().get_dtao_validator_yield_latest(hotkey, netuid, min_stake, page, limit, order)


@router.get(
    "/api/validator/history/v1",
    responses={
        200: {"model": ValidatorResponse, "description": "Validators retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Validators not found"},
        500: {"description": "Internal server error"},
    },
    tags=["validator"],
    response_model_by_alias=True,
)
async def get_validator_history(
    hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="hotkey"),
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[ValidatorHistoryOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> ValidatorResponse:
    if not BaseValidatorApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseValidatorApi.subclasses[0]().get_validator_history(hotkey, block_number, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/validator/identity/v1",
    responses={
        200: {"model": ValidatorIdentityResponse, "description": "Validator identity retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Validator identity not found"},
        500: {"description": "Internal server error"},
    },
    tags=["validator"],
    response_model_by_alias=True,
)
async def get_validator_identity(
    hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="hotkey"),
    name: Optional[StrictStr] = Query(None, description="", alias="name"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[ValidatorIdentityOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> ValidatorIdentityResponse:
    if not BaseValidatorApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseValidatorApi.subclasses[0]().get_validator_identity(hotkey, name, page, limit, order)


@router.get(
    "/api/validator/latest/v1",
    responses={
        200: {"model": ValidatorResponse, "description": "Validators retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Validators not found"},
        500: {"description": "Internal server error"},
    },
    tags=["validator"],
    response_model_by_alias=True,
)
async def get_validator_latest(
    hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="hotkey"),
    stake_min: Optional[StrictStr] = Query(None, description="", alias="stake_min"),
    stake_max: Optional[StrictStr] = Query(None, description="", alias="stake_max"),
    apr_min: Optional[StrictStr] = Query(None, description="", alias="apr_min"),
    apr_max: Optional[StrictStr] = Query(None, description="", alias="apr_max"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[ValidatorOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> ValidatorResponse:
    if not BaseValidatorApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseValidatorApi.subclasses[0]().get_validator_latest(hotkey, stake_min, stake_max, apr_min, apr_max, page, limit, order)


@router.get(
    "/api/validator/metrics/history/v1",
    responses={
        200: {"model": ValidatorMetricsResponse, "description": "Validator metrics retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Validator metrics not found"},
        500: {"description": "Internal server error"},
    },
    tags=["validator"],
    response_model_by_alias=True,
)
async def get_validator_metrics_history(
    hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="hotkey"),
    coldkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="coldkey"),
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    block_number: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[ValidatorMetricsHistoryOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> ValidatorMetricsResponse:
    if not BaseValidatorApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseValidatorApi.subclasses[0]().get_validator_metrics_history(hotkey, coldkey, netuid, block_number, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/validator/metrics/latest/v1",
    responses={
        200: {"model": ValidatorMetricsResponse, "description": "Validator metrics retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Validator metrics not found"},
        500: {"description": "Internal server error"},
    },
    tags=["validator"],
    response_model_by_alias=True,
)
async def get_validator_metrics_latest(
    hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="hotkey"),
    coldkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="coldkey"),
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[ValidatorMetricsOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> ValidatorMetricsResponse:
    if not BaseValidatorApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseValidatorApi.subclasses[0]().get_validator_metrics_latest(hotkey, coldkey, netuid, page, limit, order)


@router.get(
    "/api/validator/performance/v1",
    responses={
        200: {"model": ValidatorPerformanceResponse, "description": "Validator performance retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Validator performance not found"},
        500: {"description": "Internal server error"},
    },
    tags=["validator"],
    response_model_by_alias=True,
)
async def get_validator_performance(
    hotkey: Annotated[StrictStr, Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="hotkey"),
    netuid: int = Query(None, description="", alias="netuid"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[ValidatorPerformanceOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> ValidatorPerformanceResponse:
    if not BaseValidatorApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseValidatorApi.subclasses[0]().get_validator_performance(hotkey, netuid, page, limit, order)


@router.get(
    "/api/validator/weight_copier/v1",
    responses={
        200: {"model": WeightCopierResponse, "description": "Validator weight copiers retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Validator weight copiers not found"},
        500: {"description": "Internal server error"},
    },
    tags=["validator"],
    response_model_by_alias=True,
)
async def get_validator_weight_copier(
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> WeightCopierResponse:
    if not BaseValidatorApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseValidatorApi.subclasses[0]().get_validator_weight_copier(page, limit)


@router.get(
    "/api/validator/weights/history/v1",
    responses={
        200: {"model": ValidatorWeightsResponse, "description": "Validator weights retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Validator weights not found"},
        500: {"description": "Internal server error"},
    },
    tags=["validator"],
    response_model_by_alias=True,
)
async def get_validator_weights_history(
    hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="hotkey"),
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    uid: Optional[int] = Query(None, description="", alias="uid"),
    block_number: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[ValidatorWeightsHistoryOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> ValidatorWeightsResponse:
    if not BaseValidatorApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseValidatorApi.subclasses[0]().get_validator_weights_history(hotkey, netuid, uid, block_number, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/validator/weights/history/v2",
    responses={
        200: {"model": ValidatorWeightsV2Response, "description": "Validator weights retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Validator weights not found"},
        500: {"description": "Internal server error"},
    },
    tags=["validator"],
    response_model_by_alias=True,
)
async def get_validator_weights_history1(
    hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="hotkey"),
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    uid: Optional[int] = Query(None, description="", alias="uid"),
    block_number: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[ValidatorWeightsV2HistoryOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> ValidatorWeightsV2Response:
    if not BaseValidatorApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseValidatorApi.subclasses[0]().get_validator_weights_history1(hotkey, netuid, uid, block_number, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/validator/weights/latest/v1",
    responses={
        200: {"model": ValidatorWeightsResponse, "description": "Validator weights retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Validator weights not found"},
        500: {"description": "Internal server error"},
    },
    tags=["validator"],
    response_model_by_alias=True,
)
async def get_validator_weights_latest(
    hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="hotkey"),
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    uid: Optional[int] = Query(None, description="", alias="uid"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[ValidatorWeightsOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> ValidatorWeightsResponse:
    if not BaseValidatorApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseValidatorApi.subclasses[0]().get_validator_weights_latest(hotkey, netuid, uid, page, limit, order)


@router.get(
    "/api/validator/weights/latest/v2",
    responses={
        200: {"model": ValidatorWeightsV2Response, "description": "Validator weights retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Validator weights not found"},
        500: {"description": "Internal server error"},
    },
    tags=["validator"],
    response_model_by_alias=True,
)
async def get_validator_weights_latest1(
    hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="hotkey"),
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    uid: Optional[int] = Query(None, description="", alias="uid"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[ValidatorWeightsV2Order] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> ValidatorWeightsV2Response:
    if not BaseValidatorApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseValidatorApi.subclasses[0]().get_validator_weights_latest1(hotkey, netuid, uid, page, limit, order)
