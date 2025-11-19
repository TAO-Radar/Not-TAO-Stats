# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.config_response import ConfigResponse  # noqa: F401
from openapi_server.models.dtao_burned_alpha_order import DtaoBurnedAlphaOrder  # noqa: F401
from openapi_server.models.dtao_burned_alpha_response import DtaoBurnedAlphaResponse  # noqa: F401
from openapi_server.models.dtao_burned_alpha_total_order import DtaoBurnedAlphaTotalOrder  # noqa: F401
from openapi_server.models.dtao_burned_alpha_total_response import DtaoBurnedAlphaTotalResponse  # noqa: F401
from openapi_server.models.dtao_coldkey_alpha_shares_history_order import DtaoColdkeyAlphaSharesHistoryOrder  # noqa: F401
from openapi_server.models.dtao_coldkey_alpha_shares_latest_order import DtaoColdkeyAlphaSharesLatestOrder  # noqa: F401
from openapi_server.models.dtao_coldkey_alpha_shares_response import DtaoColdkeyAlphaSharesResponse  # noqa: F401
from openapi_server.models.dtao_delegation_frequency import DtaoDelegationFrequency  # noqa: F401
from openapi_server.models.dtao_delegation_volume_response import DtaoDelegationVolumeResponse  # noqa: F401
from openapi_server.models.dtao_hotkey_alpha_shares_history_order import DtaoHotkeyAlphaSharesHistoryOrder  # noqa: F401
from openapi_server.models.dtao_hotkey_alpha_shares_latest_order import DtaoHotkeyAlphaSharesLatestOrder  # noqa: F401
from openapi_server.models.dtao_hotkey_alpha_shares_response import DtaoHotkeyAlphaSharesResponse  # noqa: F401
from openapi_server.models.dtao_hotkey_emission_order import DtaoHotkeyEmissionOrder  # noqa: F401
from openapi_server.models.dtao_hotkey_emission_response import DtaoHotkeyEmissionResponse  # noqa: F401
from openapi_server.models.dtao_slippage_direction import DtaoSlippageDirection  # noqa: F401
from openapi_server.models.dtao_slippage_response import DtaoSlippageResponse  # noqa: F401
from openapi_server.models.dtao_stake_balance_aggregated_latest_order import DtaoStakeBalanceAggregatedLatestOrder  # noqa: F401
from openapi_server.models.dtao_stake_balance_aggregated_response import DtaoStakeBalanceAggregatedResponse  # noqa: F401
from openapi_server.models.dtao_stake_balance_history_order import DtaoStakeBalanceHistoryOrder  # noqa: F401
from openapi_server.models.dtao_stake_balance_history_response import DtaoStakeBalanceHistoryResponse  # noqa: F401
from openapi_server.models.dtao_stake_balance_latest_order import DtaoStakeBalanceLatestOrder  # noqa: F401
from openapi_server.models.dtao_stake_balance_latest_response import DtaoStakeBalanceLatestResponse  # noqa: F401
from openapi_server.models.dtao_stake_balance_portfolio_response import DtaoStakeBalancePortfolioResponse  # noqa: F401
from openapi_server.models.dtao_subnet_emission_order import DtaoSubnetEmissionOrder  # noqa: F401
from openapi_server.models.dtao_subnet_emission_response import DtaoSubnetEmissionResponse  # noqa: F401
from openapi_server.models.history_response import HistoryResponse  # noqa: F401
from openapi_server.models.symbol_info_response import SymbolInfoResponse  # noqa: F401
from openapi_server.models.tao_flow_response import TaoFlowResponse  # noqa: F401


def test_get_dtao_burned_alpha_total(client: TestClient):
    """Test case for get_dtao_burned_alpha_total

    
    """
    params = [("netuid", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.DtaoBurnedAlphaTotalOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/burned_alpha/total/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_burned_alpha(client: TestClient):
    """Test case for get_dtao_burned_alpha

    
    """
    params = [("netuid", 56),     ("hotkey", 'hotkey_example'),     ("coldkey", 'coldkey_example'),     ("extrinsic_id", 'extrinsic_id_example'),     ("burn_type", 'burn_type_example'),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("amount_min", 'amount_min_example'),     ("amount_max", 'amount_max_example'),     ("page", 56),     ("limit", 56),     ("order", openapi_server.DtaoBurnedAlphaOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/burned_alpha/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_coldkey_alpha_shares_history(client: TestClient):
    """Test case for get_dtao_coldkey_alpha_shares_history

    
    """
    params = [("coldkey", 'coldkey_example'),     ("hotkey", 'hotkey_example'),     ("netuid", 56),     ("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.DtaoColdkeyAlphaSharesHistoryOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/coldkey_alpha_shares/history/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_coldkey_alpha_shares_latest(client: TestClient):
    """Test case for get_dtao_coldkey_alpha_shares_latest

    
    """
    params = [("alpha_min", 'alpha_min_example'),     ("alpha_max", 'alpha_max_example'),     ("coldkey", 'coldkey_example'),     ("hotkey", 'hotkey_example'),     ("netuid", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.DtaoColdkeyAlphaSharesLatestOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/coldkey_alpha_shares/latest/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_delegation_volume(client: TestClient):
    """Test case for get_dtao_delegation_volume

    
    """
    params = [("frequency", openapi_server.DtaoDelegationFrequency()),     ("page", 56),     ("limit", 56)]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/delegation_volume/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_hotkey_alpha_shares_history(client: TestClient):
    """Test case for get_dtao_hotkey_alpha_shares_history

    
    """
    params = [("hotkey", 'hotkey_example'),     ("netuid", 56),     ("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.DtaoHotkeyAlphaSharesHistoryOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/hotkey_alpha_shares/history/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_hotkey_alpha_shares_latest(client: TestClient):
    """Test case for get_dtao_hotkey_alpha_shares_latest

    
    """
    params = [("alpha_min", 'alpha_min_example'),     ("alpha_max", 'alpha_max_example'),     ("hotkey", 'hotkey_example'),     ("netuid", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.DtaoHotkeyAlphaSharesLatestOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/hotkey_alpha_shares/latest/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_hotkey_emission(client: TestClient):
    """Test case for get_dtao_hotkey_emission

    
    """
    params = [("hotkey", 'hotkey_example'),     ("netuid", 56),     ("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.DtaoHotkeyEmissionOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/hotkey_emission/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_slippage(client: TestClient):
    """Test case for get_dtao_slippage

    
    """
    params = [("netuid", 56),     ("input_tokens", 'input_tokens_example'),     ("direction", openapi_server.DtaoSlippageDirection())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/slippage/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_stake_balance_history(client: TestClient):
    """Test case for get_dtao_stake_balance_history

    
    """
    params = [("coldkey", 'coldkey_example'),     ("hotkey", 'hotkey_example'),     ("netuid", 56),     ("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.DtaoStakeBalanceHistoryOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/stake_balance/history/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_stake_balance_latest(client: TestClient):
    """Test case for get_dtao_stake_balance_latest

    
    """
    params = [("coldkey", 'coldkey_example'),     ("hotkey", 'hotkey_example'),     ("netuid", 56),     ("balance_min", 'balance_min_example'),     ("balance_max", 'balance_max_example'),     ("balance_as_tao_min", 'balance_as_tao_min_example'),     ("balance_as_tao_max", 'balance_as_tao_max_example'),     ("page", 56),     ("limit", 56),     ("order", openapi_server.DtaoStakeBalanceLatestOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/stake_balance/latest/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_stake_balance_portfolio(client: TestClient):
    """Test case for get_dtao_stake_balance_portfolio

    
    """
    params = [("coldkey", 'coldkey_example'),     ("hotkey", 'hotkey_example'),     ("netuid", 56),     ("days", 56),     ("balance_min", 'balance_min_example'),     ("balance_max", 'balance_max_example'),     ("balance_as_tao_min", 'balance_as_tao_min_example'),     ("balance_as_tao_max", 'balance_as_tao_max_example'),     ("page", 56),     ("limit", 56),     ("order", openapi_server.DtaoStakeBalanceLatestOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/stake_balance/portfolio/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_stake_balance_aggregated_latest(client: TestClient):
    """Test case for get_dtao_stake_balance_aggregated_latest

    
    """
    params = [("coldkey", 'coldkey_example'),     ("total_balance_as_tao_min", 'total_balance_as_tao_min_example'),     ("total_balance_as_tao_max", 'total_balance_as_tao_max_example'),     ("page", 56),     ("limit", 56),     ("order", openapi_server.DtaoStakeBalanceAggregatedLatestOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/stake_balance_aggregated/latest/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_subnet_emission(client: TestClient):
    """Test case for get_dtao_subnet_emission

    
    """
    params = [("netuid", 56),     ("block_number", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56),     ("page", 56),     ("limit", 56),     ("order", openapi_server.DtaoSubnetEmissionOrder())]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/subnet_emission/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_tao_flow(client: TestClient):
    """Test case for get_dtao_tao_flow

    
    """
    params = [("netuid", 56),     ("block_start", 56),     ("block_end", 56),     ("timestamp_start", 56),     ("timestamp_end", 56)]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/tao_flow/v1",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_tradingview_udf_config(client: TestClient):
    """Test case for get_dtao_tradingview_udf_config

    
    """

    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/tradingview/udf/config",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_tradingview_udf_history(client: TestClient):
    """Test case for get_dtao_tradingview_udf_history

    
    """
    params = [("symbol", 'symbol_example'),     ("resolution", 'resolution_example'),     ("var_from", 56),     ("to", 56),     ("countback", 56)]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/tradingview/udf/history",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_dtao_tradingview_udf_symbol_info(client: TestClient):
    """Test case for get_dtao_tradingview_udf_symbol_info

    
    """
    params = [("netuid", 56)]
    headers = {
        "api_key": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/api/dtao/tradingview/udf/symbol_info",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

