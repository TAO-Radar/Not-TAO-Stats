# coding: utf-8

from fastapi.testclient import TestClient


from typing import Any  # noqa: F401
from openapi_server.models.network_parameter_response import NetworkParameterResponse  # noqa: F401


def test_get_network_parameter_latest(client: TestClient):
    """Test case for get_network_parameter_latest

    
    """

    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/network_parameter/latest/v1",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

