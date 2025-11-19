# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.dtao_trade_order import DtaoTradeOrder  # noqa: F401
from openapi_server.models.dtao_trade_response import DtaoTradeResponse  # noqa: F401


def test_get_dtao_trade(client: TestClient):
    """Test case for get_dtao_trade

    
    """
    params = [("coldkey", 'coldkey_example'),     ("extrinsic_id", 'extrinsic_id_example'),     ("from_name", 'from_name_example'),     ("to_name", 'to_name_example'),     ("tao_value_min", 'tao_value_min_example'),     ("tao_value_max", 'tao_value_max_example'),     ("usd_value_min", 'usd_value_min_example'),     ("usd_value_max", 'usd_value_max_example'),     ("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.DtaoTradeOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/trade/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

