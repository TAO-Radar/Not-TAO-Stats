import pickle
from datetime import datetime
from typing import Optional, List
from bittensor import MetagraphInfo, SubnetIdentity
from openapi_server.models.pagination import Pagination
from openapi_server.models.dtao_pool_order import DtaoPoolOrder
from openapi_server.models.dtao_pool_item import DtaoPoolItem
from openapi_server.models.dtao_pool_daily_price_item import DtaoPoolDailyPriceItem
from openapi_server.context import get_context
from openapi_server.apis.pool_api_base import BasePoolApi
from openapi_server.models.dtao_pool_response import DtaoPoolResponse


def _convert_metagraph_info_to_items(metagraph_info: MetagraphInfo) -> List[DtaoPoolItem]:
    """Convert MetagraphInfo to a list of DtaoPoolItem objects (one per netuid)."""
    items = []
    
    # Aggregate data from all neurons in the metagraph
    num_uids = metagraph_info.num_uids
    
    # Calculate aggregated values
    total_alpha_stake = sum(
        (metagraph_info.alpha_stake[uid].rao if uid < len(metagraph_info.alpha_stake) and metagraph_info.alpha_stake[uid] else 0)
        for uid in range(num_uids)
    )
    
    total_tao_stake = sum(
        (metagraph_info.tao_stake[uid].rao if uid < len(metagraph_info.tao_stake) and metagraph_info.tao_stake[uid] else 0)
        for uid in range(num_uids)
    )
    tao_in = metagraph_info.tao_in
    alpha_in = metagraph_info.alpha_in
    
    
    # Calculate alpha_staked (sum of all alpha stakes)
    alpha_staked = str(total_alpha_stake)
    
    # Calculate total_alpha (same as alpha_staked for now)
    total_alpha = str(total_alpha_stake)
    
    # Calculate total_tao (sum of all tao stakes)
    total_tao = str(total_tao_stake)
    
    # Calculate alpha_in_pool (could be same as total_alpha or different)
    alpha_in_pool = str(total_alpha_stake)
    
    # Calculate liquidity (simplified - could be based on pool formula)
    liquidity = str(total_alpha_stake + total_tao_stake)
    
    # Calculate market_cap (simplified)
    market_cap = str(alpha_in)
    
    # Calculate price (simplified - alpha/tao ratio)
    price = "0"
    if total_tao_stake > 0:
        price = str(tao_in.rao / alpha_in.rao)
    
    # Get netuid
    netuid = metagraph_info.netuid
    
    # Calculate rank (could be based on total stake or other metrics)
    # For now, using netuid as rank
    rank = netuid
    
    # Calculate root_prop (proportion of root stake)
    root_prop = "0"
    if total_alpha_stake > 0:
        root_prop = str(total_tao_stake / total_alpha_stake)
    
    # Calculate startup_mode (check if metagraph is in startup)
    startup_mode = metagraph_info.immunity_period > 0 if hasattr(metagraph_info, 'immunity_period') else False
    
    # Name and symbol (derived from netuid)
    identity = SubnetIdentity._from_dict(metagraph_info.identity)
    name = identity.subnet_name
    symbol = metagraph_info.symbol
    
    # Default values for fields not available in MetagraphInfo
    alpha_buy_volume_24_hr = "0"
    alpha_sell_volume_24_hr = "0"
    alpha_volume_24_hr = "0"
    tao_buy_volume_24_hr = "0"
    tao_sell_volume_24_hr = "0"
    tao_volume_24_hr = "0"
    buyers_24_hr = 0
    sellers_24_hr = 0
    buys_24_hr = 0
    sells_24_hr = 0
    seven_day_prices: List[DtaoPoolDailyPriceItem] = []
    
    item = DtaoPoolItem(
        alpha_buy_volume_24_hr=alpha_buy_volume_24_hr,
        alpha_in_pool=alpha_in_pool,
        alpha_sell_volume_24_hr=alpha_sell_volume_24_hr,
        alpha_sqrt_price=None,
        alpha_staked=alpha_staked,
        alpha_volume_24_hr=alpha_volume_24_hr,
        alpha_volume_24_hr_change_1_day=None,
        block_number=metagraph_info.block,
        buyers_24_hr=buyers_24_hr,
        buys_24_hr=buys_24_hr,
        current_tick=None,
        enabled_user_liquidity=None,
        fear_and_greed_index=None,
        fear_and_greed_sentiment=None,
        fee_global_alpha=None,
        fee_global_tao=None,
        fee_rate=None,
        highest_price_24_hr=None,
        last_price=None,
        liquidity=liquidity,
        liquidity_raw=None,
        lowest_price_24_hr=None,
        market_cap=market_cap,
        market_cap_change_1_day=None,
        name=name,
        netuid=netuid,
        price=price,
        price_change_1_day=None,
        price_change_1_hour=None,
        price_change_1_month=None,
        price_change_1_week=None,
        protocol_provided_alpha=None,
        protocol_provided_tao=None,
        rank=rank,
        root_prop=root_prop,
        sellers_24_hr=sellers_24_hr,
        sells_24_hr=sells_24_hr,
        seven_day_prices=seven_day_prices,
        startup_mode=startup_mode,
        swap_v3_initialized=None,
        symbol=symbol,
        tao_buy_volume_24_hr=tao_buy_volume_24_hr,
        tao_sell_volume_24_hr=tao_sell_volume_24_hr,
        tao_volume_24_hr=tao_volume_24_hr,
        tao_volume_24_hr_change_1_day=None,
        timestamp=datetime.now(),
        total_alpha=total_alpha,
        total_tao=total_tao,
        user_provided_alpha=None,
        user_provided_tao=None,
    )
    items.append(item)
    
    return items


class PoolApiImpl(BasePoolApi):
    def __init__(self):
        self.context = get_context()

    async def get_dtao_pool_latest(self, netuid: Optional[int], page: Optional[int], limit: Optional[int], order: Optional[DtaoPoolOrder]) -> DtaoPoolResponse:
        netuid = netuid or 0
        metagraph = await self.context.redis.get(f"metagraph:{netuid}")
        if metagraph:
            metagraph = pickle.loads(metagraph)
            metagraph_info = MetagraphInfo.from_dict(metagraph)
            items = _convert_metagraph_info_to_items(metagraph_info)
        else:
            items = []
        
        # Calculate pagination
        total_items = len(items)
        per_page = limit or 10
        current_page = page or 1
        total_pages = (total_items + per_page - 1) // per_page if total_items > 0 else 1
        
        # Apply pagination
        start_idx = (current_page - 1) * per_page
        end_idx = start_idx + per_page
        paginated_items = items[start_idx:end_idx]
        
        pagination = Pagination(
            current_page=current_page,
            per_page=per_page,
            total_pages=total_pages,
            total_items=total_items,
        )
        
        return DtaoPoolResponse(data=paginated_items, pagination=pagination) 