# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.dtao_validator_available_response import DtaoValidatorAvailableResponse
from openapi_server.models.dtao_validator_dividends_history_order import DtaoValidatorDividendsHistoryOrder
from openapi_server.models.dtao_validator_dividends_latest_order import DtaoValidatorDividendsLatestOrder
from openapi_server.models.dtao_validator_dividends_response import DtaoValidatorDividendsResponse
from openapi_server.models.dtao_validator_history_order import DtaoValidatorHistoryOrder
from openapi_server.models.dtao_validator_latest_order import DtaoValidatorLatestOrder
from openapi_server.models.dtao_validator_performance_history_order import DtaoValidatorPerformanceHistoryOrder
from openapi_server.models.dtao_validator_performance_latest_order import DtaoValidatorPerformanceLatestOrder
from openapi_server.models.dtao_validator_performance_response import DtaoValidatorPerformanceResponse
from openapi_server.models.dtao_validator_response import DtaoValidatorResponse
from openapi_server.models.dtao_validator_yield_latest_order import DtaoValidatorYieldLatestOrder
from openapi_server.models.dtao_validator_yield_response import DtaoValidatorYieldResponse
from openapi_server.models.validator_history_order import ValidatorHistoryOrder
from openapi_server.models.validator_identity_order import ValidatorIdentityOrder
from openapi_server.models.validator_identity_response import ValidatorIdentityResponse
from openapi_server.models.validator_metrics_history_order import ValidatorMetricsHistoryOrder
from openapi_server.models.validator_metrics_order import ValidatorMetricsOrder
from openapi_server.models.validator_metrics_response import ValidatorMetricsResponse
from openapi_server.models.validator_order import ValidatorOrder
from openapi_server.models.validator_performance_order import ValidatorPerformanceOrder
from openapi_server.models.validator_performance_response import ValidatorPerformanceResponse
from openapi_server.models.validator_response import ValidatorResponse
from openapi_server.models.validator_weights_history_order import ValidatorWeightsHistoryOrder
from openapi_server.models.validator_weights_order import ValidatorWeightsOrder
from openapi_server.models.validator_weights_response import ValidatorWeightsResponse
from openapi_server.models.validator_weights_v2_history_order import ValidatorWeightsV2HistoryOrder
from openapi_server.models.validator_weights_v2_order import ValidatorWeightsV2Order
from openapi_server.models.validator_weights_v2_response import ValidatorWeightsV2Response
from openapi_server.models.weight_copier_response import WeightCopierResponse
from openapi_server.security_api import get_token_api_key

class BaseValidatorApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseValidatorApi.subclasses = BaseValidatorApi.subclasses + (cls,)
    async def get_dtao_validator_available(
        self,
        netuid: Optional[int],
    ) -> DtaoValidatorAvailableResponse:
        ...


    async def get_dtao_validator_dividends_history(
        self,
        hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        netuid: Optional[int],
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        frequency: Optional[Any],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[DtaoValidatorDividendsHistoryOrder],
    ) -> DtaoValidatorDividendsResponse:
        ...


    async def get_dtao_validator_dividends_latest(
        self,
        hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        netuid: Optional[int],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[DtaoValidatorDividendsLatestOrder],
    ) -> DtaoValidatorDividendsResponse:
        ...


    async def get_dtao_validator_history(
        self,
        hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[DtaoValidatorHistoryOrder],
    ) -> DtaoValidatorResponse:
        ...


    async def get_dtao_validator_latest(
        self,
        hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[DtaoValidatorLatestOrder],
    ) -> DtaoValidatorResponse:
        ...


    async def get_dtao_validator_performance_history(
        self,
        hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        netuid: Optional[int],
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[DtaoValidatorPerformanceHistoryOrder],
    ) -> DtaoValidatorPerformanceResponse:
        ...


    async def get_dtao_validator_performance_latest(
        self,
        hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        netuid: Optional[int],
        validator_type: Annotated[Optional[StrictStr], Field(description="Validator type: \"running_infra\" or \"childkey\".")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[DtaoValidatorPerformanceLatestOrder],
    ) -> DtaoValidatorPerformanceResponse:
        ...


    async def get_dtao_validator_yield_latest(
        self,
        hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        netuid: Optional[int],
        min_stake: Optional[StrictStr],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[DtaoValidatorYieldLatestOrder],
    ) -> DtaoValidatorYieldResponse:
        ...


    async def get_validator_history(
        self,
        hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[ValidatorHistoryOrder],
    ) -> ValidatorResponse:
        ...


    async def get_validator_identity(
        self,
        hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        name: Optional[StrictStr],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[ValidatorIdentityOrder],
    ) -> ValidatorIdentityResponse:
        ...


    async def get_validator_latest(
        self,
        hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        stake_min: Optional[StrictStr],
        stake_max: Optional[StrictStr],
        apr_min: Optional[StrictStr],
        apr_max: Optional[StrictStr],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[ValidatorOrder],
    ) -> ValidatorResponse:
        ...


    async def get_validator_metrics_history(
        self,
        hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        coldkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        netuid: Optional[int],
        block_number: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[ValidatorMetricsHistoryOrder],
    ) -> ValidatorMetricsResponse:
        ...


    async def get_validator_metrics_latest(
        self,
        hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        coldkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        netuid: Optional[int],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[ValidatorMetricsOrder],
    ) -> ValidatorMetricsResponse:
        ...


    async def get_validator_performance(
        self,
        hotkey: Annotated[StrictStr, Field(description="SS58 or hex format")],
        netuid: int,
        page: Optional[int],
        limit: Optional[int],
        order: Optional[ValidatorPerformanceOrder],
    ) -> ValidatorPerformanceResponse:
        ...


    async def get_validator_weight_copier(
        self,
        page: Optional[int],
        limit: Optional[int],
    ) -> WeightCopierResponse:
        ...


    async def get_validator_weights_history(
        self,
        hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        netuid: Optional[int],
        uid: Optional[int],
        block_number: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[ValidatorWeightsHistoryOrder],
    ) -> ValidatorWeightsResponse:
        ...


    async def get_validator_weights_history1(
        self,
        hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        netuid: Optional[int],
        uid: Optional[int],
        block_number: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[ValidatorWeightsV2HistoryOrder],
    ) -> ValidatorWeightsV2Response:
        ...


    async def get_validator_weights_latest(
        self,
        hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        netuid: Optional[int],
        uid: Optional[int],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[ValidatorWeightsOrder],
    ) -> ValidatorWeightsResponse:
        ...


    async def get_validator_weights_latest1(
        self,
        hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        netuid: Optional[int],
        uid: Optional[int],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[ValidatorWeightsV2Order],
    ) -> ValidatorWeightsV2Response:
        ...
