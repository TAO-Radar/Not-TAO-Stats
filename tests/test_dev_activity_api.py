# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.dev_activity_history_response import DevActivityHistoryResponse  # noqa: F401
from openapi_server.models.dev_activity_latest_order import DevActivityLatestOrder  # noqa: F401
from openapi_server.models.dev_activity_latest_response import DevActivityLatestResponse  # noqa: F401


def test_get_dev_activity_history(client: TestClient):
    """Test case for get_dev_activity_history

    
    """
    params = [("netuid", '1,16,21'),     ("date_start", '2025-01-01'),     ("date_end", '2025-01-31')]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dev_activity/history/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dev_activity_latest(client: TestClient):
    """Test case for get_dev_activity_latest

    
    """
    params = [("netuid", 'netuid_example'),     ("days_since_last_event_max", 56),     ("order", openapi_server.DevActivityLatestOrder()),     ("page", 56),     ("limit", 56)]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dev_activity/latest/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

