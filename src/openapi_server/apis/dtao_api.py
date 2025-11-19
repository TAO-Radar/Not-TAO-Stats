# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.dtao_api_base import BaseDtaoApi
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
from openapi_server.models.config_response import ConfigResponse
from openapi_server.models.dtao_burned_alpha_order import DtaoBurnedAlphaOrder
from openapi_server.models.dtao_burned_alpha_response import DtaoBurnedAlphaResponse
from openapi_server.models.dtao_burned_alpha_total_order import DtaoBurnedAlphaTotalOrder
from openapi_server.models.dtao_burned_alpha_total_response import DtaoBurnedAlphaTotalResponse
from openapi_server.models.dtao_coldkey_alpha_shares_history_order import DtaoColdkeyAlphaSharesHistoryOrder
from openapi_server.models.dtao_coldkey_alpha_shares_latest_order import DtaoColdkeyAlphaSharesLatestOrder
from openapi_server.models.dtao_coldkey_alpha_shares_response import DtaoColdkeyAlphaSharesResponse
from openapi_server.models.dtao_delegation_frequency import DtaoDelegationFrequency
from openapi_server.models.dtao_delegation_volume_response import DtaoDelegationVolumeResponse
from openapi_server.models.dtao_hotkey_alpha_shares_history_order import DtaoHotkeyAlphaSharesHistoryOrder
from openapi_server.models.dtao_hotkey_alpha_shares_latest_order import DtaoHotkeyAlphaSharesLatestOrder
from openapi_server.models.dtao_hotkey_alpha_shares_response import DtaoHotkeyAlphaSharesResponse
from openapi_server.models.dtao_hotkey_emission_order import DtaoHotkeyEmissionOrder
from openapi_server.models.dtao_hotkey_emission_response import DtaoHotkeyEmissionResponse
from openapi_server.models.dtao_slippage_direction import DtaoSlippageDirection
from openapi_server.models.dtao_slippage_response import DtaoSlippageResponse
from openapi_server.models.dtao_stake_balance_aggregated_latest_order import DtaoStakeBalanceAggregatedLatestOrder
from openapi_server.models.dtao_stake_balance_aggregated_response import DtaoStakeBalanceAggregatedResponse
from openapi_server.models.dtao_stake_balance_history_order import DtaoStakeBalanceHistoryOrder
from openapi_server.models.dtao_stake_balance_history_response import DtaoStakeBalanceHistoryResponse
from openapi_server.models.dtao_stake_balance_latest_order import DtaoStakeBalanceLatestOrder
from openapi_server.models.dtao_stake_balance_latest_response import DtaoStakeBalanceLatestResponse
from openapi_server.models.dtao_stake_balance_portfolio_response import DtaoStakeBalancePortfolioResponse
from openapi_server.models.dtao_subnet_emission_order import DtaoSubnetEmissionOrder
from openapi_server.models.dtao_subnet_emission_response import DtaoSubnetEmissionResponse
from openapi_server.models.history_response import HistoryResponse
from openapi_server.models.symbol_info_response import SymbolInfoResponse
from openapi_server.models.tao_flow_response import TaoFlowResponse
from openapi_server.security_api import get_token_api_key

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/dtao/burned_alpha/total/v1",
    responses={
        200: {"model": DtaoBurnedAlphaTotalResponse, "description": "Dtao burned alpha total retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Dtao burned alpha total not found"},
        500: {"description": "Internal server error"},
    },
    tags=["dtao"],
    response_model_by_alias=True,
)
async def get_dtao_burned_alpha_total(
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[DtaoBurnedAlphaTotalOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoBurnedAlphaTotalResponse:
    if not BaseDtaoApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDtaoApi.subclasses[0]().get_dtao_burned_alpha_total(netuid, page, limit, order)


@router.get(
    "/api/dtao/burned_alpha/v1",
    responses={
        200: {"model": DtaoBurnedAlphaResponse, "description": "Dtao burned alpha retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Dtao burned alpha not found"},
        500: {"description": "Internal server error"},
    },
    tags=["dtao"],
    response_model_by_alias=True,
)
async def get_dtao_burned_alpha(
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    hotkey: Optional[StrictStr] = Query(None, description="", alias="hotkey"),
    coldkey: Optional[StrictStr] = Query(None, description="", alias="coldkey"),
    extrinsic_id: Optional[StrictStr] = Query(None, description="", alias="extrinsic_id"),
    burn_type: Annotated[Optional[StrictStr], Field(description="incentive OR call")] = Query(None, description="incentive OR call", alias="burn_type"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    amount_min: Optional[StrictStr] = Query(None, description="", alias="amount_min"),
    amount_max: Optional[StrictStr] = Query(None, description="", alias="amount_max"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[DtaoBurnedAlphaOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoBurnedAlphaResponse:
    if not BaseDtaoApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDtaoApi.subclasses[0]().get_dtao_burned_alpha(netuid, hotkey, coldkey, extrinsic_id, burn_type, block_start, block_end, timestamp_start, timestamp_end, amount_min, amount_max, page, limit, order)


@router.get(
    "/api/dtao/coldkey_alpha_shares/history/v1",
    responses={
        200: {"model": DtaoColdkeyAlphaSharesResponse, "description": "Dtao coldkey alpha shares retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Dtao coldkey alpha shares not found"},
        500: {"description": "Internal server error"},
    },
    tags=["dtao"],
    response_model_by_alias=True,
)
async def get_dtao_coldkey_alpha_shares_history(
    coldkey: Optional[StrictStr] = Query(None, description="", alias="coldkey"),
    hotkey: Optional[StrictStr] = Query(None, description="", alias="hotkey"),
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[DtaoColdkeyAlphaSharesHistoryOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoColdkeyAlphaSharesResponse:
    if not BaseDtaoApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDtaoApi.subclasses[0]().get_dtao_coldkey_alpha_shares_history(coldkey, hotkey, netuid, block_number, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/dtao/coldkey_alpha_shares/latest/v1",
    responses={
        200: {"model": DtaoColdkeyAlphaSharesResponse, "description": "Dtao coldkey alpha shares retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Dtao coldkey alpha shares not found"},
        500: {"description": "Internal server error"},
    },
    tags=["dtao"],
    response_model_by_alias=True,
)
async def get_dtao_coldkey_alpha_shares_latest(
    alpha_min: Optional[StrictStr] = Query(None, description="", alias="alpha_min"),
    alpha_max: Optional[StrictStr] = Query(None, description="", alias="alpha_max"),
    coldkey: Optional[StrictStr] = Query(None, description="", alias="coldkey"),
    hotkey: Optional[StrictStr] = Query(None, description="", alias="hotkey"),
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[DtaoColdkeyAlphaSharesLatestOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoColdkeyAlphaSharesResponse:
    if not BaseDtaoApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDtaoApi.subclasses[0]().get_dtao_coldkey_alpha_shares_latest(alpha_min, alpha_max, coldkey, hotkey, netuid, page, limit, order)


@router.get(
    "/api/dtao/delegation_volume/v1",
    responses={
        200: {"model": DtaoDelegationVolumeResponse, "description": "Delegation volume retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Delegation volume not found"},
        500: {"description": "Internal server error"},
    },
    tags=["dtao"],
    response_model_by_alias=True,
)
async def get_dtao_delegation_volume(
    frequency: Annotated[Optional[DtaoDelegationFrequency], Field(description="Default is 60 minutes")] = Query(None, description="Default is 60 minutes", alias="frequency"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoDelegationVolumeResponse:
    if not BaseDtaoApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDtaoApi.subclasses[0]().get_dtao_delegation_volume(frequency, page, limit)


@router.get(
    "/api/dtao/hotkey_alpha_shares/history/v1",
    responses={
        200: {"model": DtaoHotkeyAlphaSharesResponse, "description": "Dtao hotkey alpha shares retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Dtao hotkey alpha shares not found"},
        500: {"description": "Internal server error"},
    },
    tags=["dtao"],
    response_model_by_alias=True,
)
async def get_dtao_hotkey_alpha_shares_history(
    hotkey: Optional[StrictStr] = Query(None, description="", alias="hotkey"),
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[DtaoHotkeyAlphaSharesHistoryOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoHotkeyAlphaSharesResponse:
    if not BaseDtaoApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDtaoApi.subclasses[0]().get_dtao_hotkey_alpha_shares_history(hotkey, netuid, block_number, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/dtao/hotkey_alpha_shares/latest/v1",
    responses={
        200: {"model": DtaoHotkeyAlphaSharesResponse, "description": "Dtao hotkey alpha shares retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Dtao hotkey alpha shares not found"},
        500: {"description": "Internal server error"},
    },
    tags=["dtao"],
    response_model_by_alias=True,
)
async def get_dtao_hotkey_alpha_shares_latest(
    alpha_min: Optional[StrictStr] = Query(None, description="", alias="alpha_min"),
    alpha_max: Optional[StrictStr] = Query(None, description="", alias="alpha_max"),
    hotkey: Optional[StrictStr] = Query(None, description="", alias="hotkey"),
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[DtaoHotkeyAlphaSharesLatestOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoHotkeyAlphaSharesResponse:
    if not BaseDtaoApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDtaoApi.subclasses[0]().get_dtao_hotkey_alpha_shares_latest(alpha_min, alpha_max, hotkey, netuid, page, limit, order)


@router.get(
    "/api/dtao/hotkey_emission/v1",
    responses={
        200: {"model": DtaoHotkeyEmissionResponse, "description": "Dtao hotkey emission retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Dtao hotkey emission not found"},
        500: {"description": "Internal server error"},
    },
    tags=["dtao"],
    response_model_by_alias=True,
)
async def get_dtao_hotkey_emission(
    hotkey: Optional[StrictStr] = Query(None, description="", alias="hotkey"),
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[DtaoHotkeyEmissionOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoHotkeyEmissionResponse:
    if not BaseDtaoApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDtaoApi.subclasses[0]().get_dtao_hotkey_emission(hotkey, netuid, block_number, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/dtao/slippage/v1",
    responses={
        200: {"model": DtaoSlippageResponse, "description": "Dtao slippage retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Dtao slippage not found"},
        500: {"description": "Internal server error"},
    },
    tags=["dtao"],
    response_model_by_alias=True,
)
async def get_dtao_slippage(
    netuid: int = Query(None, description="", alias="netuid"),
    input_tokens: StrictStr = Query(None, description="", alias="input_tokens"),
    direction: DtaoSlippageDirection = Query(None, description="", alias="direction"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoSlippageResponse:
    if not BaseDtaoApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDtaoApi.subclasses[0]().get_dtao_slippage(netuid, input_tokens, direction)


@router.get(
    "/api/dtao/stake_balance/history/v1",
    responses={
        200: {"model": DtaoStakeBalanceHistoryResponse, "description": "Stake balances retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Stake balances not found"},
        500: {"description": "Internal server error"},
    },
    tags=["dtao"],
    response_model_by_alias=True,
)
async def get_dtao_stake_balance_history(
    coldkey: Annotated[StrictStr, Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="coldkey"),
    hotkey: Annotated[StrictStr, Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="hotkey"),
    netuid: int = Query(None, description="", alias="netuid"),
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[DtaoStakeBalanceHistoryOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoStakeBalanceHistoryResponse:
    if not BaseDtaoApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDtaoApi.subclasses[0]().get_dtao_stake_balance_history(coldkey, hotkey, netuid, block_number, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/dtao/stake_balance/latest/v1",
    responses={
        200: {"model": DtaoStakeBalanceLatestResponse, "description": "Stake balances retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Stake balances not found"},
        500: {"description": "Internal server error"},
    },
    tags=["dtao"],
    response_model_by_alias=True,
)
async def get_dtao_stake_balance_latest(
    coldkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="coldkey"),
    hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="hotkey"),
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    balance_min: Optional[StrictStr] = Query(None, description="", alias="balance_min"),
    balance_max: Optional[StrictStr] = Query(None, description="", alias="balance_max"),
    balance_as_tao_min: Optional[StrictStr] = Query(None, description="", alias="balance_as_tao_min"),
    balance_as_tao_max: Optional[StrictStr] = Query(None, description="", alias="balance_as_tao_max"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[DtaoStakeBalanceLatestOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoStakeBalanceLatestResponse:
    if not BaseDtaoApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDtaoApi.subclasses[0]().get_dtao_stake_balance_latest(coldkey, hotkey, netuid, balance_min, balance_max, balance_as_tao_min, balance_as_tao_max, page, limit, order)


@router.get(
    "/api/dtao/stake_balance/portfolio/v1",
    responses={
        200: {"model": DtaoStakeBalancePortfolioResponse, "description": "Stake balance portfolios retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Stake balance portfolios not found"},
        500: {"description": "Internal server error"},
    },
    tags=["dtao"],
    response_model_by_alias=True,
)
async def get_dtao_stake_balance_portfolio(
    coldkey: Annotated[StrictStr, Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="coldkey"),
    hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="hotkey"),
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    days: Optional[int] = Query(None, description="", alias="days"),
    balance_min: Optional[StrictStr] = Query(None, description="", alias="balance_min"),
    balance_max: Optional[StrictStr] = Query(None, description="", alias="balance_max"),
    balance_as_tao_min: Optional[StrictStr] = Query(None, description="", alias="balance_as_tao_min"),
    balance_as_tao_max: Optional[StrictStr] = Query(None, description="", alias="balance_as_tao_max"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[DtaoStakeBalanceLatestOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoStakeBalancePortfolioResponse:
    if not BaseDtaoApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDtaoApi.subclasses[0]().get_dtao_stake_balance_portfolio(coldkey, hotkey, netuid, days, balance_min, balance_max, balance_as_tao_min, balance_as_tao_max, page, limit, order)


@router.get(
    "/api/dtao/stake_balance_aggregated/latest/v1",
    responses={
        200: {"model": DtaoStakeBalanceAggregatedResponse, "description": "Stake balances retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Stake balances not found"},
        500: {"description": "Internal server error"},
    },
    tags=["dtao"],
    response_model_by_alias=True,
)
async def get_dtao_stake_balance_aggregated_latest(
    coldkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="coldkey"),
    total_balance_as_tao_min: Optional[StrictStr] = Query(None, description="", alias="total_balance_as_tao_min"),
    total_balance_as_tao_max: Optional[StrictStr] = Query(None, description="", alias="total_balance_as_tao_max"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[DtaoStakeBalanceAggregatedLatestOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoStakeBalanceAggregatedResponse:
    if not BaseDtaoApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDtaoApi.subclasses[0]().get_dtao_stake_balance_aggregated_latest(coldkey, total_balance_as_tao_min, total_balance_as_tao_max, page, limit, order)


@router.get(
    "/api/dtao/subnet_emission/v1",
    responses={
        200: {"model": DtaoSubnetEmissionResponse, "description": "Dtao subnet emission retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Dtao subnet emission not found"},
        500: {"description": "Internal server error"},
    },
    tags=["dtao"],
    response_model_by_alias=True,
)
async def get_dtao_subnet_emission(
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[DtaoSubnetEmissionOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DtaoSubnetEmissionResponse:
    if not BaseDtaoApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDtaoApi.subclasses[0]().get_dtao_subnet_emission(netuid, block_number, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)


@router.get(
    "/api/dtao/tao_flow/v1",
    responses={
        200: {"model": TaoFlowResponse, "description": "Tao flow retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Tao flow not found"},
        500: {"description": "Internal server error"},
    },
    tags=["dtao"],
    response_model_by_alias=True,
)
async def get_dtao_tao_flow(
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> TaoFlowResponse:
    if not BaseDtaoApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDtaoApi.subclasses[0]().get_dtao_tao_flow(netuid, block_start, block_end, timestamp_start, timestamp_end)


@router.get(
    "/api/dtao/tradingview/udf/config",
    responses={
        200: {"model": ConfigResponse, "description": "Config retrieved successfully"},
    },
    tags=["dtao"],
    response_model_by_alias=True,
)
async def get_dtao_tradingview_udf_config(
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> ConfigResponse:
    if not BaseDtaoApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDtaoApi.subclasses[0]().get_dtao_tradingview_udf_config()


@router.get(
    "/api/dtao/tradingview/udf/history",
    responses={
        200: {"model": HistoryResponse, "description": "History retrieved successfully"},
    },
    tags=["dtao"],
    response_model_by_alias=True,
)
async def get_dtao_tradingview_udf_history(
    symbol: StrictStr = Query(None, description="", alias="symbol"),
    resolution: StrictStr = Query(None, description="", alias="resolution"),
    to: int = Query(None, description="", alias="to"),
    var_from: Optional[int] = Query(None, description="", alias="from"),
    countback: Optional[int] = Query(None, description="", alias="countback"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> HistoryResponse:
    if not BaseDtaoApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDtaoApi.subclasses[0]().get_dtao_tradingview_udf_history(symbol, resolution, to, var_from, countback)


@router.get(
    "/api/dtao/tradingview/udf/symbol_info",
    responses={
        200: {"model": SymbolInfoResponse, "description": "Symbol info retrieved successfully"},
    },
    tags=["dtao"],
    response_model_by_alias=True,
)
async def get_dtao_tradingview_udf_symbol_info(
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> SymbolInfoResponse:
    if not BaseDtaoApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDtaoApi.subclasses[0]().get_dtao_tradingview_udf_symbol_info(netuid)
