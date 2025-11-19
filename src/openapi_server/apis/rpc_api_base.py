# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from openapi_server.models.rpc_hypertext_request import RPCHypertextRequest
from openapi_server.models.rpc_hypertext_response import RPCHypertextResponse
from openapi_server.models.rpc_target import RPCTarget
from openapi_server.security_api import get_token_api_key

class BaseRpcApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseRpcApi.subclasses = BaseRpcApi.subclasses + (cls,)
    async def post_v1_rpc_http(
        self,
        rpc_hypertext_request: RPCHypertextRequest,
    ) -> RPCHypertextResponse:
        ...


    async def get_v1_rpc_ws_target(
        self,
        target: RPCTarget,
    ) -> None:
        ...
