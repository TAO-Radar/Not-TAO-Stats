# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.status_api_base import BaseStatusApi
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
from openapi_server.models.status_response import StatusResponse


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/status/v1",
    responses={
        200: {"model": StatusResponse, "description": ""},
    },
    tags=["status"],
    response_model_by_alias=True,
)
async def get_status(
) -> StatusResponse:
    if not BaseStatusApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseStatusApi.subclasses[0]().get_status()
