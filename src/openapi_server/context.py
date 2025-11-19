
from functools import lru_cache
from .settings import Settings
import bittensor as bt
from redis.asyncio import Redis

class Context:
    def __init__(self):
        self.settings = Settings()
        self.subtensor = bt.AsyncSubtensor(network=self.settings.network)
        self.redis = Redis.from_url(self.settings.redis_url)


@lru_cache
def get_context() -> Context:
    return Context()