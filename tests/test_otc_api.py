# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from openapi_server.models.frozen_status import FrozenStatus  # noqa: F401
from openapi_server.models.listing_event_type import ListingEventType  # noqa: F401
from openapi_server.models.listing_status import ListingStatus  # noqa: F401
from openapi_server.models.offer_event_type import OfferEventType  # noqa: F401
from openapi_server.models.offer_status import OfferStatus  # noqa: F401
from openapi_server.models.otc_listing_history_order import OtcListingHistoryOrder  # noqa: F401
from openapi_server.models.otc_listing_history_response import OtcListingHistoryResponse  # noqa: F401
from openapi_server.models.otc_listing_order import OtcListingOrder  # noqa: F401
from openapi_server.models.otc_listing_response import OtcListingResponse  # noqa: F401
from openapi_server.models.otc_offer_history_order import OtcOfferHistoryOrder  # noqa: F401
from openapi_server.models.otc_offer_history_response import OtcOfferHistoryResponse  # noqa: F401
from openapi_server.models.otc_offer_order import OtcOfferOrder  # noqa: F401
from openapi_server.models.otc_offer_response import OtcOfferResponse  # noqa: F401
from openapi_server.models.otc_subnet_status_order import OtcSubnetStatusOrder  # noqa: F401
from openapi_server.models.otc_subnet_status_response import OtcSubnetStatusResponse  # noqa: F401
from openapi_server.models.otc_trade_order import OtcTradeOrder  # noqa: F401
from openapi_server.models.otc_trade_response import OtcTradeResponse  # noqa: F401
from openapi_server.models.otc_user_stats_order import OtcUserStatsOrder  # noqa: F401
from openapi_server.models.otc_user_stats_response import OtcUserStatsResponse  # noqa: F401
from openapi_server.models.trade_type import TradeType  # noqa: F401


def test_get_otc_listing_history(client: TestClient):
    """Test case for get_otc_listing_history

    
    """
    params = [("listing_id", 'listing_id_example'),     ("event_type", openapi_server.ListingEventType()),     ("seller", 'seller_example'),     ("buyer", 'buyer_example'),     ("hotkey", 'hotkey_example'),     ("netuid", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.OtcListingHistoryOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/otc/listing/history/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_otc_listing(client: TestClient):
    """Test case for get_otc_listing

    
    """
    params = [("listing_id", 'listing_id_example'),     ("seller", 'seller_example'),     ("hotkey", 'hotkey_example'),     ("netuid", 56),     ("status", openapi_server.ListingStatus()),     ("price_min", 'price_min_example'),     ("price_max", 'price_max_example'),     ("amount_min", 'amount_min_example'),     ("amount_max", 'amount_max_example'),     ("created_block_start", 56),     ("created_block_end", 56),     ("created_timestamp_start", 56),     ("created_timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.OtcListingOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/otc/listing/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_otc_offer_history(client: TestClient):
    """Test case for get_otc_offer_history

    
    """
    params = [("offer_id", 'offer_id_example'),     ("event_type", openapi_server.OfferEventType()),     ("buyer", 'buyer_example'),     ("seller", 'seller_example'),     ("netuid", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.OtcOfferHistoryOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/otc/offer/history/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_otc_offer(client: TestClient):
    """Test case for get_otc_offer

    
    """
    params = [("offer_id", 'offer_id_example'),     ("buyer", 'buyer_example'),     ("netuid", 56),     ("status", openapi_server.OfferStatus()),     ("price_min", 'price_min_example'),     ("price_max", 'price_max_example'),     ("amount_min", 'amount_min_example'),     ("amount_max", 'amount_max_example'),     ("created_block_start", 56),     ("created_block_end", 56),     ("created_timestamp_start", 56),     ("created_timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.OtcOfferOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/otc/offer/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_otc_subnet_status(client: TestClient):
    """Test case for get_otc_subnet_status

    
    """
    params = [("netuid", 56),     ("frozen", openapi_server.FrozenStatus()),     ("page", 56),     ("limit", 56),     ("order", openapi_server.OtcSubnetStatusOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/otc/subnet/status/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_otc_trade(client: TestClient):
    """Test case for get_otc_trade

    
    """
    params = [("trade_type", openapi_server.TradeType()),     ("seller", 'seller_example'),     ("buyer", 'buyer_example'),     ("netuid", 56),     ("listing_id", 'listing_id_example'),     ("offer_id", 'offer_id_example'),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.OtcTradeOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/otc/trade/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_otc_user_stats(client: TestClient):
    """Test case for get_otc_user_stats

    
    """
    params = [("account", 'account_example'),     ("netuid", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.OtcUserStatsOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/otc/user/stats/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

