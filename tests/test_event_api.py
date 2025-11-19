# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.event_order import EventOrder  # noqa: F401
from openapi_server.models.event_response import EventResponse  # noqa: F401
from openapi_server.models.network import Network  # noqa: F401


def test_get_event(client: TestClient):
    """Test case for get_event

    
    """
    params = [("network", openapi_server.Network()),     ("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("pallet", 'pallet_example'),     ("name", 'name_example'),     ("full_name", 'full_name_example'),     ("extrinsic_id", 'extrinsic_id_example'),     ("call_id", 'call_id_example'),     ("id", 'id_example'),     ("phase", 'phase_example'),     ("page", 56),     ("limit", 56),     ("order", openapi_server.EventOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/event/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

