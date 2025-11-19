# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.identity_history_order import IdentityHistoryOrder  # noqa: F401
from openapi_server.models.identity_history_response import IdentityHistoryResponse  # noqa: F401
from openapi_server.models.identity_response import IdentityResponse  # noqa: F401


def test_get_identity_history(client: TestClient):
    """Test case for get_identity_history

    
    """
    params = [("address", 'address_example'),     ("page", 56),     ("limit", 56),     ("order", openapi_server.IdentityHistoryOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/identity/history/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_identity_latest(client: TestClient):
    """Test case for get_identity_latest

    
    """
    params = [("address", 'address_example'),     ("validator_hotkey", 'validator_hotkey_example'),     ("page", 56),     ("limit", 56)]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/identity/latest/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

