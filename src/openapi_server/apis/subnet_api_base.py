# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import datetime
from pydantic import Field, StrictBool, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.frequency_block_hour_day import FrequencyBlockHourDay
from openapi_server.models.subnet_distribution_coldkey_response import SubnetDistributionColdkeyResponse
from openapi_server.models.subnet_distribution_ip_response import SubnetDistributionIPResponse
from openapi_server.models.subnet_distribution_incentive_response import SubnetDistributionIncentiveResponse
from openapi_server.models.subnet_history_order import SubnetHistoryOrder
from openapi_server.models.subnet_identity_response import SubnetIdentityResponse
from openapi_server.models.subnet_identity_set_order import SubnetIdentitySetOrder
from openapi_server.models.subnet_identity_set_response import SubnetIdentitySetResponse
from openapi_server.models.subnet_latest_response import SubnetLatestResponse
from openapi_server.models.subnet_metadata_response import SubnetMetadataResponse
from openapi_server.models.subnet_neuron_deregistration_order import SubnetNeuronDeregistrationOrder
from openapi_server.models.subnet_neuron_deregistration_response import SubnetNeuronDeregistrationResponse
from openapi_server.models.subnet_neuron_registration_order import SubnetNeuronRegistrationOrder
from openapi_server.models.subnet_neuron_registration_response import SubnetNeuronRegistrationResponse
from openapi_server.models.subnet_order import SubnetOrder
from openapi_server.models.subnet_owner_order import SubnetOwnerOrder
from openapi_server.models.subnet_owner_response import SubnetOwnerResponse
from openapi_server.models.subnet_pruning_history_order import SubnetPruningHistoryOrder
from openapi_server.models.subnet_pruning_latest_order import SubnetPruningLatestOrder
from openapi_server.models.subnet_pruning_response import SubnetPruningResponse
from openapi_server.models.subnet_registration_cost_history_order import SubnetRegistrationCostHistoryOrder
from openapi_server.models.subnet_registration_cost_response import SubnetRegistrationCostResponse
from openapi_server.models.subnet_registration_order import SubnetRegistrationOrder
from openapi_server.models.subnet_registration_response import SubnetRegistrationResponse
from openapi_server.models.subnet_response import SubnetResponse
from openapi_server.security_api import get_token_api_key

class BaseSubnetApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseSubnetApi.subclasses = BaseSubnetApi.subclasses + (cls,)
    async def get_subnet_distribution_coldkey(
        self,
        netuid: int,
    ) -> SubnetDistributionColdkeyResponse:
        ...


    async def get_subnet_distribution_incentive(
        self,
        netuid: int,
    ) -> SubnetDistributionIncentiveResponse:
        ...


    async def get_subnet_distribution_ip(
        self,
        netuid: int,
    ) -> SubnetDistributionIPResponse:
        ...


    async def get_subnet_history(
        self,
        netuid: int,
        frequency: Optional[FrequencyBlockHourDay],
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[SubnetHistoryOrder],
    ) -> SubnetResponse:
        ...


    async def get_subnet_identity(
        self,
        netuid: Optional[int],
        page: Optional[int],
        limit: Optional[int],
    ) -> SubnetIdentityResponse:
        ...


    async def get_subnet_identity_set(
        self,
        netuid: Optional[int],
        owner: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[SubnetIdentitySetOrder],
    ) -> SubnetIdentitySetResponse:
        ...


    async def get_subnet_latest(
        self,
        netuid: Optional[int],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[SubnetOrder],
    ) -> SubnetLatestResponse:
        ...


    async def get_subnet_metadata(
        self,
        netuid: Optional[int],
        page: Optional[int],
        limit: Optional[int],
    ) -> SubnetMetadataResponse:
        ...


    async def get_subnet_neuron_deregistration(
        self,
        netuid: Optional[int],
        uid: Optional[int],
        hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[SubnetNeuronDeregistrationOrder],
    ) -> SubnetNeuronDeregistrationResponse:
        ...


    async def get_subnet_neuron_registration(
        self,
        netuid: Optional[int],
        uid: Optional[int],
        hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        coldkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[SubnetNeuronRegistrationOrder],
    ) -> SubnetNeuronRegistrationResponse:
        ...


    async def get_subnet_owner(
        self,
        netuid: Optional[int],
        owner: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        is_coldkey_swap: Optional[StrictBool],
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[SubnetOwnerOrder],
    ) -> SubnetOwnerResponse:
        ...


    async def get_subnet_pruning_history(
        self,
        netuid: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[SubnetPruningHistoryOrder],
    ) -> SubnetPruningResponse:
        ...


    async def get_subnet_pruning_latest(
        self,
        netuid: Optional[int],
        is_immune: Optional[StrictBool],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[SubnetPruningLatestOrder],
    ) -> SubnetPruningResponse:
        ...


    async def get_subnet_registration(
        self,
        netuid: Optional[int],
        owner: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        registered_by: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[datetime], Field(description="Start of timestamp range (inclusive)")],
        timestamp_end: Annotated[Optional[datetime], Field(description="End of timestamp range (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[SubnetRegistrationOrder],
    ) -> SubnetRegistrationResponse:
        ...


    async def get_subnet_registration_cost_history(
        self,
        block_number: Optional[int],
        block_start: Annotated[Optional[int], Field(description="Start of block range (inclusive)")],
        block_end: Annotated[Optional[int], Field(description="End of block range (inclusive)")],
        timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[SubnetRegistrationCostHistoryOrder],
    ) -> SubnetRegistrationCostResponse:
        ...


    async def get_subnet_registration_cost_latest(
        self,
    ) -> SubnetRegistrationCostResponse:
        ...
