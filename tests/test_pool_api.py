# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.dtao_pool_history_order import DtaoPoolHistoryOrder  # noqa: F401
from openapi_server.models.dtao_pool_history_response import DtaoPoolHistoryResponse  # noqa: F401
from openapi_server.models.dtao_pool_order import DtaoPoolOrder  # noqa: F401
from openapi_server.models.dtao_pool_response import DtaoPoolResponse  # noqa: F401
from openapi_server.models.dtao_pool_total_price_history_order import DtaoPoolTotalPriceHistoryOrder  # noqa: F401
from openapi_server.models.dtao_pool_total_price_history_response import DtaoPoolTotalPriceHistoryResponse  # noqa: F401
from openapi_server.models.dtao_pool_total_price_latest_response import DtaoPoolTotalPriceLatestResponse  # noqa: F401
from openapi_server.models.frequency_block_hour_day import FrequencyBlockHourDay  # noqa: F401


def test_get_dtao_pool_history(client: TestClient):
    """Test case for get_dtao_pool_history

    
    """
    params = [("netuid", 56),     ("frequency", openapi_server.FrequencyBlockHourDay()),     ("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.DtaoPoolHistoryOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/pool/history/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_pool_latest(client: TestClient):
    """Test case for get_dtao_pool_latest

    
    """
    params = [("netuid", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.DtaoPoolOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/pool/latest/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_pool_total_price_history(client: TestClient):
    """Test case for get_dtao_pool_total_price_history

    
    """
    params = [("frequency", openapi_server.FrequencyBlockHourDay()),     ("page", 56),     ("limit", 56),     ("order", openapi_server.DtaoPoolTotalPriceHistoryOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/pool/total_price/history/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_pool_total_price_latest(client: TestClient):
    """Test case for get_dtao_pool_total_price_latest

    
    """

    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/pool/total_price/latest/v1",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_pool_total_price(client: TestClient):
    """Test case for get_dtao_pool_total_price

    
    """
    params = [("frequency", openapi_server.FrequencyBlockHourDay()),     ("page", 56),     ("limit", 56),     ("order", openapi_server.DtaoPoolTotalPriceHistoryOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/pool/total_price/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_pool(client: TestClient):
    """Test case for get_dtao_pool

    
    """
    params = [("netuid", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.DtaoPoolOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/pool/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

