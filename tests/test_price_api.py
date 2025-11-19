# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.price_history_order import PriceHistoryOrder  # noqa: F401
from openapi_server.models.price_ohlc_period import PriceOHLCPeriod  # noqa: F401
from openapi_server.models.price_ohlc_response import PriceOHLCResponse  # noqa: F401
from openapi_server.models.price_response import PriceResponse  # noqa: F401
from openapi_server.models.price_simple_response import PriceSimpleResponse  # noqa: F401


def test_get_price_history(client: TestClient):
    """Test case for get_price_history

    
    """
    params = [("asset", 'asset_example'),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.PriceHistoryOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/price/history/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_price_latest(client: TestClient):
    """Test case for get_price_latest

    
    """
    params = [("asset", 'asset_example')]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/price/latest/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_price_ohlc(client: TestClient):
    """Test case for get_price_ohlc

    
    """
    params = [("asset", 'asset_example'),     ("period", openapi_server.PriceOHLCPeriod()),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56)]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/price/ohlc/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_price_simple_latest(client: TestClient):
    """Test case for get_price_simple_latest

    
    """

    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/price/simple/latest/v1",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

