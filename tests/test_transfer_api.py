# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.network_with_all import NetworkWithAll  # noqa: F401
from openapi_server.models.transfer_order import TransferOrder  # noqa: F401
from openapi_server.models.transfer_response import TransferResponse  # noqa: F401


def test_get_transfer(client: TestClient):
    """Test case for get_transfer

    
    """
    params = [("network", openapi_server.NetworkWithAll()),     ("address", 'address_example'),     ("var_from", 'var_from_example'),     ("to", 'to_example'),     ("transaction_hash", 'transaction_hash_example'),     ("extrinsic_id", 'extrinsic_id_example'),     ("amount_min", 'amount_min_example'),     ("amount_max", 'amount_max_example'),     ("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.TransferOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/transfer/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

