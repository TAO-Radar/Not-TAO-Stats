# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.proxy_call_order import ProxyCallOrder  # noqa: F401
from openapi_server.models.proxy_call_response import ProxyCallResponse  # noqa: F401


def test_get_proxy_call(client: TestClient):
    """Test case for get_proxy_call

    
    """
    params = [("id", 'id_example'),     ("signer_address", 'signer_address_example'),     ("real_address", 'real_address_example'),     ("network", 'network_example'),     ("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("extrinsic_hash", 'extrinsic_hash_example'),     ("extrinsic_id", 'extrinsic_id_example'),     ("page", 56),     ("limit", 56),     ("order", openapi_server.ProxyCallOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/proxy_call/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

