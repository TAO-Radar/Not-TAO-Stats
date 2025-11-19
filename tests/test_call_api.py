# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictBool, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.call_order import CallOrder  # noqa: F401
from openapi_server.models.call_response import CallResponse  # noqa: F401
from openapi_server.models.network import Network  # noqa: F401


def test_get_call(client: TestClient):
    """Test case for get_call

    
    """
    params = [("origin_address", 'origin_address_example'),     ("network", openapi_server.Network()),     ("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("success", True),     ("full_name", 'full_name_example'),     ("id", 'id_example'),     ("extrinsic_id", 'extrinsic_id_example'),     ("parent_id", 'parent_id_example'),     ("page", 56),     ("limit", 56),     ("order", openapi_server.CallOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/call/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

