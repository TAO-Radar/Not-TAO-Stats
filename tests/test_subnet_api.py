# coding: utf-8

from fastapi.testclient import TestClient


from datetime import datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.frequency_block_hour_day import FrequencyBlockHourDay  # noqa: F401
from openapi_server.models.subnet_distribution_coldkey_response import SubnetDistributionColdkeyResponse  # noqa: F401
from openapi_server.models.subnet_distribution_ip_response import SubnetDistributionIPResponse  # noqa: F401
from openapi_server.models.subnet_distribution_incentive_response import SubnetDistributionIncentiveResponse  # noqa: F401
from openapi_server.models.subnet_history_order import SubnetHistoryOrder  # noqa: F401
from openapi_server.models.subnet_identity_response import SubnetIdentityResponse  # noqa: F401
from openapi_server.models.subnet_identity_set_order import SubnetIdentitySetOrder  # noqa: F401
from openapi_server.models.subnet_identity_set_response import SubnetIdentitySetResponse  # noqa: F401
from openapi_server.models.subnet_latest_response import SubnetLatestResponse  # noqa: F401
from openapi_server.models.subnet_metadata_response import SubnetMetadataResponse  # noqa: F401
from openapi_server.models.subnet_neuron_deregistration_order import SubnetNeuronDeregistrationOrder  # noqa: F401
from openapi_server.models.subnet_neuron_deregistration_response import SubnetNeuronDeregistrationResponse  # noqa: F401
from openapi_server.models.subnet_neuron_registration_order import SubnetNeuronRegistrationOrder  # noqa: F401
from openapi_server.models.subnet_neuron_registration_response import SubnetNeuronRegistrationResponse  # noqa: F401
from openapi_server.models.subnet_order import SubnetOrder  # noqa: F401
from openapi_server.models.subnet_owner_order import SubnetOwnerOrder  # noqa: F401
from openapi_server.models.subnet_owner_response import SubnetOwnerResponse  # noqa: F401
from openapi_server.models.subnet_pruning_history_order import SubnetPruningHistoryOrder  # noqa: F401
from openapi_server.models.subnet_pruning_latest_order import SubnetPruningLatestOrder  # noqa: F401
from openapi_server.models.subnet_pruning_response import SubnetPruningResponse  # noqa: F401
from openapi_server.models.subnet_registration_cost_history_order import SubnetRegistrationCostHistoryOrder  # noqa: F401
from openapi_server.models.subnet_registration_cost_response import SubnetRegistrationCostResponse  # noqa: F401
from openapi_server.models.subnet_registration_order import SubnetRegistrationOrder  # noqa: F401
from openapi_server.models.subnet_registration_response import SubnetRegistrationResponse  # noqa: F401
from openapi_server.models.subnet_response import SubnetResponse  # noqa: F401


def test_get_subnet_distribution_coldkey(client: TestClient):
    """Test case for get_subnet_distribution_coldkey

    
    """
    params = [("netuid", 56)]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/subnet/distribution/coldkey/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_subnet_distribution_incentive(client: TestClient):
    """Test case for get_subnet_distribution_incentive

    
    """
    params = [("netuid", 56)]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/subnet/distribution/incentive/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_subnet_distribution_ip(client: TestClient):
    """Test case for get_subnet_distribution_ip

    
    """
    params = [("netuid", 56)]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/subnet/distribution/ip/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_subnet_history(client: TestClient):
    """Test case for get_subnet_history

    
    """
    params = [("netuid", 56),     ("frequency", openapi_server.FrequencyBlockHourDay()),     ("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.SubnetHistoryOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/subnet/history/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_subnet_identity(client: TestClient):
    """Test case for get_subnet_identity

    
    """
    params = [("netuid", 56),     ("page", 56),     ("limit", 56)]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/subnet/identity/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_subnet_identity_set(client: TestClient):
    """Test case for get_subnet_identity_set

    
    """
    params = [("netuid", 56),     ("owner", 'owner_example'),     ("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.SubnetIdentitySetOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/subnet/identity_set/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_subnet_latest(client: TestClient):
    """Test case for get_subnet_latest

    
    """
    params = [("netuid", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.SubnetOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/subnet/latest/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_subnet_metadata(client: TestClient):
    """Test case for get_subnet_metadata

    
    """
    params = [("netuid", 56),     ("page", 56),     ("limit", 56)]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/subnet/metadata/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_subnet_neuron_deregistration(client: TestClient):
    """Test case for get_subnet_neuron_deregistration

    
    """
    params = [("netuid", 56),     ("uid", 56),     ("hotkey", 'hotkey_example'),     ("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.SubnetNeuronDeregistrationOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/subnet/neuron/deregistration/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_subnet_neuron_registration(client: TestClient):
    """Test case for get_subnet_neuron_registration

    
    """
    params = [("netuid", 56),     ("uid", 56),     ("hotkey", 'hotkey_example'),     ("coldkey", 'coldkey_example'),     ("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.SubnetNeuronRegistrationOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/subnet/neuron/registration/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_subnet_owner(client: TestClient):
    """Test case for get_subnet_owner

    
    """
    params = [("netuid", 56),     ("owner", 'owner_example'),     ("is_coldkey_swap", True),     ("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.SubnetOwnerOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/subnet/owner/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_subnet_pruning_history(client: TestClient):
    """Test case for get_subnet_pruning_history

    
    """
    params = [("netuid", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.SubnetPruningHistoryOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/subnet/pruning/history/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_subnet_pruning_latest(client: TestClient):
    """Test case for get_subnet_pruning_latest

    
    """
    params = [("netuid", 56),     ("is_immune", True),     ("page", 56),     ("limit", 56),     ("order", openapi_server.SubnetPruningLatestOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/subnet/pruning/latest/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_subnet_registration(client: TestClient):
    """Test case for get_subnet_registration

    
    """
    params = [("netuid", 56),     ("owner", 'owner_example'),     ("registered_by", 'registered_by_example'),     ("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", '2013-10-20T19:20:30+01:00'),     ("timestamp_end", '2013-10-20T19:20:30+01:00'),     ("page", 56),     ("limit", 56),     ("order", openapi_server.SubnetRegistrationOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/subnet/registration/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_subnet_registration_cost_history(client: TestClient):
    """Test case for get_subnet_registration_cost_history

    
    """
    params = [("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.SubnetRegistrationCostHistoryOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/subnet/registration_cost/history/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_subnet_registration_cost_latest(client: TestClient):
    """Test case for get_subnet_registration_cost_latest

    
    """

    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/subnet/registration_cost/latest/v1",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

