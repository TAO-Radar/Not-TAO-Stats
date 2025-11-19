from datetime import timedelta
from pydantic_settings import BaseSettings
    

class Settings(BaseSettings):
    network: str = "finney"
    sync_metagraph_interval: timedelta = timedelta(seconds=10)
    sync_scores_interval: timedelta = timedelta(seconds=300)
    redis_url: str = "redis://localhost:6379"
