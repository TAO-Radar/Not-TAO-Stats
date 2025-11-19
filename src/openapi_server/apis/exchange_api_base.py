# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from typing import Any, Optional
from openapi_server.models.exchange_response import ExchangeResponse
from openapi_server.security_api import get_token_api_key

class BaseExchangeApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseExchangeApi.subclasses = BaseExchangeApi.subclasses + (cls,)
    async def get_exchange(
        self,
        page: Optional[int],
        limit: Optional[int],
    ) -> ExchangeResponse:
        ...
