# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.rpc_hypertext_request import RPCHypertextRequest  # noqa: F401
from openapi_server.models.rpc_hypertext_response import RPCHypertextResponse  # noqa: F401
from openapi_server.models.rpc_target import RPCTarget  # noqa: F401


def test_post_v1_rpc_http(client: TestClient):
    """Test case for post_v1_rpc_http

    
    """
    rpc_hypertext_request = {"request":{"method":"method","id":"","jsonrpc":"jsonrpc","params":""},"target":"finney_lite"}

    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/api/v1/rpc/http",
    #    headers=headers,
    #    json=rpc_hypertext_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_v1_rpc_ws_target(client: TestClient):
    """Test case for get_v1_rpc_ws_target

    
    """

    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/v1/rpc/ws/{target}".format(target=openapi_server.RPCTarget()),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

