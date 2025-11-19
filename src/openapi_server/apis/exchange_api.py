# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.exchange_api_base import BaseExchangeApi
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
from typing import Any, Optional
from openapi_server.models.exchange_response import ExchangeResponse
from openapi_server.security_api import get_token_api_key

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/exchange/v1",
    responses={
        200: {"model": ExchangeResponse, "description": "Exchanges retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Exchanges not found"},
        500: {"description": "Internal server error"},
    },
    tags=["exchange"],
    response_model_by_alias=True,
)
async def get_exchange(
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> ExchangeResponse:
    if not BaseExchangeApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseExchangeApi.subclasses[0]().get_exchange(page, limit)
