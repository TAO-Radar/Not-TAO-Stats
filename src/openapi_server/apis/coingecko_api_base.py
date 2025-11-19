# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing import Any
from typing_extensions import Annotated
from openapi_server.models.coin_gecko_asset_response import CoinGeckoAssetResponse
from openapi_server.models.coin_gecko_events_response import CoinGeckoEventsResponse
from openapi_server.models.coin_gecko_latest_block_response import CoinGeckoLatestBlockResponse
from openapi_server.models.coin_gecko_pair_response import CoinGeckoPairResponse
from openapi_server.security_api import get_token_api_key

class BaseCoingeckoApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseCoingeckoApi.subclasses = BaseCoingeckoApi.subclasses + (cls,)
    async def get_coingecko_asset(
        self,
        id: Annotated[StrictStr, Field(description="integer")],
    ) -> CoinGeckoAssetResponse:
        ...


    async def get_coingecko_events(
        self,
        from_block: int,
        to_block: int,
    ) -> CoinGeckoEventsResponse:
        ...


    async def get_coingecko_latest_block(
        self,
    ) -> CoinGeckoLatestBlockResponse:
        ...


    async def get_coingecko_pair(
        self,
        id: StrictStr,
    ) -> CoinGeckoPairResponse:
        ...
