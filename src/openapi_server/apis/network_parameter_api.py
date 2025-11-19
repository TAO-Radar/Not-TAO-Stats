# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.network_parameter_api_base import BaseNetworkParameterApi
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
from typing import Any
from openapi_server.models.network_parameter_response import NetworkParameterResponse
from openapi_server.security_api import get_token_api_key

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/network_parameter/latest/v1",
    responses={
        200: {"model": NetworkParameterResponse, "description": "Network parameters retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Network parameters not found"},
        500: {"description": "Internal server error"},
    },
    tags=["network_parameter"],
    response_model_by_alias=True,
)
async def get_network_parameter_latest(
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> NetworkParameterResponse:
    if not BaseNetworkParameterApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseNetworkParameterApi.subclasses[0]().get_network_parameter_latest()
