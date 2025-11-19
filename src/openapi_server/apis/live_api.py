# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.live_api_base import BaseLiveApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
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

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/v1/live/accounts/{address}/balance-info",
    responses={
        200: {"model": SidecarAccountBalanceInfo, "description": ""},
    },
    tags=["live"],
    response_model_by_alias=True,
)
async def get_v1_live_accounts_address_balance_info(
    address: StrictStr = Path(..., description=""),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> SidecarAccountBalanceInfo:
    if not BaseLiveApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLiveApi.subclasses[0]().get_v1_live_accounts_address_balance_info(address)


@router.get(
    "/api/v1/live/blocks",
    responses={
        200: {"model": List[SidecarBlock], "description": ""},
    },
    tags=["live"],
    response_model_by_alias=True,
)
async def get_v1_live_blocks(
    block_start: Annotated[int, Field(strict=True, ge=0)] = Query(None, description="", alias="block_start", ge=0),
    block_end: Annotated[int, Field(strict=True, ge=0)] = Query(None, description="", alias="block_end", ge=0),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> List[SidecarBlock]:
    if not BaseLiveApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLiveApi.subclasses[0]().get_v1_live_blocks(block_start, block_end)


@router.get(
    "/api/v1/live/blocks/head",
    responses={
        200: {"model": SidecarBlock, "description": ""},
    },
    tags=["live"],
    response_model_by_alias=True,
)
async def get_v1_live_blocks_head(
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> SidecarBlock:
    if not BaseLiveApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLiveApi.subclasses[0]().get_v1_live_blocks_head()


@router.get(
    "/api/v1/live/blocks/{height}",
    responses={
        200: {"model": SidecarBlock, "description": ""},
    },
    tags=["live"],
    response_model_by_alias=True,
)
async def get_v1_live_blocks_height(
    height: Annotated[int, Field(strict=True, ge=0)] = Path(..., description="", ge=0),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> SidecarBlock:
    if not BaseLiveApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLiveApi.subclasses[0]().get_v1_live_blocks_height(height)


@router.get(
    "/api/v1/live/blocks/{height}/extrinsics-raw",
    responses={
        200: {"model": SidecarBlockRaw, "description": ""},
    },
    tags=["live"],
    response_model_by_alias=True,
)
async def get_v1_live_blocks_height_extrinsics_raw(
    height: Annotated[int, Field(strict=True, ge=0)] = Path(..., description="", ge=0),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> SidecarBlockRaw:
    if not BaseLiveApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLiveApi.subclasses[0]().get_v1_live_blocks_height_extrinsics_raw(height)


@router.get(
    "/api/v1/live/blocks/{height}/extrinsics/{index}",
    responses={
        200: {"model": SidecarExtrinsicIndex, "description": ""},
    },
    tags=["live"],
    response_model_by_alias=True,
)
async def get_v1_live_blocks_height_extrinsics_index(
    height: Annotated[int, Field(strict=True, ge=0)] = Path(..., description="", ge=0),
    index: StrictStr = Path(..., description=""),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> SidecarExtrinsicIndex:
    if not BaseLiveApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLiveApi.subclasses[0]().get_v1_live_blocks_height_extrinsics_index(height, index)


@router.get(
    "/api/v1/live/node/transaction-pool",
    responses={
        200: {"model": SidecarTransactionPool, "description": ""},
    },
    tags=["live"],
    response_model_by_alias=True,
)
async def get_v1_live_node_transaction_pool(
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> SidecarTransactionPool:
    if not BaseLiveApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLiveApi.subclasses[0]().get_v1_live_node_transaction_pool()


@router.get(
    "/api/v1/live/node/version",
    responses={
        200: {"model": SidecarVersionInfo, "description": ""},
    },
    tags=["live"],
    response_model_by_alias=True,
)
async def get_v1_live_node_version(
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> SidecarVersionInfo:
    if not BaseLiveApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLiveApi.subclasses[0]().get_v1_live_node_version()


@router.get(
    "/api/v1/live/pallets/{pallet_id}/consts",
    responses={
        200: {"model": SidecarPalletConstants, "description": ""},
    },
    tags=["live"],
    response_model_by_alias=True,
)
async def get_v1_live_pallets_pallet_id_consts(
    pallet_id: StrictStr = Path(..., description=""),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> SidecarPalletConstants:
    if not BaseLiveApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLiveApi.subclasses[0]().get_v1_live_pallets_pallet_id_consts(pallet_id)


@router.get(
    "/api/v1/live/pallets/{pallet_id}/consts/{id}",
    responses={
        200: {"model": SidecarPalletConstant, "description": ""},
    },
    tags=["live"],
    response_model_by_alias=True,
)
async def get_v1_live_pallets_pallet_id_consts_id(
    pallet_id: StrictStr = Path(..., description=""),
    id: StrictStr = Path(..., description=""),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> SidecarPalletConstant:
    if not BaseLiveApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLiveApi.subclasses[0]().get_v1_live_pallets_pallet_id_consts_id(pallet_id, id)


@router.get(
    "/api/v1/live/pallets/{pallet_id}/events",
    responses={
        200: {"model": SidecarPalletEvents, "description": ""},
    },
    tags=["live"],
    response_model_by_alias=True,
)
async def get_v1_live_pallets_pallet_id_events(
    pallet_id: StrictStr = Path(..., description=""),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> SidecarPalletEvents:
    if not BaseLiveApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLiveApi.subclasses[0]().get_v1_live_pallets_pallet_id_events(pallet_id)


@router.get(
    "/api/v1/live/pallets/{pallet_id}/events/{id}",
    responses={
        200: {"model": SidecarPalletEvent, "description": ""},
    },
    tags=["live"],
    response_model_by_alias=True,
)
async def get_v1_live_pallets_pallet_id_events_id(
    pallet_id: StrictStr = Path(..., description=""),
    id: StrictStr = Path(..., description=""),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> SidecarPalletEvent:
    if not BaseLiveApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLiveApi.subclasses[0]().get_v1_live_pallets_pallet_id_events_id(pallet_id, id)


@router.get(
    "/api/v1/live/pallets/{pallet_id}/storage",
    responses={
        200: {"model": SidecarPalletsStorage, "description": ""},
    },
    tags=["live"],
    response_model_by_alias=True,
)
async def get_v1_live_pallets_pallet_id_storage(
    pallet_id: StrictStr = Path(..., description=""),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> SidecarPalletsStorage:
    if not BaseLiveApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLiveApi.subclasses[0]().get_v1_live_pallets_pallet_id_storage(pallet_id)


@router.get(
    "/api/v1/live/pallets/{pallet_id}/storage/{id}",
    responses={
        200: {"model": SidecarPalletStorageItem, "description": ""},
    },
    tags=["live"],
    response_model_by_alias=True,
)
async def get_v1_live_pallets_pallet_id_storage_id(
    pallet_id: StrictStr = Path(..., description=""),
    id: StrictStr = Path(..., description=""),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> SidecarPalletStorageItem:
    if not BaseLiveApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseLiveApi.subclasses[0]().get_v1_live_pallets_pallet_id_storage_id(pallet_id, id)
