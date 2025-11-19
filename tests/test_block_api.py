# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.block_emission_order import BlockEmissionOrder  # noqa: F401
from openapi_server.models.block_emission_response import BlockEmissionResponse  # noqa: F401
from openapi_server.models.block_interval_order import BlockIntervalOrder  # noqa: F401
from openapi_server.models.block_interval_response import BlockIntervalResponse  # noqa: F401
from openapi_server.models.block_order import BlockOrder  # noqa: F401
from openapi_server.models.block_response import BlockResponse  # noqa: F401
from openapi_server.models.frequency_hour_day import FrequencyHourDay  # noqa: F401


def test_get_block_emission(client: TestClient):
    """Test case for get_block_emission

    
    """
    params = [("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.BlockEmissionOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/block/emission/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_block_interval(client: TestClient):
    """Test case for get_block_interval

    
    """
    params = [("timestamp_start", 56),     ("timestamp_end", 56),     ("frequency", openapi_server.FrequencyHourDay()),     ("page", 56),     ("limit", 56),     ("order", openapi_server.BlockIntervalOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/block/interval/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_block(client: TestClient):
    """Test case for get_block

    
    """
    params = [("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("hash", 'hash_example'),     ("spec_version", 56),     ("validator", 'validator_example'),     ("page", 56),     ("limit", 56),     ("order", openapi_server.BlockOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/block/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

