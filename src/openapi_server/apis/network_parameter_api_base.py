# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from typing import Any
from openapi_server.models.network_parameter_response import NetworkParameterResponse
from openapi_server.security_api import get_token_api_key

class BaseNetworkParameterApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseNetworkParameterApi.subclasses = BaseNetworkParameterApi.subclasses + (cls,)
    async def get_network_parameter_latest(
        self,
    ) -> NetworkParameterResponse:
        ...
