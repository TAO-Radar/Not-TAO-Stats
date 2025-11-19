# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.account_history_order import AccountHistoryOrder  # noqa: F401
from openapi_server.models.account_history_response import AccountHistoryResponse  # noqa: F401
from openapi_server.models.account_order import AccountOrder  # noqa: F401
from openapi_server.models.account_response import AccountResponse  # noqa: F401


def test_get_account_history(client: TestClient):
    """Test case for get_account_history

    
    """
    params = [("address", 'address_example'),     ("network", 'network_example'),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.AccountHistoryOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/account/history/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_account_latest(client: TestClient):
    """Test case for get_account_latest

    
    """
    params = [("address", 'address_example'),     ("balance_free_min", 'balance_free_min_example'),     ("balance_free_max", 'balance_free_max_example'),     ("balance_staked_min", 'balance_staked_min_example'),     ("balance_staked_max", 'balance_staked_max_example'),     ("balance_staked_root_min", 'balance_staked_root_min_example'),     ("balance_staked_root_max", 'balance_staked_root_max_example'),     ("balance_staked_alpha_as_tao_min", 'balance_staked_alpha_as_tao_min_example'),     ("balance_staked_alpha_as_tao_max", 'balance_staked_alpha_as_tao_max_example'),     ("balance_total_min", 'balance_total_min_example'),     ("balance_total_max", 'balance_total_max_example'),     ("rank", 56),     ("created_on_network", 'created_on_network_example'),     ("created_on_timestamp_start", 56),     ("created_on_timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.AccountOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/account/latest/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

