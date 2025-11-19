# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.evm_block_order import EVMBlockOrder  # noqa: F401
from openapi_server.models.evm_block_response import EVMBlockResponse  # noqa: F401
from openapi_server.models.evm_contract_order import EVMContractOrder  # noqa: F401
from openapi_server.models.evm_contract_response import EVMContractResponse  # noqa: F401
from openapi_server.models.evm_log_order import EVMLogOrder  # noqa: F401
from openapi_server.models.evm_log_response import EVMLogResponse  # noqa: F401
from openapi_server.models.evm_transaction_order import EVMTransactionOrder  # noqa: F401
from openapi_server.models.evm_transaction_response import EVMTransactionResponse  # noqa: F401


def test_get_evm_address_from_ss58(client: TestClient):
    """Test case for get_evm_address_from_ss58

    
    """
    params = [("ss58_address", 'ss58_address_example')]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/evm/address_from_ss58/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_evm_block(client: TestClient):
    """Test case for get_evm_block

    
    """
    params = [("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.EVMBlockOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/evm/block/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_evm_contract(client: TestClient):
    """Test case for get_evm_contract

    
    """
    params = [("address", 'address_example'),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.EVMContractOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/evm/contract/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_evm_log(client: TestClient):
    """Test case for get_evm_log

    
    """
    params = [("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("transaction_hash", 'transaction_hash_example'),     ("address", 'address_example'),     ("event_name", 'event_name_example'),     ("topic0", 'topic0_example'),     ("page", 56),     ("limit", 56),     ("order", openapi_server.EVMLogOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/evm/log/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_evm_transaction(client: TestClient):
    """Test case for get_evm_transaction

    
    """
    params = [("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("hash", 'hash_example'),     ("address", 'address_example'),     ("to", 'to_example'),     ("var_from", 'var_from_example'),     ("method_name", 'method_name_example'),     ("method_id", 'method_id_example'),     ("contract_created", 'contract_created_example'),     ("index", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.EVMTransactionOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/evm/transaction/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

