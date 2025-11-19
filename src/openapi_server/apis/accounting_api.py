# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.accounting_api_base import BaseAccountingApi
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
from datetime import date
from pydantic import Field, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.accounting_response import AccountingResponse
from openapi_server.models.coldkey_report_response import ColdkeyReportResponse
from openapi_server.models.network import Network
from openapi_server.models.tax_response import TaxResponse
from openapi_server.models.tax_token_response import TaxTokenResponse
from openapi_server.security_api import get_token_api_key

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/accounting/coldkey_report/v1",
    responses={
        200: {"model": ColdkeyReportResponse, "description": "Coldkey report retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Coldkey report not found"},
        500: {"description": "Internal server error"},
    },
    tags=["accounting"],
    response_model_by_alias=True,
)
async def get_accounting_coldkey_report(
    date_start: Annotated[date, Field(description="Start of date range in YYYY-MM-DD format (inclusive)")] = Query(None, description="Start of date range in YYYY-MM-DD format (inclusive)", alias="date_start"),
    date_end: Annotated[date, Field(description="End of date range in YYYY-MM-DD format (inclusive). Must be within 12 calendar months of date_start.")] = Query(None, description="End of date range in YYYY-MM-DD format (inclusive). Must be within 12 calendar months of date_start.", alias="date_end"),
    coldkey: Annotated[StrictStr, Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="coldkey"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> ColdkeyReportResponse:
    if not BaseAccountingApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAccountingApi.subclasses[0]().get_accounting_coldkey_report(date_start, date_end, coldkey)


@router.get(
    "/api/accounting/coldkey_report_csv/v1",
    responses={
        200: {"description": "Coldkey report retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Coldkey report not found"},
        500: {"description": "Internal server error"},
    },
    tags=["accounting"],
    response_model_by_alias=True,
)
async def get_accounting_coldkey_report_csv(
    date_start: Annotated[date, Field(description="Start of date range in YYYY-MM-DD format (inclusive)")] = Query(None, description="Start of date range in YYYY-MM-DD format (inclusive)", alias="date_start"),
    date_end: Annotated[date, Field(description="End of date range in YYYY-MM-DD format (inclusive). Must be within 12 calendar months of date_start.")] = Query(None, description="End of date range in YYYY-MM-DD format (inclusive). Must be within 12 calendar months of date_start.", alias="date_end"),
    coldkey: Annotated[StrictStr, Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="coldkey"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> None:
    if not BaseAccountingApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAccountingApi.subclasses[0]().get_accounting_coldkey_report_csv(date_start, date_end, coldkey)


@router.get(
    "/api/accounting/tax/v1",
    responses={
        200: {"model": TaxResponse, "description": "Tax report retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Tax report not found"},
        500: {"description": "Internal server error"},
    },
    tags=["accounting"],
    response_model_by_alias=True,
)
async def get_accounting_tax(
    token: Annotated[StrictStr, Field(description="TAO or SN1, SN2, etc.")] = Query(None, description="TAO or SN1, SN2, etc.", alias="token"),
    date_start: Annotated[date, Field(description="Start of date range in YYYY-MM-DD format (inclusive)")] = Query(None, description="Start of date range in YYYY-MM-DD format (inclusive)", alias="date_start"),
    date_end: Annotated[date, Field(description="End of date range in YYYY-MM-DD format (inclusive). Must be within 12 calendar months of date_start.")] = Query(None, description="End of date range in YYYY-MM-DD format (inclusive). Must be within 12 calendar months of date_start.", alias="date_end"),
    coldkey: Annotated[StrictStr, Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="coldkey"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> TaxResponse:
    if not BaseAccountingApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAccountingApi.subclasses[0]().get_accounting_tax(token, date_start, date_end, coldkey)


@router.get(
    "/api/accounting/tax_csv/v1",
    responses={
        200: {"description": "Tax report retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Tax report not found"},
        500: {"description": "Internal server error"},
    },
    tags=["accounting"],
    response_model_by_alias=True,
)
async def get_accounting_tax_csv(
    token: Annotated[StrictStr, Field(description="TAO or SN1, SN2, etc.")] = Query(None, description="TAO or SN1, SN2, etc.", alias="token"),
    date_start: Annotated[date, Field(description="Start of date range in YYYY-MM-DD format (inclusive)")] = Query(None, description="Start of date range in YYYY-MM-DD format (inclusive)", alias="date_start"),
    date_end: Annotated[date, Field(description="End of date range in YYYY-MM-DD format (inclusive). Must be within 12 calendar months of date_start.")] = Query(None, description="End of date range in YYYY-MM-DD format (inclusive). Must be within 12 calendar months of date_start.", alias="date_end"),
    coldkey: Annotated[StrictStr, Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="coldkey"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> None:
    if not BaseAccountingApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAccountingApi.subclasses[0]().get_accounting_tax_csv(token, date_start, date_end, coldkey)


@router.get(
    "/api/accounting/tax_token/v1",
    responses={
        200: {"model": TaxTokenResponse, "description": "Tokens retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Tokens not found"},
        500: {"description": "Internal server error"},
    },
    tags=["accounting"],
    response_model_by_alias=True,
)
async def get_accounting_tax_token(
    date_start: Annotated[date, Field(description="Start of date range in YYYY-MM-DD format (inclusive)")] = Query(None, description="Start of date range in YYYY-MM-DD format (inclusive)", alias="date_start"),
    date_end: Annotated[date, Field(description="End of date range in YYYY-MM-DD format (inclusive). Must be within 12 calendar months of date_start.")] = Query(None, description="End of date range in YYYY-MM-DD format (inclusive). Must be within 12 calendar months of date_start.", alias="date_end"),
    coldkey: Annotated[StrictStr, Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="coldkey"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> TaxTokenResponse:
    if not BaseAccountingApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAccountingApi.subclasses[0]().get_accounting_tax_token(date_start, date_end, coldkey)


@router.get(
    "/api/accounting/v1",
    responses={
        200: {"model": AccountingResponse, "description": "Accounting retrieved successfully"},
        400: {"description": "Bad request"},
        404: {"description": "Accounting not found"},
        500: {"description": "Internal server error"},
    },
    tags=["accounting"],
    response_model_by_alias=True,
)
async def get_accounting(
    date_start: Annotated[date, Field(description="Start of date range in YYYY-MM-DD format (inclusive)")] = Query(None, description="Start of date range in YYYY-MM-DD format (inclusive)", alias="date_start"),
    date_end: Annotated[date, Field(description="End of date range in YYYY-MM-DD format (inclusive)")] = Query(None, description="End of date range in YYYY-MM-DD format (inclusive)", alias="date_end"),
    coldkey: Annotated[StrictStr, Field(description="SS58 or hex format")] = Query(None, description="SS58 or hex format", alias="coldkey"),
    hotkey: Optional[StrictStr] = Query(None, description="", alias="hotkey"),
    network: Optional[Network] = Query(None, description="", alias="network"),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> AccountingResponse:
    if not BaseAccountingApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAccountingApi.subclasses[0]().get_accounting(date_start, date_end, coldkey, hotkey, network)
