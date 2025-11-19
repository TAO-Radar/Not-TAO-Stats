# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictBool, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.metagraph_history_order import MetagraphHistoryOrder  # noqa: F401
from openapi_server.models.metagraph_history_response import MetagraphHistoryResponse  # noqa: F401
from openapi_server.models.metagraph_order import MetagraphOrder  # noqa: F401
from openapi_server.models.metagraph_response import MetagraphResponse  # noqa: F401
from openapi_server.models.root_metagraph_history_order import RootMetagraphHistoryOrder  # noqa: F401
from openapi_server.models.root_metagraph_history_response import RootMetagraphHistoryResponse  # noqa: F401
from openapi_server.models.root_metagraph_order import RootMetagraphOrder  # noqa: F401
from openapi_server.models.root_metagraph_response import RootMetagraphResponse  # noqa: F401


def test_get_metagraph_history(client: TestClient):
    """Test case for get_metagraph_history

    
    """
    params = [("netuid", 56),     ("uid", 56),     ("hotkey", 'hotkey_example'),     ("coldkey", 'coldkey_example'),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.MetagraphHistoryOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/metagraph/history/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_metagraph_latest(client: TestClient):
    """Test case for get_metagraph_latest

    
    """
    params = [("netuid", 56),     ("search", 'search_example'),     ("uid", 56),     ("active", True),     ("hotkey", 'hotkey_example'),     ("coldkey", 'coldkey_example'),     ("validator_permit", True),     ("is_immunity_period", True),     ("is_child_key", True),     ("page", 56),     ("limit", 56),     ("order", openapi_server.MetagraphOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/metagraph/latest/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_metagraph_root_history(client: TestClient):
    """Test case for get_metagraph_root_history

    
    """
    params = [("hotkey", 'hotkey_example'),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.RootMetagraphHistoryOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/metagraph/root/history/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_metagraph_root_latest(client: TestClient):
    """Test case for get_metagraph_root_latest

    
    """
    params = [("hotkey", 'hotkey_example'),     ("page", 56),     ("limit", 56),     ("order", openapi_server.RootMetagraphOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/metagraph/root/latest/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

