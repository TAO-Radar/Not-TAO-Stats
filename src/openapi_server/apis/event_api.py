# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.event_api_base import BaseEventApi
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
from openapi_server.models.event_order import EventOrder
from openapi_server.models.event_response import EventResponse
from openapi_server.models.network import Network
from openapi_server.security_api import get_token_api_key

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/event/v1",
    responses={
        200: {"model": EventResponse, "description": "Events retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Events not found"},
        500: {"description": "Internal server error"},
    },
    tags=["event"],
    response_model_by_alias=True,
)
async def get_event(
    network: Optional[Network] = Query(None, description="", alias="network"),
    block_number: Optional[int] = Query(None, description="", alias="block_number"),
    block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")] = Query(None, description="Start of block range (inclusive)", alias="block_start"),
    block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")] = Query(None, description="End of block range (inclusive)", alias="block_end"),
    timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_start"),
    timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")] = Query(None, description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)", alias="timestamp_end"),
    pallet: Optional[StrictStr] = Query(None, description="", alias="pallet"),
    name: Optional[StrictStr] = Query(None, description="", alias="name"),
    full_name: Annotated[Optional[StrictStr], Field(description="Full name of the event, e.g. \"SubtensorModule.AxonServed\"")] = Query(None, description="Full name of the event, e.g. \&quot;SubtensorModule.AxonServed\&quot;", alias="full_name"),
    extrinsic_id: Optional[StrictStr] = Query(None, description="", alias="extrinsic_id"),
    call_id: Optional[StrictStr] = Query(None, description="", alias="call_id"),
    id: Optional[StrictStr] = Query(None, description="", alias="id"),
    phase: Optional[StrictStr] = Query(None, description="", alias="phase"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[EventOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> EventResponse:
    if not BaseEventApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseEventApi.subclasses[0]().get_event(network, block_number, block_start, block_end, timestamp_start, timestamp_end, pallet, name, full_name, extrinsic_id, call_id, id, phase, page, limit, order)
