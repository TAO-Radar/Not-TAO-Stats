# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.call_api_base import BaseCallApi
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
from openapi_server.models.call_order import CallOrder
from openapi_server.models.call_response import CallResponse
from openapi_server.models.network import Network
from openapi_server.security_api import get_token_api_key

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/call/v1",
    responses={
        200: {"model": CallResponse, "description": "Calls retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Calls not found"},
        500: {"description": "Internal server error"},
    },
    tags=["call"],
    response_model_by_alias=True,
)
async def get_call(
    origin_address: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="origin_address"),
    network: Optional[Network] = Query(None, description="", alias="network"),
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    success: Optional[StrictBool] = Query(None, description="", alias="success"),
    full_name: Optional[StrictStr] = Query(None, description="", alias="full_name"),
    id: Optional[StrictStr] = Query(None, description="", alias="id"),
    extrinsic_id: Optional[StrictStr] = Query(None, description="", alias="extrinsic_id"),
    parent_id: Optional[StrictStr] = Query(None, description="", alias="parent_id"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[CallOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> CallResponse:
    if not BaseCallApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCallApi.subclasses[0]().get_call(origin_address, network, block_number, block_start, block_end, timestamp_start, timestamp_end, success, full_name, id, extrinsic_id, parent_id, page, limit, order)
