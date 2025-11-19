# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.extrinsic_api_base import BaseExtrinsicApi
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
from openapi_server.models.extrinsic_order import ExtrinsicOrder
from openapi_server.models.extrinsic_response import ExtrinsicResponse
from openapi_server.models.network_with_testnet import NetworkWithTestnet
from openapi_server.security_api import get_token_api_key

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/extrinsic/v1",
    responses={
        200: {"model": ExtrinsicResponse, "description": "Extrinsics retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Extrinsics not found"},
        500: {"description": "Internal server error"},
    },
    tags=["extrinsic"],
    response_model_by_alias=True,
)
async def get_extrinsic(
    network: Optional[NetworkWithTestnet] = Query(None, description="", alias="network"),
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    hash: Optional[StrictStr] = Query(None, description="", alias="hash"),
    full_name: Optional[StrictStr] = Query(None, description="", alias="full_name"),
    id: Optional[StrictStr] = Query(None, description="", alias="id"),
    success: Optional[StrictBool] = Query(None, description="", alias="success"),
    signer_address: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="signer_address"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[ExtrinsicOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> ExtrinsicResponse:
    if not BaseExtrinsicApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseExtrinsicApi.subclasses[0]().get_extrinsic(network, block_number, block_start, block_end, timestamp_start, timestamp_end, hash, full_name, id, success, signer_address, page, limit, order)
