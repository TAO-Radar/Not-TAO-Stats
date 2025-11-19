# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.delegation_api_base import BaseDelegationApi
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
from openapi_server.models.delegation_action import DelegationAction
from openapi_server.models.delegation_order import DelegationOrder
from openapi_server.models.delegation_response import DelegationResponse
from openapi_server.security_api import get_token_api_key

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/delegation/v1",
    responses={
        200: {"model": DelegationResponse, "description": "Delegations retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Delegations not found"},
        500: {"description": "Internal server error"},
    },
    tags=["delegation"],
    response_model_by_alias=True,
)
async def get_delegation(
    nominator: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="nominator"),
    delegate: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="delegate"),
    action: Optional[DelegationAction] = Query(None, description="", alias="action"),
    is_transfer: Optional[StrictBool] = Query(None, description="", alias="is_transfer"),
    transfer_address: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="transfer_address"),
    extrinsic_id: Optional[StrictStr] = Query(None, description="", alias="extrinsic_id"),
    amount_min: Annotated[Optional[StrictStr], Field(description="Minimum amount (inclusive)")] = Query(None, description="Minimum amount (inclusive)", alias="amount_min"),
    amount_max: Annotated[Optional[StrictStr], Field(description="Maximum amount (inclusive)")] = Query(None, description="Maximum amount (inclusive)", alias="amount_max"),
    netuid: Optional[int] = Query(None, description="", alias="netuid"),
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[DelegationOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DelegationResponse:
    if not BaseDelegationApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDelegationApi.subclasses[0]().get_delegation(nominator, delegate, action, is_transfer, transfer_address, extrinsic_id, amount_min, amount_max, netuid, block_number, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)
