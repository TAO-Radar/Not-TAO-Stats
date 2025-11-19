# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictBool, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.extrinsic_order import ExtrinsicOrder  # noqa: F401
from openapi_server.models.extrinsic_response import ExtrinsicResponse  # noqa: F401
from openapi_server.models.network_with_testnet import NetworkWithTestnet  # noqa: F401


def test_get_extrinsic(client: TestClient):
    """Test case for get_extrinsic

    
    """
    params = [("network", openapi_server.NetworkWithTestnet()),     ("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("hash", 'hash_example'),     ("full_name", 'full_name_example'),     ("id", 'id_example'),     ("success", True),     ("signer_address", 'signer_address_example'),     ("page", 56),     ("limit", 56),     ("order", openapi_server.ExtrinsicOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/extrinsic/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

