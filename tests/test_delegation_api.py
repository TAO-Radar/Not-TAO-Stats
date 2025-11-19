# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictBool, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.delegation_action import DelegationAction  # noqa: F401
from openapi_server.models.delegation_order import DelegationOrder  # noqa: F401
from openapi_server.models.delegation_response import DelegationResponse  # noqa: F401


def test_get_delegation(client: TestClient):
    """Test case for get_delegation

    
    """
    params = [("nominator", 'nominator_example'),     ("delegate", 'delegate_example'),     ("action", openapi_server.DelegationAction()),     ("is_transfer", True),     ("transfer_address", 'transfer_address_example'),     ("extrinsic_id", 'extrinsic_id_example'),     ("amount_min", 'amount_min_example'),     ("amount_max", 'amount_max_example'),     ("netuid", 56),     ("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.DelegationOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/delegation/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

