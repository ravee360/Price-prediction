import os
import json
import redis
from dotenv import load_dotenv
import numpy as np

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL")

# keep decode_responses=True so Redis returns/accepts strings
redis_client = redis.StrictRedis.from_url(REDIS_URL, decode_responses=True)


def _convert_to_json_serializable(obj):
    """Recursively convert NumPy types to native Python types for JSON."""
    if isinstance(obj, (np.integer,)):
        return int(obj)
    if isinstance(obj, (np.floating,)):
        return float(obj)
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if isinstance(obj, dict):
        return {k: _convert_to_json_serializable(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_convert_to_json_serializable(v) for v in obj]
    return obj


def get_cached_prediction(key: str):
    value = redis_client.get(key)
    if not value:
        return None
    try:
        return json.loads(value)
    except Exception:
        # If parsing fails, return None so caller computes fresh prediction
        return None


def set_cached_prediction(key: str, value: dict):
    safe_value = _convert_to_json_serializable(value)
    redis_client.set(key, json.dumps(safe_value))