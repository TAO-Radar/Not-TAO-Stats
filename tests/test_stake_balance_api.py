# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.stake_balance_history_order import StakeBalanceHistoryOrder  # noqa: F401
from openapi_server.models.stake_balance_response import StakeBalanceResponse  # noqa: F401


def test_get_stake_balance_history(client: TestClient):
    """Test case for get_stake_balance_history

    
    """
    params = [("coldkey", 'coldkey_example'),     ("hotkey", 'hotkey_example'),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.StakeBalanceHistoryOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/stake_balance/history/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

