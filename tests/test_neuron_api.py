# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictBool, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.neuron_aggregated_history_order import NeuronAggregatedHistoryOrder  # noqa: F401
from openapi_server.models.neuron_aggregated_latest_order import NeuronAggregatedLatestOrder  # noqa: F401
from openapi_server.models.neuron_aggregated_response import NeuronAggregatedResponse  # noqa: F401
from openapi_server.models.neuron_history_order import NeuronHistoryOrder  # noqa: F401
from openapi_server.models.neuron_incentive_distribution_response import NeuronIncentiveDistributionResponse  # noqa: F401
from openapi_server.models.neuron_latest_order import NeuronLatestOrder  # noqa: F401
from openapi_server.models.neuron_response import NeuronResponse  # noqa: F401


def test_get_neuron_aggregated_history(client: TestClient):
    """Test case for get_neuron_aggregated_history

    
    """
    params = [("netuid", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.NeuronAggregatedHistoryOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/neuron/aggregated/history/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_neuron_aggregated_latest(client: TestClient):
    """Test case for get_neuron_aggregated_latest

    
    """
    params = [("netuid", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.NeuronAggregatedLatestOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/neuron/aggregated/latest/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_neuron_history(client: TestClient):
    """Test case for get_neuron_history

    
    """
    params = [("netuid", 56),     ("uid", 56),     ("hotkey", 'hotkey_example'),     ("coldkey", 'coldkey_example'),     ("is_immune", True),     ("in_danger", True),     ("has_dividends", True),     ("has_incentive", True),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.NeuronHistoryOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/neuron/history/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_neuron_incentive_distribution(client: TestClient):
    """Test case for get_neuron_incentive_distribution

    
    """
    params = [("netuid", 56),     ("days", 56)]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/neuron/incentive_distribution/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_neuron_latest(client: TestClient):
    """Test case for get_neuron_latest

    
    """
    params = [("netuid", 56),     ("uid", 56),     ("hotkey", 'hotkey_example'),     ("coldkey", 'coldkey_example'),     ("is_immune", True),     ("in_danger", True),     ("has_dividends", True),     ("has_incentive", True),     ("page", 56),     ("limit", 56),     ("order", openapi_server.NeuronLatestOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/neuron/latest/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

