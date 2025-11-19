# coding: utf-8

from fastapi.testclient import TestClient


from typing import Any, Optional  # noqa: F401
from openapi_server.models.exchange_response import ExchangeResponse  # noqa: F401


def test_get_exchange(client: TestClient):
    """Test case for get_exchange

    
    """
    params = [("page", 56),     ("limit", 56)]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/exchange/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

