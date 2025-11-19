import pickle
import redis
import bittensor as bt


async def sync_metagraphs(subtensor: bt.AsyncSubtensor, redis: redis.Redis):
    query = await subtensor.query_runtime_api(
            runtime_api="SubnetInfoRuntimeApi",
            method="get_all_metagraphs",
            params=None,
    )
    for metagraph in query:
        pickled_data = pickle.dumps(metagraph)
        await redis.set(f"metagraph:{metagraph['netuid']}", pickled_data)
    