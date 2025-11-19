# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date  # noqa: F401
from pydantic import Field, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.accounting_response import AccountingResponse  # noqa: F401
from openapi_server.models.coldkey_report_response import ColdkeyReportResponse  # noqa: F401
from openapi_server.models.network import Network  # noqa: F401
from openapi_server.models.tax_response import TaxResponse  # noqa: F401
from openapi_server.models.tax_token_response import TaxTokenResponse  # noqa: F401


def test_get_accounting_coldkey_report(client: TestClient):
    """Test case for get_accounting_coldkey_report

    
    """
    params = [("date_start", '2013-10-20'),     ("date_end", '2013-10-20'),     ("coldkey", 'coldkey_example')]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/accounting/coldkey_report/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_accounting_coldkey_report_csv(client: TestClient):
    """Test case for get_accounting_coldkey_report_csv

    
    """
    params = [("date_start", '2013-10-20'),     ("date_end", '2013-10-20'),     ("coldkey", 'coldkey_example')]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/accounting/coldkey_report_csv/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_accounting_tax(client: TestClient):
    """Test case for get_accounting_tax

    
    """
    params = [("token", 'token_example'),     ("date_start", '2013-10-20'),     ("date_end", '2013-10-20'),     ("coldkey", 'coldkey_example')]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/accounting/tax/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_accounting_tax_csv(client: TestClient):
    """Test case for get_accounting_tax_csv

    
    """
    params = [("token", 'token_example'),     ("date_start", '2013-10-20'),     ("date_end", '2013-10-20'),     ("coldkey", 'coldkey_example')]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/accounting/tax_csv/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_accounting_tax_token(client: TestClient):
    """Test case for get_accounting_tax_token

    
    """
    params = [("date_start", '2013-10-20'),     ("date_end", '2013-10-20'),     ("coldkey", 'coldkey_example')]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/accounting/tax_token/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_accounting(client: TestClient):
    """Test case for get_accounting

    
    """
    params = [("date_start", '2013-10-20'),     ("date_end", '2013-10-20'),     ("coldkey", 'coldkey_example'),     ("hotkey", 'hotkey_example'),     ("network", openapi_server.Network())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/accounting/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

