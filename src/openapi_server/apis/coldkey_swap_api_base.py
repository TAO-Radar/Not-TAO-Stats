# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from typing import Any
from openapi_server.models.pending_coldkey_swap_response import PendingColdkeySwapResponse
from openapi_server.security_api import get_token_api_key

class BaseColdkeySwapApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseColdkeySwapApi.subclasses = BaseColdkeySwapApi.subclasses + (cls,)
    async def get_pending_coldkey_swap(
        self,
    ) -> PendingColdkeySwapResponse:
        ...
