import json
import redis
from app.core.config import settings

redis_client = redis.Redis.from_url(settings.REDIS_URL)

def get_cache_prediction(key: str):
    cached_value = redis_client.get(key)
    if cached_value:
        return json.loads(cached_value)
    return None 