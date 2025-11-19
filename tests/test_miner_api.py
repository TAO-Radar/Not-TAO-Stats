# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.miner_autostake_order import MinerAutostakeOrder  # noqa: F401
from openapi_server.models.miner_autostake_response import MinerAutostakeResponse  # noqa: F401
from openapi_server.models.miner_coldkey_response import MinerColdkeyResponse  # noqa: F401
from openapi_server.models.miner_weights_history_order import MinerWeightsHistoryOrder  # noqa: F401
from openapi_server.models.miner_weights_latest_order import MinerWeightsLatestOrder  # noqa: F401
from openapi_server.models.miner_weights_response import MinerWeightsResponse  # noqa: F401


def test_get_miner_autostake(client: TestClient):
    """Test case for get_miner_autostake

    
    """
    params = [("netuid", 56),     ("hotkey", 'hotkey_example'),     ("coldkey", 'coldkey_example'),     ("destination_hotkey", 'destination_hotkey_example'),     ("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.MinerAutostakeOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/miner/autostake/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_miner_coldkey(client: TestClient):
    """Test case for get_miner_coldkey

    
    """
    params = [("coldkey", 'coldkey_example'),     ("days", 56)]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/miner/coldkey/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_miner_weights_history(client: TestClient):
    """Test case for get_miner_weights_history

    
    """
    params = [("netuid", 56),     ("miner_uid", 56),     ("validator_uid", 56),     ("miner_hotkey", 'miner_hotkey_example'),     ("validator_hotkey", 'validator_hotkey_example'),     ("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.MinerWeightsHistoryOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/miner/weights/history/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_miner_weights_latest(client: TestClient):
    """Test case for get_miner_weights_latest

    
    """
    params = [("netuid", 56),     ("miner_uid", 56),     ("validator_uid", 56),     ("miner_hotkey", 'miner_hotkey_example'),     ("validator_hotkey", 'validator_hotkey_example'),     ("page", 56),     ("limit", 56),     ("order", openapi_server.MinerWeightsLatestOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/miner/weights/latest/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

