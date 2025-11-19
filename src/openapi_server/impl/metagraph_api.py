# coding: utf-8
"""
Mocked implementation of MetagraphAPI
"""

from datetime import datetime
import pickle
from typing import Optional, List
from bittensor import MetagraphInfo
from pydantic import Field, StrictBool, StrictStr
from typing_extensions import Annotated

from openapi_server.apis.metagraph_api_base import BaseMetagraphApi
from openapi_server.models.metagraph_history_order import MetagraphHistoryOrder
from openapi_server.models.metagraph_history_response import MetagraphHistoryResponse
from openapi_server.models.metagraph_order import MetagraphOrder
from openapi_server.models.metagraph_response import MetagraphResponse
from openapi_server.models.root_metagraph_history_order import RootMetagraphHistoryOrder
from openapi_server.models.root_metagraph_history_response import RootMetagraphHistoryResponse
from openapi_server.models.root_metagraph_order import RootMetagraphOrder
from openapi_server.models.root_metagraph_response import RootMetagraphResponse
from openapi_server.models.metagraph_item import MetagraphItem
from openapi_server.models.root_metagraph_item import RootMetagraphItem
from openapi_server.models.pagination import Pagination
from openapi_server.models.key import Key
from openapi_server.context import get_context


def _ss58_to_hex(ss58_address: str) -> str:
    """Convert SS58 address to hex format."""
    try:
        from scalecodec.utils.ss58 import ss58_decode
        decoded = ss58_decode(ss58_address)
        return f"0x{decoded.hex()}" if isinstance(decoded, bytes) else f"0x{decoded}"
    except Exception:
        # Fallback: return placeholder
        return f"0x{ss58_address.encode().hex()[:64]}" if ss58_address else "0x"


def _convert_metagraph_info_to_items(metagraph_info: MetagraphInfo) -> List[MetagraphItem]:
    """Convert MetagraphInfo to a list of MetagraphItem objects."""
    items = []
    num_uids = metagraph_info.num_uids
    
    for uid in range(num_uids):
        # Get hotkey and coldkey
        hotkey_ss58 = metagraph_info.hotkeys[uid] if uid < len(metagraph_info.hotkeys) else ""
        coldkey_ss58 = metagraph_info.coldkeys[uid] if uid < len(metagraph_info.coldkeys) else ""
        
        # Convert to hex
        hotkey_hex = _ss58_to_hex(hotkey_ss58)
        coldkey_hex = _ss58_to_hex(coldkey_ss58)
        
        # Get axon info
        axon = metagraph_info.axons[uid] if uid < len(metagraph_info.axons) else None
        axon_dict = None
        if axon:
            try:
                # Try accessing as object (AxonInfo)
                axon_dict = {
                    "ip": axon.ip,
                    "port": axon.port,
                    "ip_type": axon.ip_type,
                    "protocol": axon.protocol,
                    "version": axon.version,
                }
            except (AttributeError, TypeError):
                # Fallback: access as dict
                if isinstance(axon, dict):
                    axon_dict = {
                        "ip": axon.get("ip", ""),
                        "port": axon.get("port", 0),
                        "ip_type": axon.get("ip_type", 0),
                        "protocol": axon.get("protocol", 4),
                        "version": axon.get("version", 0),
                    }
                else:
                    axon_dict = {
                        "ip": str(axon),
                        "port": 0,
                        "ip_type": 0,
                        "protocol": 4,
                        "version": 0,
                    }
        
        # Get values from lists (with bounds checking)
        active = metagraph_info.active[uid] if uid < len(metagraph_info.active) else False
        validator_permit = metagraph_info.validator_permit[uid] if uid < len(metagraph_info.validator_permit) else False
        rank = int(metagraph_info.rank[uid]) if uid < len(metagraph_info.rank) else 0
        consensus = str(metagraph_info.consensus[uid]) if uid < len(metagraph_info.consensus) else "0"
        trust = str(metagraph_info.trust[uid]) if uid < len(metagraph_info.trust) else "0"
        validator_trust = str(metagraph_info.trust[uid]) if uid < len(metagraph_info.trust) else "0"  # Using trust as validator_trust
        incentive = str(metagraph_info.incentives[uid]) if uid < len(metagraph_info.incentives) else "0"
        dividends = str(metagraph_info.dividends[uid]) if uid < len(metagraph_info.dividends) else "0"
        emission = metagraph_info.emission[uid].rao if uid < len(metagraph_info.emission) and metagraph_info.emission[uid] else 0
        emission_str = str(emission)
        updated = metagraph_info.last_update[uid] if uid < len(metagraph_info.last_update) else 0
        registered_at_block = metagraph_info.block_at_registration[uid] if uid < len(metagraph_info.block_at_registration) else 0
        
        # Stake values
        alpha_stake = str(metagraph_info.alpha_stake[uid].rao) if uid < len(metagraph_info.alpha_stake) and metagraph_info.alpha_stake[uid] else "0"
        stake = str(metagraph_info.total_stake[uid].rao) if uid < len(metagraph_info.total_stake) and metagraph_info.total_stake[uid] else "0"
        root_stake = str(metagraph_info.tao_stake[uid].rao) if uid < len(metagraph_info.tao_stake) and metagraph_info.tao_stake[uid] else "0"
        root_stake_as_alpha = str(metagraph_info.alpha_stake[uid].rao) if uid < len(metagraph_info.alpha_stake) and metagraph_info.alpha_stake[uid] else "0"  # Approximation
        total_alpha_stake = str(metagraph_info.alpha_stake[uid].rao) if uid < len(metagraph_info.alpha_stake) and metagraph_info.alpha_stake[uid] else "0"
        root_weight = "0"  # Not directly available in MetagraphInfo
        
        # Check immunity period
        is_immunity_period = False
        if registered_at_block > 0 and metagraph_info.block > 0:
            blocks_since_registration = metagraph_info.block - registered_at_block
            is_immunity_period = blocks_since_registration < metagraph_info.immunity_period
        
        # Check if child key (simplified - would need additional logic)
        is_child_key = False
        
        # Check if owner hotkey
        is_owner_hotkey = metagraph_info.owner_hotkey == hotkey_ss58 if metagraph_info.owner_hotkey else False
        
        # Mech incentive and updated (not directly available, using empty lists)
        mech_incentive: List[str] = []
        mech_updated: List[int] = []
        
        # Daily rewards (not available in MetagraphInfo, using defaults)
        epoches_in_24_hours = 20
        daily_reward = str(emission * epoches_in_24_hours)
        daily_mining_tao = None
        daily_mining_alpha = None
        daily_mining_alpha_as_tao = None
        daily_validating_alpha = None
        daily_validating_alpha_as_tao = None
        daily_validating_tao = None
        daily_total_rewards_as_tao = None
        daily_owner_alpha = None
        daily_owner_alpha_as_tao = None
        daily_burned_alpha = None
        daily_burned_alpha_as_tao = None
        
        item = MetagraphItem(
            active=active,
            alpha_stake=alpha_stake,
            axon=axon_dict,
            block_number=metagraph_info.block,
            coldkey=Key(hex=coldkey_hex, ss58=coldkey_ss58),
            consensus=consensus,
            daily_burned_alpha=daily_burned_alpha,
            daily_burned_alpha_as_tao=daily_burned_alpha_as_tao,
            daily_mining_alpha=daily_mining_alpha,
            daily_mining_alpha_as_tao=daily_mining_alpha_as_tao,
            daily_mining_tao=daily_mining_tao,
            daily_owner_alpha=daily_owner_alpha,
            daily_owner_alpha_as_tao=daily_owner_alpha_as_tao,
            daily_reward=daily_reward,
            daily_total_rewards_as_tao=daily_total_rewards_as_tao,
            daily_validating_alpha=daily_validating_alpha,
            daily_validating_alpha_as_tao=daily_validating_alpha_as_tao,
            daily_validating_tao=daily_validating_tao,
            dividends=dividends,
            emission=emission_str,
            hotkey=Key(hex=hotkey_hex, ss58=hotkey_ss58),
            incentive=incentive,
            is_child_key=is_child_key,
            is_immunity_period=is_immunity_period,
            is_owner_hotkey=is_owner_hotkey,
            mech_incentive=mech_incentive,
            mech_updated=mech_updated,
            netuid=metagraph_info.netuid,
            rank=rank,
            registered_at_block=registered_at_block,
            root_stake=root_stake,
            root_stake_as_alpha=root_stake_as_alpha,
            root_weight=root_weight,
            stake=stake,
            timestamp=datetime.now(),  # Using current time as timestamp is not in MetagraphInfo
            total_alpha_stake=total_alpha_stake,
            trust=trust,
            uid=uid,
            updated=updated,
            validator_permit=validator_permit,
            validator_trust=validator_trust,
        )
        items.append(item)
    
    return items


class MetagraphApiImpl(BaseMetagraphApi):
    def __init__(self):
        self.context = get_context()

    def _matches_search(self, item: MetagraphItem, search: str) -> bool:
        """Check if item matches search query (case-insensitive, partial match)."""
        if not search:
            return True
        
        search_lower = search.lower()
        
        # Search in UID (partial match)
        if search_lower in str(item.uid).lower():
            return True
        
        # Search in hotkey (SS58 and hex)
        if item.hotkey:
            if search_lower in item.hotkey.ss58.lower() or search_lower in item.hotkey.hex.lower():
                return True
        
        # Search in coldkey (SS58 and hex)
        if item.coldkey:
            if search_lower in item.coldkey.ss58.lower() or search_lower in item.coldkey.hex.lower():
                return True
        
        # Search in axon IP
        if item.axon and isinstance(item.axon, dict):
            axon_ip = str(item.axon.get("ip", ""))
            if search_lower in axon_ip.lower():
                return True
        
        return False
    
    def _apply_filters(self, items: List[MetagraphItem], uid: Optional[int], active: Optional[bool],
                      hotkey: Optional[str], coldkey: Optional[str], validator_permit: Optional[bool],
                      is_immunity_period: Optional[bool], is_child_key: Optional[bool]) -> List[MetagraphItem]:
        """Apply filters to items."""
        filtered = items
        
        if uid is not None:
            filtered = [item for item in filtered if item.uid == uid]
        
        if active is not None:
            filtered = [item for item in filtered if item.active == active]
        
        if hotkey:
            hotkey_lower = hotkey.lower()
            filtered = [item for item in filtered 
                       if item.hotkey and (hotkey_lower in item.hotkey.ss58.lower() or hotkey_lower in item.hotkey.hex.lower())]
        
        if coldkey:
            coldkey_lower = coldkey.lower()
            filtered = [item for item in filtered 
                        if item.coldkey and (coldkey_lower in item.coldkey.ss58.lower() or coldkey_lower in item.coldkey.hex.lower())]
        
        if validator_permit is not None:
            filtered = [item for item in filtered if item.validator_permit == validator_permit]
        
        if is_immunity_period is not None:
            filtered = [item for item in filtered if item.is_immunity_period == is_immunity_period]
        
        if is_child_key is not None:
            filtered = [item for item in filtered if item.is_child_key == is_child_key]
        
        return filtered
    
    def _apply_ordering(self, items: List[MetagraphItem], order: Optional[MetagraphOrder]) -> List[MetagraphItem]:
        """Apply ordering to items."""
        if not order:
            return items
        
        order_str = order.value if hasattr(order, 'value') else str(order)
        reverse = order_str.endswith('_desc')
        field = order_str.rsplit('_', 1)[0]
        
        def get_sort_key(item: MetagraphItem):
            if field == 'uid':
                return item.uid
            elif field == 'updated':
                return item.updated
            elif field == 'stake':
                return float(item.stake) if item.stake else 0.0
            elif field == 'trust':
                return float(item.trust) if item.trust else 0.0
            elif field == 'validator_trust':
                return float(item.validator_trust) if item.validator_trust else 0.0
            elif field == 'consensus':
                return float(item.consensus) if item.consensus else 0.0
            elif field == 'incentive':
                return float(item.incentive) if item.incentive else 0.0
            elif field == 'dividends':
                return float(item.dividends) if item.dividends else 0.0
            elif field == 'emission':
                return float(item.emission) if item.emission else 0.0
            elif field == 'active':
                return 1 if item.active else 0
            elif field == 'hotkey':
                return item.hotkey.ss58 if item.hotkey else ""
            elif field == 'coldkey':
                return item.coldkey.ss58 if item.coldkey else ""
            elif field == 'validator_permit':
                return 1 if item.validator_permit else 0
            elif field == 'axon':
                if item.axon and isinstance(item.axon, dict):
                    return item.axon.get("ip", "")
                return ""
            elif field == 'daily_reward':
                return float(item.daily_reward) if item.daily_reward else 0.0
            elif field == 'registered_at':
                return item.registered_at_block
            elif field == 'is_immunity_period':
                return 1 if item.is_immunity_period else 0
            elif field == 'total_alpha_stake':
                return float(item.total_alpha_stake) if item.total_alpha_stake else 0.0
            else:
                return item.uid
        
        return sorted(items, key=get_sort_key, reverse=reverse)
    
    async def get_metagraph_latest(
        self,
        netuid: Annotated[Optional[int], Field(description="Subnet ID")],
        search: Annotated[Optional[StrictStr], Field(description="Search across UID, hotkey, coldkey, axon_ip")],
        uid: Annotated[Optional[int], Field(description="Neuron ID")],
        active: Optional[StrictBool],
        hotkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        coldkey: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")],
        validator_permit: Optional[StrictBool],
        is_immunity_period: Optional[StrictBool],
        is_child_key: Optional[StrictBool],
        page: Optional[int],
        limit: Optional[int],
        order: Optional[MetagraphOrder],
    ) -> MetagraphResponse:
        """Get latest metagraph data with mocked data"""
        netuid = netuid or 0
        metagraph_data = await self.context.redis.get(f"metagraph:{netuid}")
        
        items: List[MetagraphItem] = []
        if metagraph_data:
            metagraph = pickle.loads(metagraph_data)
            metagraph_info = MetagraphInfo.from_dict(metagraph)
            items = _convert_metagraph_info_to_items(metagraph_info)
        
        # Apply search filter
        if search:
            items = [item for item in items if self._matches_search(item, search)]
        
        # Apply other filters
        items = self._apply_filters(items, uid, active, hotkey, coldkey, validator_permit, 
                                   is_immunity_period, is_child_key)
        
        # Apply ordering
        items = self._apply_ordering(items, order)
        
        # Apply pagination
        total_items = len(items)
        per_page = limit or 10
        current_page = page or 1
        total_pages = (total_items + per_page - 1) // per_page if total_items > 0 else 0
        
        start_idx = (current_page - 1) * per_page
        end_idx = start_idx + per_page
        paginated_items = items[start_idx:end_idx]
        
        pagination = Pagination(
            current_page=current_page,
            next_page=current_page + 1 if current_page < total_pages else None,
            per_page=per_page,
            prev_page=current_page - 1 if current_page > 1 else None,
            total_items=total_items,
            total_pages=total_pages,
        )

        return MetagraphResponse(
            data=paginated_items,
            pagination=pagination
        )
