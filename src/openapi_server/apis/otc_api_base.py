# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import StrictStr
from typing import Any, Optional
from openapi_server.models.frozen_status import FrozenStatus
from openapi_server.models.listing_event_type import ListingEventType
from openapi_server.models.listing_status import ListingStatus
from openapi_server.models.offer_event_type import OfferEventType
from openapi_server.models.offer_status import OfferStatus
from openapi_server.models.otc_listing_history_order import OtcListingHistoryOrder
from openapi_server.models.otc_listing_history_response import OtcListingHistoryResponse
from openapi_server.models.otc_listing_order import OtcListingOrder
from openapi_server.models.otc_listing_response import OtcListingResponse
from openapi_server.models.otc_offer_history_order import OtcOfferHistoryOrder
from openapi_server.models.otc_offer_history_response import OtcOfferHistoryResponse
from openapi_server.models.otc_offer_order import OtcOfferOrder
from openapi_server.models.otc_offer_response import OtcOfferResponse
from openapi_server.models.otc_subnet_status_order import OtcSubnetStatusOrder
from openapi_server.models.otc_subnet_status_response import OtcSubnetStatusResponse
from openapi_server.models.otc_trade_order import OtcTradeOrder
from openapi_server.models.otc_trade_response import OtcTradeResponse
from openapi_server.models.otc_user_stats_order import OtcUserStatsOrder
from openapi_server.models.otc_user_stats_response import OtcUserStatsResponse
from openapi_server.models.trade_type import TradeType
from openapi_server.security_api import get_token_api_key

class BaseOtcApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseOtcApi.subclasses = BaseOtcApi.subclasses + (cls,)
    async def get_otc_listing_history(
        self,
        listing_id: Optional[StrictStr],
        event_type: Optional[ListingEventType],
        seller: Optional[StrictStr],
        buyer: Optional[StrictStr],
        hotkey: Optional[StrictStr],
        netuid: Optional[int],
        block_start: Optional[int],
        block_end: Optional[int],
        timestamp_start: Optional[int],
        timestamp_end: Optional[int],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[OtcListingHistoryOrder],
    ) -> OtcListingHistoryResponse:
        ...


    async def get_otc_listing(
        self,
        listing_id: Optional[StrictStr],
        seller: Optional[StrictStr],
        hotkey: Optional[StrictStr],
        netuid: Optional[int],
        status: Optional[ListingStatus],
        price_min: Optional[StrictStr],
        price_max: Optional[StrictStr],
        amount_min: Optional[StrictStr],
        amount_max: Optional[StrictStr],
        created_block_start: Optional[int],
        created_block_end: Optional[int],
        created_timestamp_start: Optional[int],
        created_timestamp_end: Optional[int],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[OtcListingOrder],
    ) -> OtcListingResponse:
        ...


    async def get_otc_offer_history(
        self,
        offer_id: Optional[StrictStr],
        event_type: Optional[OfferEventType],
        buyer: Optional[StrictStr],
        seller: Optional[StrictStr],
        netuid: Optional[int],
        block_start: Optional[int],
        block_end: Optional[int],
        timestamp_start: Optional[int],
        timestamp_end: Optional[int],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[OtcOfferHistoryOrder],
    ) -> OtcOfferHistoryResponse:
        ...


    async def get_otc_offer(
        self,
        offer_id: Optional[StrictStr],
        buyer: Optional[StrictStr],
        netuid: Optional[int],
        status: Optional[OfferStatus],
        price_min: Optional[StrictStr],
        price_max: Optional[StrictStr],
        amount_min: Optional[StrictStr],
        amount_max: Optional[StrictStr],
        created_block_start: Optional[int],
        created_block_end: Optional[int],
        created_timestamp_start: Optional[int],
        created_timestamp_end: Optional[int],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[OtcOfferOrder],
    ) -> OtcOfferResponse:
        ...


    async def get_otc_subnet_status(
        self,
        netuid: Optional[int],
        frozen: Optional[FrozenStatus],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[OtcSubnetStatusOrder],
    ) -> OtcSubnetStatusResponse:
        ...


    async def get_otc_trade(
        self,
        trade_type: Optional[TradeType],
        seller: Optional[StrictStr],
        buyer: Optional[StrictStr],
        netuid: Optional[int],
        listing_id: Optional[StrictStr],
        offer_id: Optional[StrictStr],
        block_start: Optional[int],
        block_end: Optional[int],
        timestamp_start: Optional[int],
        timestamp_end: Optional[int],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[OtcTradeOrder],
    ) -> OtcTradeResponse:
        ...


    async def get_otc_user_stats(
        self,
        account: Optional[StrictStr],
        netuid: Optional[int],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[OtcUserStatsOrder],
    ) -> OtcUserStatsResponse:
        ...
