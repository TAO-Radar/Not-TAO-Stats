# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.dev_activity_api_base import BaseDevActivityApi
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
from openapi_server.models.dev_activity_history_response import DevActivityHistoryResponse
from openapi_server.models.dev_activity_latest_order import DevActivityLatestOrder
from openapi_server.models.dev_activity_latest_response import DevActivityLatestResponse
from openapi_server.security_api import get_token_api_key

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/dev_activity/history/v1",
    responses={
        200: {"model": DevActivityHistoryResponse, "description": "Dev activity history"},
        400: {"description": "Bad request"},
        500: {"description": "Internal server error"},
    },
    tags=["dev_activity"],
    response_model_by_alias=True,
)
async def get_dev_activity_history(
    netuid: Annotated[Optional[StrictStr], Field(description="CSV of netuids (e.g. 1,2,3)")] = Query(None, description="CSV of netuids (e.g. 1,2,3)", alias="netuid"),
    date_start: Annotated[Optional[StrictStr], Field(description="Start date inclusive (YYYY-MM-DD)")] = Query(None, description="Start date inclusive (YYYY-MM-DD)", alias="date_start"),
    date_end: Annotated[Optional[StrictStr], Field(description="End date inclusive (YYYY-MM-DD)")] = Query(None, description="End date inclusive (YYYY-MM-DD)", alias="date_end"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DevActivityHistoryResponse:
    if not BaseDevActivityApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDevActivityApi.subclasses[0]().get_dev_activity_history(netuid, date_start, date_end)


@router.get(
    "/api/dev_activity/latest/v1",
    responses={
        200: {"model": DevActivityLatestResponse, "description": "Dev activity latest"},
        400: {"description": "Bad request"},
        500: {"description": "Internal server error"},
    },
    tags=["dev_activity"],
    response_model_by_alias=True,
)
async def get_dev_activity_latest(
    netuid: Optional[StrictStr] = Query(None, description="", alias="netuid"),
    days_since_last_event_max: Optional[int] = Query(None, description="", alias="days_since_last_event_max"),
    order: Optional[DevActivityLatestOrder] = Query(None, description="", alias="order"),
    page: Optional[int] = Query(None, description="", alias="page"),
    limit: Optional[int] = Query(None, description="", alias="limit"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> DevActivityLatestResponse:
    if not BaseDevActivityApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDevActivityApi.subclasses[0]().get_dev_activity_latest(netuid, days_since_last_event_max, order, page, limit)
