# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.evmerc20_account_order import EVMERC20AccountOrder  # noqa: F401
from openapi_server.models.evmerc20_account_response import EVMERC20AccountResponse  # noqa: F401
from openapi_server.models.evmerc20_token_order import EVMERC20TokenOrder  # noqa: F401
from openapi_server.models.evmerc20_token_response import EVMERC20TokenResponse  # noqa: F401
from openapi_server.models.evmerc20_transfer_order import EVMERC20TransferOrder  # noqa: F401
from openapi_server.models.evmerc20_transfer_response import EVMERC20TransferResponse  # noqa: F401


def test_get_evm_erc20_account(client: TestClient):
    """Test case for get_evm_erc20_account

    
    """
    params = [("address", 'address_example'),     ("token_name", 'token_name_example'),     ("token_symbol", 'token_symbol_example'),     ("token_address", 'token_address_example'),     ("balance_min", 'balance_min_example'),     ("balance_max", 'balance_max_example'),     ("page", 56),     ("limit", 56),     ("order", openapi_server.EVMERC20AccountOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/evm/erc20/account/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_evm_erc20_token(client: TestClient):
    """Test case for get_evm_erc20_token

    
    """
    params = [("address", 'address_example'),     ("name", 'name_example'),     ("symbol", 'symbol_example'),     ("page", 56),     ("limit", 56),     ("order", openapi_server.EVMERC20TokenOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/evm/erc20/token/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_evm_erc20_transfer(client: TestClient):
    """Test case for get_evm_erc20_transfer

    
    """
    params = [("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("address", 'address_example'),     ("to", 'to_example'),     ("var_from", 'var_from_example'),     ("transaction_hash", 'transaction_hash_example'),     ("token_name", 'token_name_example'),     ("token_symbol", 'token_symbol_example'),     ("token_address", 'token_address_example'),     ("amount_min", 'amount_min_example'),     ("amount_max", 'amount_max_example'),     ("page", 56),     ("limit", 56),     ("order", openapi_server.EVMERC20TransferOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/evm/erc20/transfer/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

