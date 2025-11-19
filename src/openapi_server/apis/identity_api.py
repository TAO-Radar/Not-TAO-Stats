# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.identity_api_base import BaseIdentityApi
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
from openapi_server.models.identity_history_order import IdentityHistoryOrder
from openapi_server.models.identity_history_response import IdentityHistoryResponse
from openapi_server.models.identity_response import IdentityResponse
from openapi_server.security_api import get_token_api_key

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/identity/history/v1",
    responses={
        200: {"model": IdentityHistoryResponse, "description": "Identity retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Identity not found"},
        500: {"description": "Internal server error"},
    },
    tags=["identity"],
    response_model_by_alias=True,
)
async def get_identity_history(
    address: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="address"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    order: Optional[IdentityHistoryOrder] = Query(None, description="", alias="order"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> IdentityHistoryResponse:
    if not BaseIdentityApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseIdentityApi.subclasses[0]().get_identity_history(address, page, limit, order)


@router.get(
    "/api/identity/latest/v1",
    responses={
        200: {"model": IdentityResponse, "description": "Identity retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Identity not found"},
        500: {"description": "Internal server error"},
    },
    tags=["identity"],
    response_model_by_alias=True,
)
async def get_identity_latest(
    address: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="address"),
    validator_hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="validator_hotkey"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> IdentityResponse:
    if not BaseIdentityApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseIdentityApi.subclasses[0]().get_identity_latest(address, validator_hotkey, page, limit)
