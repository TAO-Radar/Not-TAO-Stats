# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.transfer_api_base import BaseTransferApi
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
from openapi_server.models.network_with_all import NetworkWithAll
from openapi_server.models.transfer_order import TransferOrder
from openapi_server.models.transfer_response import TransferResponse
from openapi_server.security_api import get_token_api_key

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/transfer/v1",
    responses={
        200: {"model": TransferResponse, "description": "Transfers retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Transfers not found"},
        500: {"description": "Internal server error"},
    },
    tags=["transfer"],
    response_model_by_alias=True,
)
async def get_transfer(
    network: Optional[NetworkWithAll] = Query(None, description="", alias="network"),
    address: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="address"),
    var_from: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="from"),
    to: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="to"),
    transaction_hash: Optional[StrictStr] = Query(None, description="", alias="transaction_hash"),
    extrinsic_id: Optional[StrictStr] = Query(None, description="", alias="extrinsic_id"),
    amount_min: Annotated[Optional[StrictStr], Field(description="Minimum amount (inclusive)")] = Query(None, description="Minimum amount (inclusive)", alias="amount_min"),
    amount_max: Annotated[Optional[StrictStr], Field(description="Maximum amount (inclusive)")] = Query(None, description="Maximum amount (inclusive)", alias="amount_max"),
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[TransferOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> TransferResponse:
    if not BaseTransferApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTransferApi.subclasses[0]().get_transfer(network, address, var_from, to, transaction_hash, extrinsic_id, amount_min, amount_max, block_number, block_start, block_end, timestamp_start, timestamp_end, page, limit, order)
