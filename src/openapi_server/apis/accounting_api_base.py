# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

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

class BaseAccountingApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseAccountingApi.subclasses = BaseAccountingApi.subclasses + (cls,)
    async def get_accounting_coldkey_report(
        self,
        date_start: Annotated[date, Field(description="Start of date range in YYYY-MM-DD format (inclusive)")],
        date_end: Annotated[date, Field(description="End of date range in YYYY-MM-DD format (inclusive). Must be within 12 calendar months of date_start.")],
        coldkey: Annotated[StrictStr, Field(description="SS58 or hex format")],
    ) -> ColdkeyReportResponse:
        ...


    async def get_accounting_coldkey_report_csv(
        self,
        date_start: Annotated[date, Field(description="Start of date range in YYYY-MM-DD format (inclusive)")],
        date_end: Annotated[date, Field(description="End of date range in YYYY-MM-DD format (inclusive). Must be within 12 calendar months of date_start.")],
        coldkey: Annotated[StrictStr, Field(description="SS58 or hex format")],
    ) -> None:
        ...


    async def get_accounting_tax(
        self,
        token: Annotated[StrictStr, Field(description="TAO or SN1, SN2, etc.")],
        date_start: Annotated[date, Field(description="Start of date range in YYYY-MM-DD format (inclusive)")],
        date_end: Annotated[date, Field(description="End of date range in YYYY-MM-DD format (inclusive). Must be within 12 calendar months of date_start.")],
        coldkey: Annotated[StrictStr, Field(description="SS58 or hex format")],
    ) -> TaxResponse:
        ...


    async def get_accounting_tax_csv(
        self,
        token: Annotated[StrictStr, Field(description="TAO or SN1, SN2, etc.")],
        date_start: Annotated[date, Field(description="Start of date range in YYYY-MM-DD format (inclusive)")],
        date_end: Annotated[date, Field(description="End of date range in YYYY-MM-DD format (inclusive). Must be within 12 calendar months of date_start.")],
        coldkey: Annotated[StrictStr, Field(description="SS58 or hex format")],
    ) -> None:
        ...


    async def get_accounting_tax_token(
        self,
        date_start: Annotated[date, Field(description="Start of date range in YYYY-MM-DD format (inclusive)")],
        date_end: Annotated[date, Field(description="End of date range in YYYY-MM-DD format (inclusive). Must be within 12 calendar months of date_start.")],
        coldkey: Annotated[StrictStr, Field(description="SS58 or hex format")],
    ) -> TaxTokenResponse:
        ...


    async def get_accounting(
        self,
        date_start: Annotated[date, Field(description="Start of date range in YYYY-MM-DD format (inclusive)")],
        date_end: Annotated[date, Field(description="End of date range in YYYY-MM-DD format (inclusive)")],
        coldkey: Annotated[StrictStr, Field(description="SS58 or hex format")],
        hotkey: Optional[StrictStr],
        network: Optional[Network],
    ) -> AccountingResponse:
        ...
