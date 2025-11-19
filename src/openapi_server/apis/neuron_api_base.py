# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictBool, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.neuron_aggregated_history_order import NeuronAggregatedHistoryOrder
from openapi_server.models.neuron_aggregated_latest_order import NeuronAggregatedLatestOrder
from openapi_server.models.neuron_aggregated_response import NeuronAggregatedResponse
from openapi_server.models.neuron_history_order import NeuronHistoryOrder
from openapi_server.models.neuron_incentive_distribution_response import NeuronIncentiveDistributionResponse
from openapi_server.models.neuron_latest_order import NeuronLatestOrder
from openapi_server.models.neuron_response import NeuronResponse
from openapi_server.security_api import get_token_api_key

class BaseNeuronApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseNeuronApi.subclasses = BaseNeuronApi.subclasses + (cls,)
    async def get_neuron_aggregated_history(
        self,
        netuid: Annotated[Optional[int], Field(description="Subnet ID")],
        block_start: Optional[int],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[NeuronAggregatedHistoryOrder],
    ) -> NeuronAggregatedResponse:
        ...


    async def get_neuron_aggregated_latest(
        self,
        netuid: Annotated[Optional[int], Field(description="Subnet ID")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[NeuronAggregatedLatestOrder],
    ) -> NeuronAggregatedResponse:
        ...


    async def get_neuron_history(
        self,
        netuid: Annotated[Optional[int], Field(description="Subnet ID")],
        uid: Annotated[Optional[int], Field(description="Neuron ID")],
        hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        coldkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        is_immune: Annotated[Optional[StrictBool], Field(description="Start of block range (inclusive) Is immune")],
        in_danger: Annotated[Optional[StrictBool], Field(description="Is in danger")],
        has_dividends: Annotated[Optional[StrictBool], Field(description="Has dividends")],
        has_incentive: Annotated[Optional[StrictBool], Field(description="Has incentive")],
        block_start: Optional[int],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[NeuronHistoryOrder],
    ) -> NeuronResponse:
        ...


    async def get_neuron_incentive_distribution(
        self,
        netuid: Annotated[int, Field(description="Subnet ID")],
        days: Annotated[int, Field(description="Integer between 1 and 7")],
    ) -> NeuronIncentiveDistributionResponse:
        ...


    async def get_neuron_latest(
        self,
        netuid: Annotated[Optional[int], Field(description="Subnet ID")],
        uid: Annotated[Optional[int], Field(description="Neuron ID")],
        hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        coldkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        is_immune: Annotated[Optional[StrictBool], Field(description="Start of block range (inclusive) Is immune")],
        in_danger: Annotated[Optional[StrictBool], Field(description="Is in danger")],
        has_dividends: Annotated[Optional[StrictBool], Field(description="Has dividends")],
        has_incentive: Annotated[Optional[StrictBool], Field(description="Has incentive")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[NeuronLatestOrder],
    ) -> NeuronResponse:
        ...
