# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.dtao_validator_available_response import DtaoValidatorAvailableResponse  # noqa: F401
from openapi_server.models.dtao_validator_dividends_history_order import DtaoValidatorDividendsHistoryOrder  # noqa: F401
from openapi_server.models.dtao_validator_dividends_latest_order import DtaoValidatorDividendsLatestOrder  # noqa: F401
from openapi_server.models.dtao_validator_dividends_response import DtaoValidatorDividendsResponse  # noqa: F401
from openapi_server.models.dtao_validator_history_order import DtaoValidatorHistoryOrder  # noqa: F401
from openapi_server.models.dtao_validator_latest_order import DtaoValidatorLatestOrder  # noqa: F401
from openapi_server.models.dtao_validator_performance_history_order import DtaoValidatorPerformanceHistoryOrder  # noqa: F401
from openapi_server.models.dtao_validator_performance_latest_order import DtaoValidatorPerformanceLatestOrder  # noqa: F401
from openapi_server.models.dtao_validator_performance_response import DtaoValidatorPerformanceResponse  # noqa: F401
from openapi_server.models.dtao_validator_response import DtaoValidatorResponse  # noqa: F401
from openapi_server.models.dtao_validator_yield_latest_order import DtaoValidatorYieldLatestOrder  # noqa: F401
from openapi_server.models.dtao_validator_yield_response import DtaoValidatorYieldResponse  # noqa: F401
from openapi_server.models.validator_history_order import ValidatorHistoryOrder  # noqa: F401
from openapi_server.models.validator_identity_order import ValidatorIdentityOrder  # noqa: F401
from openapi_server.models.validator_identity_response import ValidatorIdentityResponse  # noqa: F401
from openapi_server.models.validator_metrics_history_order import ValidatorMetricsHistoryOrder  # noqa: F401
from openapi_server.models.validator_metrics_order import ValidatorMetricsOrder  # noqa: F401
from openapi_server.models.validator_metrics_response import ValidatorMetricsResponse  # noqa: F401
from openapi_server.models.validator_order import ValidatorOrder  # noqa: F401
from openapi_server.models.validator_performance_order import ValidatorPerformanceOrder  # noqa: F401
from openapi_server.models.validator_performance_response import ValidatorPerformanceResponse  # noqa: F401
from openapi_server.models.validator_response import ValidatorResponse  # noqa: F401
from openapi_server.models.validator_weights_history_order import ValidatorWeightsHistoryOrder  # noqa: F401
from openapi_server.models.validator_weights_order import ValidatorWeightsOrder  # noqa: F401
from openapi_server.models.validator_weights_response import ValidatorWeightsResponse  # noqa: F401
from openapi_server.models.validator_weights_v2_history_order import ValidatorWeightsV2HistoryOrder  # noqa: F401
from openapi_server.models.validator_weights_v2_order import ValidatorWeightsV2Order  # noqa: F401
from openapi_server.models.validator_weights_v2_response import ValidatorWeightsV2Response  # noqa: F401
from openapi_server.models.weight_copier_response import WeightCopierResponse  # noqa: F401


def test_get_dtao_validator_available(client: TestClient):
    """Test case for get_dtao_validator_available

    
    """
    params = [("netuid", 56)]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/validator/available/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_validator_dividends_history(client: TestClient):
    """Test case for get_dtao_validator_dividends_history

    
    """
    params = [("hotkey", 'hotkey_example'),     ("netuid", 56),     ("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("frequency", openapi_server.Frequency()),     ("page", 56),     ("limit", 56),     ("order", openapi_server.DtaoValidatorDividendsHistoryOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/validator/dividends/history/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_validator_dividends_latest(client: TestClient):
    """Test case for get_dtao_validator_dividends_latest

    
    """
    params = [("hotkey", 'hotkey_example'),     ("netuid", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.DtaoValidatorDividendsLatestOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/validator/dividends/latest/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_validator_history(client: TestClient):
    """Test case for get_dtao_validator_history

    
    """
    params = [("hotkey", 'hotkey_example'),     ("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.DtaoValidatorHistoryOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/validator/history/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_validator_latest(client: TestClient):
    """Test case for get_dtao_validator_latest

    
    """
    params = [("hotkey", 'hotkey_example'),     ("page", 56),     ("limit", 56),     ("order", openapi_server.DtaoValidatorLatestOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/validator/latest/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_validator_performance_history(client: TestClient):
    """Test case for get_dtao_validator_performance_history

    
    """
    params = [("hotkey", 'hotkey_example'),     ("netuid", 56),     ("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.DtaoValidatorPerformanceHistoryOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/validator/performance/history/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_validator_performance_latest(client: TestClient):
    """Test case for get_dtao_validator_performance_latest

    
    """
    params = [("hotkey", 'hotkey_example'),     ("netuid", 56),     ("validator_type", 'validator_type_example'),     ("page", 56),     ("limit", 56),     ("order", openapi_server.DtaoValidatorPerformanceLatestOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/validator/performance/latest/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_validator_yield_latest(client: TestClient):
    """Test case for get_dtao_validator_yield_latest

    
    """
    params = [("hotkey", 'hotkey_example'),     ("netuid", 56),     ("min_stake", 'min_stake_example'),     ("page", 56),     ("limit", 56),     ("order", openapi_server.DtaoValidatorYieldLatestOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/validator/yield/latest/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_validator_history(client: TestClient):
    """Test case for get_validator_history

    
    """
    params = [("hotkey", 'hotkey_example'),     ("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.ValidatorHistoryOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/validator/history/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_validator_identity(client: TestClient):
    """Test case for get_validator_identity

    
    """
    params = [("hotkey", 'hotkey_example'),     ("name", 'name_example'),     ("page", 56),     ("limit", 56),     ("order", openapi_server.ValidatorIdentityOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/validator/identity/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_validator_latest(client: TestClient):
    """Test case for get_validator_latest

    
    """
    params = [("hotkey", 'hotkey_example'),     ("stake_min", 'stake_min_example'),     ("stake_max", 'stake_max_example'),     ("apr_min", 'apr_min_example'),     ("apr_max", 'apr_max_example'),     ("page", 56),     ("limit", 56),     ("order", openapi_server.ValidatorOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/validator/latest/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_validator_metrics_history(client: TestClient):
    """Test case for get_validator_metrics_history

    
    """
    params = [("hotkey", 'hotkey_example'),     ("coldkey", 'coldkey_example'),     ("netuid", 56),     ("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.ValidatorMetricsHistoryOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/validator/metrics/history/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_validator_metrics_latest(client: TestClient):
    """Test case for get_validator_metrics_latest

    
    """
    params = [("hotkey", 'hotkey_example'),     ("coldkey", 'coldkey_example'),     ("netuid", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.ValidatorMetricsOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/validator/metrics/latest/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_validator_performance(client: TestClient):
    """Test case for get_validator_performance

    
    """
    params = [("hotkey", 'hotkey_example'),     ("netuid", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.ValidatorPerformanceOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/validator/performance/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_validator_weight_copier(client: TestClient):
    """Test case for get_validator_weight_copier

    
    """
    params = [("page", 56),     ("limit", 56)]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/validator/weight_copier/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_validator_weights_history(client: TestClient):
    """Test case for get_validator_weights_history

    
    """
    params = [("hotkey", 'hotkey_example'),     ("netuid", 56),     ("uid", 56),     ("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.ValidatorWeightsHistoryOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/validator/weights/history/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_validator_weights_history1(client: TestClient):
    """Test case for get_validator_weights_history1

    
    """
    params = [("hotkey", 'hotkey_example'),     ("netuid", 56),     ("uid", 56),     ("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.ValidatorWeightsV2HistoryOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/validator/weights/history/v2",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_validator_weights_latest(client: TestClient):
    """Test case for get_validator_weights_latest

    
    """
    params = [("hotkey", 'hotkey_example'),     ("netuid", 56),     ("uid", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.ValidatorWeightsOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/validator/weights/latest/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_validator_weights_latest1(client: TestClient):
    """Test case for get_validator_weights_latest1

    
    """
    params = [("hotkey", 'hotkey_example'),     ("netuid", 56),     ("uid", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.ValidatorWeightsV2Order())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/validator/weights/latest/v2",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

