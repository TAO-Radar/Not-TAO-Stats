# worker.py
import asyncio
from datetime import timedelta
from typing import Callable, Awaitable
import bittensor as bt
from pydantic_settings import BaseSettings
from .tasks.sync_metagraph import sync_metagraphs
from redis.asyncio import Redis
from .utils.timing import measure_time
from .context import Context, get_context


def create_sync_worker(
    sync_func: Callable[[Context], Awaitable[None]],
    interval: timedelta,
    name: str
) -> Callable[[Context], Awaitable[None]]:
    """
    Creates a sync worker function that runs sync_func in a loop.
    
    Args:
        sync_func: Async function that performs the sync operation
        interval: Sleep interval in seconds between syncs
        name: Name for logging and timing
    
    Returns:
        Async function that runs the sync worker
    """
    @measure_time(f"{name} Sync Cycle")
    async def _sync_cycle(context: Context):
        """Single sync cycle - wrapped for timing"""
        await sync_func(context)
    
    async def sync_worker(context: Context):
        """Generic sync worker template"""
        while True:
            try:
                await _sync_cycle(context)
            except Exception as e:
                print(f"{name} error:", e)
            await asyncio.sleep(interval.total_seconds())
    
    return sync_worker


async def _sync_metagraph_task(context: Context):
    """Metagraph sync task implementation"""
    await sync_metagraphs(context.subtensor, context.redis)

async def _sync_scores_task(context: Context):
    """Scores sync task implementation"""


async def main():
    context = get_context()
    
    # Create sync workers using the template
    sync_metagraph = create_sync_worker(
        sync_func=_sync_metagraph_task,
        interval=context.settings.sync_metagraph_interval,
        name="Metagraph"
    )
    
    sync_scores = create_sync_worker(
        sync_func=_sync_scores_task,
        interval=context.settings.sync_scores_interval,
        name="Scores"
    )
    
    await asyncio.gather(
        sync_metagraph(context),
        sync_scores(context),
    )

if __name__ == "__main__":
    asyncio.run(main())