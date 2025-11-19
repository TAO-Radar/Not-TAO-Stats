# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import List  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.sidecar_account_balance_info import SidecarAccountBalanceInfo  # noqa: F401
from openapi_server.models.sidecar_block import SidecarBlock  # noqa: F401
from openapi_server.models.sidecar_block_raw import SidecarBlockRaw  # noqa: F401
from openapi_server.models.sidecar_extrinsic_index import SidecarExtrinsicIndex  # noqa: F401
from openapi_server.models.sidecar_pallet_constant import SidecarPalletConstant  # noqa: F401
from openapi_server.models.sidecar_pallet_constants import SidecarPalletConstants  # noqa: F401
from openapi_server.models.sidecar_pallet_event import SidecarPalletEvent  # noqa: F401
from openapi_server.models.sidecar_pallet_events import SidecarPalletEvents  # noqa: F401
from openapi_server.models.sidecar_pallet_storage_item import SidecarPalletStorageItem  # noqa: F401
from openapi_server.models.sidecar_pallets_storage import SidecarPalletsStorage  # noqa: F401
from openapi_server.models.sidecar_transaction_pool import SidecarTransactionPool  # noqa: F401
from openapi_server.models.sidecar_version_info import SidecarVersionInfo  # noqa: F401


def test_get_v1_live_accounts_address_balance_info(client: TestClient):
    """Test case for get_v1_live_accounts_address_balance_info

    
    """

    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/v1/live/accounts/{address}/balance-info".format(address='address_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_v1_live_blocks(client: TestClient):
    """Test case for get_v1_live_blocks

    
    """
    params = [("block_start", 56),     ("block_end", 56)]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/v1/live/blocks",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_v1_live_blocks_head(client: TestClient):
    """Test case for get_v1_live_blocks_head

    
    """

    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/v1/live/blocks/head",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_v1_live_blocks_height(client: TestClient):
    """Test case for get_v1_live_blocks_height

    
    """

    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/v1/live/blocks/{height}".format(height=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_v1_live_blocks_height_extrinsics_raw(client: TestClient):
    """Test case for get_v1_live_blocks_height_extrinsics_raw

    
    """

    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/v1/live/blocks/{height}/extrinsics-raw".format(height=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_v1_live_blocks_height_extrinsics_index(client: TestClient):
    """Test case for get_v1_live_blocks_height_extrinsics_index

    
    """

    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/v1/live/blocks/{height}/extrinsics/{index}".format(height=56, index='index_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_v1_live_node_transaction_pool(client: TestClient):
    """Test case for get_v1_live_node_transaction_pool

    
    """

    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/v1/live/node/transaction-pool",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_v1_live_node_version(client: TestClient):
    """Test case for get_v1_live_node_version

    
    """

    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/v1/live/node/version",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_v1_live_pallets_pallet_id_consts(client: TestClient):
    """Test case for get_v1_live_pallets_pallet_id_consts

    
    """

    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/v1/live/pallets/{pallet_id}/consts".format(pallet_id='pallet_id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_v1_live_pallets_pallet_id_consts_id(client: TestClient):
    """Test case for get_v1_live_pallets_pallet_id_consts_id

    
    """

    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/v1/live/pallets/{pallet_id}/consts/{id}".format(pallet_id='pallet_id_example', id='id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_v1_live_pallets_pallet_id_events(client: TestClient):
    """Test case for get_v1_live_pallets_pallet_id_events

    
    """

    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/v1/live/pallets/{pallet_id}/events".format(pallet_id='pallet_id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_v1_live_pallets_pallet_id_events_id(client: TestClient):
    """Test case for get_v1_live_pallets_pallet_id_events_id

    
    """

    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/v1/live/pallets/{pallet_id}/events/{id}".format(pallet_id='pallet_id_example', id='id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_v1_live_pallets_pallet_id_storage(client: TestClient):
    """Test case for get_v1_live_pallets_pallet_id_storage

    
    """

    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/v1/live/pallets/{pallet_id}/storage".format(pallet_id='pallet_id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_v1_live_pallets_pallet_id_storage_id(client: TestClient):
    """Test case for get_v1_live_pallets_pallet_id_storage_id

    
    """

    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/v1/live/pallets/{pallet_id}/storage/{id}".format(pallet_id='pallet_id_example', id='id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

