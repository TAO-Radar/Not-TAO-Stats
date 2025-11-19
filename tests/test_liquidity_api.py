# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictBool, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.dtao_liquidity_distribution_response import DtaoLiquidityDistributionResponse  # noqa: F401
from openapi_server.models.dtao_liquidity_position_event_order import DtaoLiquidityPositionEventOrder  # noqa: F401
from openapi_server.models.dtao_liquidity_position_event_response import DtaoLiquidityPositionEventResponse  # noqa: F401
from openapi_server.models.dtao_liquidity_position_history_order import DtaoLiquidityPositionHistoryOrder  # noqa: F401
from openapi_server.models.dtao_liquidity_position_history_response import DtaoLiquidityPositionHistoryResponse  # noqa: F401
from openapi_server.models.dtao_liquidity_position_order import DtaoLiquidityPositionOrder  # noqa: F401
from openapi_server.models.dtao_liquidity_position_response import DtaoLiquidityPositionResponse  # noqa: F401
from openapi_server.models.dtao_tick_to_price_response import DtaoTickToPriceResponse  # noqa: F401
from openapi_server.models.liquidity_position_status import LiquidityPositionStatus  # noqa: F401
from openapi_server.models.liquidity_position_type import LiquidityPositionType  # noqa: F401


def test_get_dtao_liquidity_distribution(client: TestClient):
    """Test case for get_dtao_liquidity_distribution

    
    """
    params = [("netuid", 56),     ("min_price", 'min_price_example'),     ("max_price", 'max_price_example'),     ("num_points", 56),     ("log_scale", True)]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/liquidity/distribution/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_liquidity_position_history(client: TestClient):
    """Test case for get_dtao_liquidity_position_history

    
    """
    params = [("position_id", 'position_id_example'),     ("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.DtaoLiquidityPositionHistoryOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/liquidity/position/history/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_liquidity_position(client: TestClient):
    """Test case for get_dtao_liquidity_position

    
    """
    params = [("id", 'id_example'),     ("coldkey", 'coldkey_example'),     ("netuid", 56),     ("status", openapi_server.LiquidityPositionStatus()),     ("page", 56),     ("limit", 56),     ("order", openapi_server.DtaoLiquidityPositionOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/liquidity/position/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_liquidity_position_event(client: TestClient):
    """Test case for get_dtao_liquidity_position_event

    
    """
    params = [("id", 'id_example'),     ("position_id", 'position_id_example'),     ("coldkey", 'coldkey_example'),     ("netuid", 56),     ("position_type", openapi_server.LiquidityPositionType()),     ("page", 56),     ("limit", 56),     ("order", openapi_server.DtaoLiquidityPositionEventOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/liquidity/position_event/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_liquidity_tick_to_price(client: TestClient):
    """Test case for get_dtao_liquidity_tick_to_price

    
    """
    params = [("tick", 56)]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/liquidity/tick_to_price/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

