# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.config_response import ConfigResponse
from openapi_server.models.dtao_burned_alpha_order import DtaoBurnedAlphaOrder
from openapi_server.models.dtao_burned_alpha_response import DtaoBurnedAlphaResponse
from openapi_server.models.dtao_burned_alpha_total_order import DtaoBurnedAlphaTotalOrder
from openapi_server.models.dtao_burned_alpha_total_response import DtaoBurnedAlphaTotalResponse
from openapi_server.models.dtao_coldkey_alpha_shares_history_order import DtaoColdkeyAlphaSharesHistoryOrder
from openapi_server.models.dtao_coldkey_alpha_shares_latest_order import DtaoColdkeyAlphaSharesLatestOrder
from openapi_server.models.dtao_coldkey_alpha_shares_response import DtaoColdkeyAlphaSharesResponse
from openapi_server.models.dtao_delegation_frequency import DtaoDelegationFrequency
from openapi_server.models.dtao_delegation_volume_response import DtaoDelegationVolumeResponse
from openapi_server.models.dtao_hotkey_alpha_shares_history_order import DtaoHotkeyAlphaSharesHistoryOrder
from openapi_server.models.dtao_hotkey_alpha_shares_latest_order import DtaoHotkeyAlphaSharesLatestOrder
from openapi_server.models.dtao_hotkey_alpha_shares_response import DtaoHotkeyAlphaSharesResponse
from openapi_server.models.dtao_hotkey_emission_order import DtaoHotkeyEmissionOrder
from openapi_server.models.dtao_hotkey_emission_response import DtaoHotkeyEmissionResponse
from openapi_server.models.dtao_slippage_direction import DtaoSlippageDirection
from openapi_server.models.dtao_slippage_response import DtaoSlippageResponse
from openapi_server.models.dtao_stake_balance_aggregated_latest_order import DtaoStakeBalanceAggregatedLatestOrder
from openapi_server.models.dtao_stake_balance_aggregated_response import DtaoStakeBalanceAggregatedResponse
from openapi_server.models.dtao_stake_balance_history_order import DtaoStakeBalanceHistoryOrder
from openapi_server.models.dtao_stake_balance_history_response import DtaoStakeBalanceHistoryResponse
from openapi_server.models.dtao_stake_balance_latest_order import DtaoStakeBalanceLatestOrder
from openapi_server.models.dtao_stake_balance_latest_response import DtaoStakeBalanceLatestResponse
from openapi_server.models.dtao_stake_balance_portfolio_response import DtaoStakeBalancePortfolioResponse
from openapi_server.models.dtao_subnet_emission_order import DtaoSubnetEmissionOrder
from openapi_server.models.dtao_subnet_emission_response import DtaoSubnetEmissionResponse
from openapi_server.models.history_response import HistoryResponse
from openapi_server.models.symbol_info_response import SymbolInfoResponse
from openapi_server.models.tao_flow_response import TaoFlowResponse
from openapi_server.security_api import get_token_api_key

class BaseDtaoApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDtaoApi.subclasses = BaseDtaoApi.subclasses + (cls,)
    async def get_dtao_burned_alpha_total(
        self,
        netuid: Optional[int],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[DtaoBurnedAlphaTotalOrder],
    ) -> DtaoBurnedAlphaTotalResponse:
        ...


    async def get_dtao_burned_alpha(
        self,
        netuid: Optional[int],
        hotkey: Optional[StrictStr],
        coldkey: Optional[StrictStr],
        extrinsic_id: Optional[StrictStr],
        burn_type: Annotated[Optional[StrictStr], Field(description="incentive OR call")],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        amount_min: Optional[StrictStr],
        amount_max: Optional[StrictStr],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[DtaoBurnedAlphaOrder],
    ) -> DtaoBurnedAlphaResponse:
        ...


    async def get_dtao_coldkey_alpha_shares_history(
        self,
        coldkey: Optional[StrictStr],
        hotkey: Optional[StrictStr],
        netuid: Optional[int],
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[DtaoColdkeyAlphaSharesHistoryOrder],
    ) -> DtaoColdkeyAlphaSharesResponse:
        ...


    async def get_dtao_coldkey_alpha_shares_latest(
        self,
        alpha_min: Optional[StrictStr],
        alpha_max: Optional[StrictStr],
        coldkey: Optional[StrictStr],
        hotkey: Optional[StrictStr],
        netuid: Optional[int],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[DtaoColdkeyAlphaSharesLatestOrder],
    ) -> DtaoColdkeyAlphaSharesResponse:
        ...


    async def get_dtao_delegation_volume(
        self,
        frequency: Annotated[Optional[DtaoDelegationFrequency], Field(description="Default is 60 minutes")],
        page: Optional[int],
        limit: Optional[int],
    ) -> DtaoDelegationVolumeResponse:
        ...


    async def get_dtao_hotkey_alpha_shares_history(
        self,
        hotkey: Optional[StrictStr],
        netuid: Optional[int],
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[DtaoHotkeyAlphaSharesHistoryOrder],
    ) -> DtaoHotkeyAlphaSharesResponse:
        ...


    async def get_dtao_hotkey_alpha_shares_latest(
        self,
        alpha_min: Optional[StrictStr],
        alpha_max: Optional[StrictStr],
        hotkey: Optional[StrictStr],
        netuid: Optional[int],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[DtaoHotkeyAlphaSharesLatestOrder],
    ) -> DtaoHotkeyAlphaSharesResponse:
        ...


    async def get_dtao_hotkey_emission(
        self,
        hotkey: Optional[StrictStr],
        netuid: Optional[int],
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[DtaoHotkeyEmissionOrder],
    ) -> DtaoHotkeyEmissionResponse:
        ...


    async def get_dtao_slippage(
        self,
        netuid: int,
        input_tokens: StrictStr,
        direction: DtaoSlippageDirection,
    ) -> DtaoSlippageResponse:
        ...


    async def get_dtao_stake_balance_history(
        self,
        coldkey: Annotated[StrictStr, Field(description="SS58 or hex format")],
        hotkey: Annotated[StrictStr, Field(description="SS58 or hex format")],
        netuid: int,
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[DtaoStakeBalanceHistoryOrder],
    ) -> DtaoStakeBalanceHistoryResponse:
        ...


    async def get_dtao_stake_balance_latest(
        self,
        coldkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        netuid: Optional[int],
        balance_min: Optional[StrictStr],
        balance_max: Optional[StrictStr],
        balance_as_tao_min: Optional[StrictStr],
        balance_as_tao_max: Optional[StrictStr],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[DtaoStakeBalanceLatestOrder],
    ) -> DtaoStakeBalanceLatestResponse:
        ...


    async def get_dtao_stake_balance_portfolio(
        self,
        coldkey: Annotated[StrictStr, Field(description="SS58 or hex format")],
        hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        netuid: Optional[int],
        days: Optional[int],
        balance_min: Optional[StrictStr],
        balance_max: Optional[StrictStr],
        balance_as_tao_min: Optional[StrictStr],
        balance_as_tao_max: Optional[StrictStr],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[DtaoStakeBalanceLatestOrder],
    ) -> DtaoStakeBalancePortfolioResponse:
        ...


    async def get_dtao_stake_balance_aggregated_latest(
        self,
        coldkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        total_balance_as_tao_min: Optional[StrictStr],
        total_balance_as_tao_max: Optional[StrictStr],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[DtaoStakeBalanceAggregatedLatestOrder],
    ) -> DtaoStakeBalanceAggregatedResponse:
        ...


    async def get_dtao_subnet_emission(
        self,
        netuid: Optional[int],
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[DtaoSubnetEmissionOrder],
    ) -> DtaoSubnetEmissionResponse:
        ...


    async def get_dtao_tao_flow(
        self,
        netuid: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
    ) -> TaoFlowResponse:
        ...


    async def get_dtao_tradingview_udf_config(
        self,
    ) -> ConfigResponse:
        ...


    async def get_dtao_tradingview_udf_history(
        self,
        symbol: StrictStr,
        resolution: StrictStr,
        to: int,
        var_from: Optional[int],
        countback: Optional[int],
    ) -> HistoryResponse:
        ...


    async def get_dtao_tradingview_udf_symbol_info(
        self,
        netuid: Optional[int],
    ) -> SymbolInfoResponse:
        ...
