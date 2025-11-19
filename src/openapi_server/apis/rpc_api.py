# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.rpc_api_base import BaseRpcApi
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
from openapi_server.models.rpc_hypertext_request import RPCHypertextRequest
from openapi_server.models.rpc_hypertext_response import RPCHypertextResponse
from openapi_server.models.rpc_target import RPCTarget
from openapi_server.security_api import get_token_api_key

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/api/v1/rpc/http",
    responses={
        200: {"model": RPCHypertextResponse, "description": ""},
    },
    tags=["rpc"],
    response_model_by_alias=True,
)
async def post_v1_rpc_http(
    rpc_hypertext_request: RPCHypertextRequest = Body(None, description=""),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> RPCHypertextResponse:
    if not BaseRpcApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseRpcApi.subclasses[0]().post_v1_rpc_http(rpc_hypertext_request)


@router.get(
    "/api/v1/rpc/ws/{target}",
    responses={
    },
    tags=["rpc"],
    response_model_by_alias=True,
)
async def get_v1_rpc_ws_target(
    target: RPCTarget = Path(..., description=""),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> None:
    if not BaseRpcApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseRpcApi.subclasses[0]().get_v1_rpc_ws_target(target)
