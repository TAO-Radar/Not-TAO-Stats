# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.status_response import StatusResponse  # noqa: F401


def test_get_status(client: TestClient):
    """Test case for get_status

    
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/status/v1",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

