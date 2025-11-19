# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.identity_history_order import IdentityHistoryOrder
from openapi_server.models.identity_history_response import IdentityHistoryResponse
from openapi_server.models.identity_response import IdentityResponse
from openapi_server.security_api import get_token_api_key

class BaseIdentityApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseIdentityApi.subclasses = BaseIdentityApi.subclasses + (cls,)
    async def get_identity_history(
        self,
        address: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[IdentityHistoryOrder],
    ) -> IdentityHistoryResponse:
        ...


    async def get_identity_latest(
        self,
        address: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        validator_hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        page: Optional[int],
        limit: Optional[int],
    ) -> IdentityResponse:
        ...
