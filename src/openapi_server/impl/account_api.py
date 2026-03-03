import pickle
from datetime import date, datetime, timedelta
from typing import Annotated, List, Optional, Tuple

from pydantic import Field, StrictStr
from bittensor import MetagraphInfo
from openapi_server.constants import SECONDS_IN_BLOCKS
from openapi_server.apis.account_api_base import BaseAccountApi
from openapi_server.models.account_response import AccountResponse
from openapi_server.models.account_item import AccountItem
from openapi_server.models.account_order import AccountOrder
from openapi_server.models.pagination import Pagination
from openapi_server.models.key import Key
from openapi_server.models.alpha_balance import AlphaBalance
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


def _hex_to_ss58(hex_address: str) -> str:
    """Convert hex address to SS58 format."""
    try:
        from scalecodec.utils.ss58 import ss58_encode
        # Remove 0x prefix if present
        hex_bytes = bytes.fromhex(hex_address[2:] if hex_address.startswith("0x") else hex_address)
        return ss58_encode(hex_bytes, 42)  # 42 is the SS58 prefix for Substrate
    except Exception:
        # Fallback: return placeholder
        return hex_address


def _normalize_address(address: str) -> Tuple[str, str]:
    """Normalize address to both SS58 and hex formats. Returns (ss58, hex)."""
    if not address:
        return "", ""
    
    if address.startswith("0x"):
        # It's hex, convert to SS58
        ss58 = _hex_to_ss58(address)
        return ss58, address
    else:
        # Assume it's SS58, convert to hex
        hex_addr = _ss58_to_hex(address)
        return address, hex_addr


class AccountApiImpl(BaseAccountApi):
    def __init__(self):
        self.context = get_context()

    def _get_metagraph_price(self, metagraph_info: MetagraphInfo) -> float:
        """Calculate price from metagraph using the same logic as pool_api.py.
        Price represents TAO per alpha (tao_in / alpha_in).
        """
        try:
            tao_in = metagraph_info.tao_in
            alpha_in = metagraph_info.alpha_in
            
            # Price calculation from pool_api.py: tao_in.rao / alpha_in.rao
            # Check if we have valid values (matching pool_api logic)
            if alpha_in and alpha_in.rao > 0 and tao_in:
                return tao_in.rao / alpha_in.rao
            return 0.0
        except Exception:
            return 0.0

    async def _get_account_data(self, address: str, block: int, block_24h_ago: int) -> Optional[AccountItem]:
        """Get account data for a single address."""
        try:
            # Normalize address
            ss58_addr, hex_addr = _normalize_address(address)
            if not ss58_addr and not hex_addr:
                return None

            # Get balance data
            balance_result = await self.context.subtensor.get_balance(address=ss58_addr, block=block)
            balance_24h_ago_result = await self.context.subtensor.get_balance(address=ss58_addr, block=block_24h_ago)
            
            # Get stake data - returns list of stake info per subnet
            stake_result_list = await self.context.subtensor.get_stake_info_for_coldkey(coldkey_ss58=ss58_addr, block=block)
            stake_24h_ago_result_list = await self.context.subtensor.get_stake_info_for_coldkey(coldkey_ss58=ss58_addr, block=block_24h_ago)

            # Process stake info per subnet first (needed for reserved balance calculation)
            stake_total_rao = 0
            stake_root_rao = 0
            stake_alpha_rao = 0
            stake_alpha_as_tao_rao = 0.0
            
            stake_total_24h_ago_rao = 0
            stake_root_24h_ago_rao = 0
            stake_alpha_24h_ago_rao = 0
            stake_alpha_as_tao_24h_ago_rao = 0.0

            # Get alpha balances from metagraphs
            alpha_balances: List[AlphaBalance] = []
            alpha_balances_24h_ago: List[AlphaBalance] = []
            
            # Process current stake results
            if stake_result_list:
                for stake_info in stake_result_list:
                    try:
                        netuid = stake_info.netuid if hasattr(stake_info, 'netuid') else None
                        if netuid is None:
                            continue
                            
                        # Get metagraph for price calculation
                        metagraph_data = await self.context.redis.get(f"metagraph:{netuid}")
                        if not metagraph_data:
                            continue
                            
                        metagraph = pickle.loads(metagraph_data)
                        metagraph_info = MetagraphInfo.from_dict(metagraph)
                        price = self._get_metagraph_price(metagraph_info)
                        
                        # Extract stake values from stake_info
                        # Alpha stake rao = stake_info.rao
                        # Handle both Balance object and direct rao value
         
                        alpha_stake_rao = stake_info.stake.rao
                        
                        # Root stake = stake_info where netuid == 0
                        if netuid == 0:
                            stake_root_rao += alpha_stake_rao
                        
                        # Total stake is sum of all stakes across all subnets
                        stake_total_rao += alpha_stake_rao
                        stake_alpha_rao += alpha_stake_rao
                        
                        # Convert alpha to TAO using price
                        if price > 0:
                            stake_alpha_as_tao_rao += alpha_stake_rao * price
                        
                        # Get hotkey from stake_info if available
                        hotkey_ss58 = stake_info.hotkey_ss58
                        # Add to alpha balances if we have alpha stake
                        if alpha_stake_rao > 0:
                            hotkey_hex = _ss58_to_hex(hotkey_ss58) if hotkey_ss58 else ""
                            alpha_as_tao = str(alpha_stake_rao * price) if price > 0 else "0"
                            
                            alpha_balances.append(AlphaBalance(
                                balance=str(alpha_stake_rao),
                                balance_as_tao=alpha_as_tao,
                                coldkey=ss58_addr,
                                hotkey=hotkey_ss58,
                                netuid=netuid
                            ))
                    except Exception as e:
                        continue
            
            # Process 24h ago stake results
            if stake_24h_ago_result_list:
                for stake_info in stake_24h_ago_result_list:
                    try:
                        netuid = stake_info.netuid if hasattr(stake_info, 'netuid') else None
                        if netuid is None:
                            continue
                            
                        # Get metagraph for price calculation
                        metagraph_data = await self.context.redis.get(f"metagraph:{netuid}")
                        if not metagraph_data:
                            continue
                            
                        metagraph = pickle.loads(metagraph_data)
                        metagraph_info = MetagraphInfo.from_dict(metagraph)
                        price = self._get_metagraph_price(metagraph_info)
                        
                        # Extract stake values from stake_info
                        # Alpha stake rao = stake_info.rao
                        # Handle both Balance object and direct rao value
                        alpha_stake_rao = stake_info.stake.rao
                        
                        # Root stake = stake_info where netuid == 0
                        if netuid == 0:
                            stake_root_24h_ago_rao += alpha_stake_rao
                        
                        # Total stake is sum of all stakes across all subnets
                        stake_total_24h_ago_rao += alpha_stake_rao
                        stake_alpha_24h_ago_rao += alpha_stake_rao
                        
                        # Convert alpha to TAO using price
                        if price > 0:
                            stake_alpha_as_tao_24h_ago_rao += alpha_stake_rao * price
                    except Exception:
                        continue
            
            # Extract balance components
            # balance_result.rao gives the free balance in rao
            balance_free_rao = balance_result.rao if balance_result else 0
            balance_free_24h_ago_rao = balance_24h_ago_result.rao if balance_24h_ago_result else 0
            
            # Reserved balance = staked balance in TAO (converted to rao)
            # stake_total_rao is already in rao (from TAO)
            balance_reserved_rao = stake_total_rao
            balance_reserved_24h_ago_rao = stake_total_24h_ago_rao
            
            # Total = reserved + free
            balance_total_rao = balance_reserved_rao + balance_free_rao
            balance_total_24h_ago_rao = balance_reserved_24h_ago_rao + balance_free_24h_ago_rao
            
            # Convert to strings
            balance_free = str(int(balance_free_rao))
            balance_reserved = str(int(balance_reserved_rao))
            balance_total = str(int(balance_total_rao))
            balance_liquidity = "0"  # Not directly available from subtensor
            
            balance_free_24h_ago = str(int(balance_free_24h_ago_rao))
            balance_reserved_24h_ago = str(int(balance_reserved_24h_ago_rao))
            balance_total_24h_ago = str(int(balance_total_24h_ago_rao))
            balance_liquidity_24h_ago = "0"
            
            # Convert stake to strings (using int to convert float to avoid decimal places for RAO)
            stake_total = str(int(stake_total_rao))
            stake_root = str(int(stake_root_rao))
            stake_alpha_as_tao = str(int(stake_alpha_as_tao_rao))
            
            stake_total_24h_ago = str(int(stake_total_24h_ago_rao))
            stake_root_24h_ago = str(int(stake_root_24h_ago_rao))
            stake_alpha_as_tao_24h_ago = str(int(stake_alpha_as_tao_24h_ago_rao))

            # Get network name from settings
            network = self.context.settings.network or "finney"
            
            # Get timestamp for current block
            timestamp = datetime.now()  # Would ideally get from block timestamp
            
            # Get rank (would need to calculate from stake or other metrics)
            rank = 0  # Simplified - would need to calculate
            
            # Get created_on information (would need to query from chain)
            created_on_network = network
            created_on_date = date.today()  # Simplified - would need to query from chain
            
            # Root claim type (would need to query from chain)
            root_claim_type = "none"  # Simplified

            return AccountItem(
                address=Key(hex=hex_addr, ss58=ss58_addr),
                alpha_balances=alpha_balances if alpha_balances else None,
                alpha_balances_24hr_ago=alpha_balances_24h_ago if alpha_balances_24h_ago else None,
                balance_free=balance_free,
                balance_free_24hr_ago=balance_free_24h_ago,
                balance_liquidity=balance_liquidity,
                balance_liquidity_24hr_ago=balance_liquidity_24h_ago,
                balance_reserved=balance_reserved,
                balance_reserved_24hr_ago=balance_reserved_24h_ago,
                balance_staked=stake_total,
                balance_staked_24hr_ago=stake_total_24h_ago,
                balance_staked_alpha_as_tao=stake_alpha_as_tao,
                balance_staked_alpha_as_tao_24hr_ago=stake_alpha_as_tao_24h_ago,
                balance_staked_root=stake_root,
                balance_staked_root_24hr_ago=stake_root_24h_ago,
                balance_total=balance_total,
                balance_total_24hr_ago=balance_total_24h_ago,
                block_number=block,
                coldkey_swap=None,
                created_on_date=created_on_date,
                created_on_network=created_on_network,
                network=network,
                rank=rank,
                root_claim_type=root_claim_type,
                timestamp=timestamp
            )
        except Exception:
            return None

    def _apply_filters(self, items: List[AccountItem], address: Optional[str],
                      balance_free_min: Optional[str], balance_free_max: Optional[str],
                      balance_staked_min: Optional[str], balance_staked_max: Optional[str],
                      balance_staked_root_min: Optional[str], balance_staked_root_max: Optional[str],
                      balance_staked_alpha_as_tao_min: Optional[str], balance_staked_alpha_as_tao_max: Optional[str],
                      balance_total_min: Optional[str], balance_total_max: Optional[str],
                      rank: Optional[int], created_on_network: Optional[str],
                      created_on_timestamp_start: Optional[int], created_on_timestamp_end: Optional[int]) -> List[AccountItem]:
        """Apply filters to account items."""
        filtered = items

        if address:
            ss58_addr, hex_addr = _normalize_address(address)
            filtered = [item for item in filtered 
                       if item.address and (item.address.ss58 == ss58_addr or item.address.hex == hex_addr)]

        if balance_free_min:
            min_val = float(balance_free_min)
            filtered = [item for item in filtered if float(item.balance_free) >= min_val]
        
        if balance_free_max:
            max_val = float(balance_free_max)
            filtered = [item for item in filtered if float(item.balance_free) <= max_val]

        if balance_staked_min:
            min_val = float(balance_staked_min)
            filtered = [item for item in filtered if float(item.balance_staked) >= min_val]
        
        if balance_staked_max:
            max_val = float(balance_staked_max)
            filtered = [item for item in filtered if float(item.balance_staked) <= max_val]

        if balance_staked_root_min:
            min_val = float(balance_staked_root_min)
            filtered = [item for item in filtered if float(item.balance_staked_root) >= min_val]
        
        if balance_staked_root_max:
            max_val = float(balance_staked_root_max)
            filtered = [item for item in filtered if float(item.balance_staked_root) <= max_val]

        if balance_staked_alpha_as_tao_min:
            min_val = float(balance_staked_alpha_as_tao_min)
            filtered = [item for item in filtered if float(item.balance_staked_alpha_as_tao) >= min_val]
        
        if balance_staked_alpha_as_tao_max:
            max_val = float(balance_staked_alpha_as_tao_max)
            filtered = [item for item in filtered if float(item.balance_staked_alpha_as_tao) <= max_val]

        if balance_total_min:
            min_val = float(balance_total_min)
            filtered = [item for item in filtered if float(item.balance_total) >= min_val]
        
        if balance_total_max:
            max_val = float(balance_total_max)
            filtered = [item for item in filtered if float(item.balance_total) <= max_val]

        if rank is not None:
            filtered = [item for item in filtered if item.rank == rank]

        if created_on_network:
            filtered = [item for item in filtered if item.created_on_network == created_on_network]

        if created_on_timestamp_start:
            start_ts = datetime.fromtimestamp(created_on_timestamp_start)
            filtered = [item for item in filtered if item.timestamp >= start_ts]

        if created_on_timestamp_end:
            end_ts = datetime.fromtimestamp(created_on_timestamp_end)
            filtered = [item for item in filtered if item.timestamp <= end_ts]

        return filtered

    def _apply_ordering(self, items: List[AccountItem], order: Optional[AccountOrder]) -> List[AccountItem]:
        """Apply ordering to items."""
        if not order:
            return items

        order_str = order.value if hasattr(order, 'value') else str(order)
        reverse = order_str.endswith('_desc')
        field = order_str.rsplit('_', 1)[0]

        def get_sort_key(item: AccountItem):
            if field == 'balance_free':
                return float(item.balance_free) if item.balance_free else 0.0
            elif field == 'balance_staked':
                return float(item.balance_staked) if item.balance_staked else 0.0
            elif field == 'balance_staked_root':
                return float(item.balance_staked_root) if item.balance_staked_root else 0.0
            elif field == 'balance_staked_alpha_as_tao':
                return float(item.balance_staked_alpha_as_tao) if item.balance_staked_alpha_as_tao else 0.0
            elif field == 'balance_total':
                return float(item.balance_total) if item.balance_total else 0.0
            elif field == 'created_at_timestamp':
                return item.timestamp.timestamp() if item.timestamp else 0.0
            else:
                return 0.0

        return sorted(items, key=get_sort_key, reverse=reverse)

    async def get_account_latest(self, address: Annotated[Optional[StrictStr], Field(description="SS58 or hex format")], balance_free_min: Optional[StrictStr], balance_free_max: Optional[StrictStr], balance_staked_min: Optional[StrictStr], balance_staked_max: Optional[StrictStr], balance_staked_root_min: Optional[StrictStr], balance_staked_root_max: Optional[StrictStr], balance_staked_alpha_as_tao_min: Optional[StrictStr], balance_staked_alpha_as_tao_max: Optional[StrictStr], balance_total_min: Optional[StrictStr], balance_total_max: Optional[StrictStr], rank: Optional[int], created_on_network: Annotated[Optional[StrictStr], Field(description="finney, nakamoto, kusanagi")], created_on_timestamp_start: Annotated[Optional[int], Field(description="Start of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")], created_on_timestamp_end: Annotated[Optional[int], Field(description="End of timestamp range in Unix timestamp (seconds since 1970-01-01) (inclusive)")], page: Optional[int], limit: Optional[int], order: Optional[AccountOrder]) -> AccountResponse:
        """Get latest account data with filtering, ordering, and pagination."""
        block = await self.context.subtensor.get_current_block()
        block_24h_ago = int(block - timedelta(hours=24).total_seconds() // SECONDS_IN_BLOCKS)

        items: List[AccountItem] = []

        if address:
            # Get data for specific address
            account_data = await self._get_account_data(address, block, block_24h_ago)
            if account_data:
                items.append(account_data)
        else:
            # Get all unique coldkeys from metagraphs
            netuids = await self.context.subtensor.get_all_subnet_netuids()
            unique_coldkeys = set()
            
            for netuid in netuids:
                try:
                    metagraph_data = await self.context.redis.get(f"metagraph:{netuid}")
                    if metagraph_data:
                        metagraph = pickle.loads(metagraph_data)
                        metagraph_info = MetagraphInfo.from_dict(metagraph)
                        unique_coldkeys.update(metagraph_info.coldkeys)
                except Exception:
                    continue

            # Get account data for each unique coldkey
            for coldkey in unique_coldkeys:
                if coldkey:
                    account_data = await self._get_account_data(coldkey, block, block_24h_ago)
                    if account_data:
                        items.append(account_data)

        # Apply filters
        items = self._apply_filters(items, address, balance_free_min, balance_free_max,
                                   balance_staked_min, balance_staked_max,
                                   balance_staked_root_min, balance_staked_root_max,
                                   balance_staked_alpha_as_tao_min, balance_staked_alpha_as_tao_max,
                                   balance_total_min, balance_total_max, rank,
                                   created_on_network, created_on_timestamp_start, created_on_timestamp_end)

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

        return AccountResponse(
            data=paginated_items,
            pagination=pagination
        )
