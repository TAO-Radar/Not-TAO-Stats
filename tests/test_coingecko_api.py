# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Any  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.coin_gecko_asset_response import CoinGeckoAssetResponse  # noqa: F401
from openapi_server.models.coin_gecko_events_response import CoinGeckoEventsResponse  # noqa: F401
from openapi_server.models.coin_gecko_latest_block_response import CoinGeckoLatestBlockResponse  # noqa: F401
from openapi_server.models.coin_gecko_pair_response import CoinGeckoPairResponse  # noqa: F401


def test_get_coingecko_asset(client: TestClient):
    """Test case for get_coingecko_asset

    
    """
    params = [("id", 'id_example')]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/coingecko/asset",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_coingecko_events(client: TestClient):
    """Test case for get_coingecko_events

    
    """
    params = [("from_block", 56),     ("to_block", 56)]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/coingecko/events",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_coingecko_latest_block(client: TestClient):
    """Test case for get_coingecko_latest_block

    
    """

    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/coingecko/latest-block",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_coingecko_pair(client: TestClient):
    """Test case for get_coingecko_pair

    
    """
    params = [("id", 'id_example')]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/coingecko/pair",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

