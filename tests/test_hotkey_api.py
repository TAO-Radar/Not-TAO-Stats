# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.hotkey_family_history_order import HotkeyFamilyHistoryOrder  # noqa: F401
from openapi_server.models.hotkey_family_response import HotkeyFamilyResponse  # noqa: F401


def test_get_hotkey_family_history(client: TestClient):
    """Test case for get_hotkey_family_history

    
    """
    params = [("hotkey", 'hotkey_example'),     ("netuid", 56),     ("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.HotkeyFamilyHistoryOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/hotkey/family/history/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_hotkey_family_latest(client: TestClient):
    """Test case for get_hotkey_family_latest

    
    """
    params = [("hotkey", 'hotkey_example'),     ("netuid", 56),     ("page", 56),     ("limit", 56)]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/hotkey/family/latest/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

