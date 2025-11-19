# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.coldkey_swap_api_base import BaseColdkeySwapApi
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
from openapi_server.models.pending_coldkey_swap_response import PendingColdkeySwapResponse
from openapi_server.security_api import get_token_api_key

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/pending_coldkey_swap/v1",
    responses={
        200: {"model": PendingColdkeySwapResponse, "description": "Pending coldkey swaps retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Pending coldkey swaps not found"},
        500: {"description": "Internal server error"},
    },
    tags=["coldkey_swap"],
    response_model_by_alias=True,
)
async def get_pending_coldkey_swap(
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> PendingColdkeySwapResponse:
    if not BaseColdkeySwapApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseColdkeySwapApi.subclasses[0]().get_pending_coldkey_swap()
