# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing import List
from typing_extensions import Annotated
from openapi_server.models.sidecar_account_balance_info import SidecarAccountBalanceInfo
from openapi_server.models.sidecar_block import SidecarBlock
from openapi_server.models.sidecar_block_raw import SidecarBlockRaw
from openapi_server.models.sidecar_extrinsic_index import SidecarExtrinsicIndex
from openapi_server.models.sidecar_pallet_constant import SidecarPalletConstant
from openapi_server.models.sidecar_pallet_constants import SidecarPalletConstants
from openapi_server.models.sidecar_pallet_event import SidecarPalletEvent
from openapi_server.models.sidecar_pallet_events import SidecarPalletEvents
from openapi_server.models.sidecar_pallet_storage_item import SidecarPalletStorageItem
from openapi_server.models.sidecar_pallets_storage import SidecarPalletsStorage
from openapi_server.models.sidecar_transaction_pool import SidecarTransactionPool
from openapi_server.models.sidecar_version_info import SidecarVersionInfo
from openapi_server.security_api import get_token_api_key

class BaseLiveApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseLiveApi.subclasses = BaseLiveApi.subclasses + (cls,)
    async def get_v1_live_accounts_address_balance_info(
        self,
        address: StrictStr,
    ) -> SidecarAccountBalanceInfo:
        ...


    async def get_v1_live_blocks(
        self,
        block_start: Annotated[int, Field(strict=True, ge=0)],
        block_end: Annotated[int, Field(strict=True, ge=0)],
    ) -> List[SidecarBlock]:
        ...


    async def get_v1_live_blocks_head(
        self,
    ) -> SidecarBlock:
        ...


    async def get_v1_live_blocks_height(
        self,
        height: Annotated[int, Field(strict=True, ge=0)],
    ) -> SidecarBlock:
        ...


    async def get_v1_live_blocks_height_extrinsics_raw(
        self,
        height: Annotated[int, Field(strict=True, ge=0)],
    ) -> SidecarBlockRaw:
        ...


    async def get_v1_live_blocks_height_extrinsics_index(
        self,
        height: Annotated[int, Field(strict=True, ge=0)],
        index: StrictStr,
    ) -> SidecarExtrinsicIndex:
        ...


    async def get_v1_live_node_transaction_pool(
        self,
    ) -> SidecarTransactionPool:
        ...


    async def get_v1_live_node_version(
        self,
    ) -> SidecarVersionInfo:
        ...


    async def get_v1_live_pallets_pallet_id_consts(
        self,
        pallet_id: StrictStr,
    ) -> SidecarPalletConstants:
        ...


    async def get_v1_live_pallets_pallet_id_consts_id(
        self,
        pallet_id: StrictStr,
        id: StrictStr,
    ) -> SidecarPalletConstant:
        ...


    async def get_v1_live_pallets_pallet_id_events(
        self,
        pallet_id: StrictStr,
    ) -> SidecarPalletEvents:
        ...


    async def get_v1_live_pallets_pallet_id_events_id(
        self,
        pallet_id: StrictStr,
        id: StrictStr,
    ) -> SidecarPalletEvent:
        ...


    async def get_v1_live_pallets_pallet_id_storage(
        self,
        pallet_id: StrictStr,
    ) -> SidecarPalletsStorage:
        ...


    async def get_v1_live_pallets_pallet_id_storage_id(
        self,
        pallet_id: StrictStr,
        id: StrictStr,
    ) -> SidecarPalletStorageItem:
        ...
