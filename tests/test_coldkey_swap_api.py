# coding: utf-8

from fastapi.testclient import TestClient


from typing import Any  # noqa: F401
from openapi_server.models.pending_coldkey_swap_response import PendingColdkeySwapResponse  # noqa: F401


def test_get_pending_coldkey_swap(client: TestClient):
    """Test case for get_pending_coldkey_swap

    
    """

    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/pending_coldkey_swap/v1",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

