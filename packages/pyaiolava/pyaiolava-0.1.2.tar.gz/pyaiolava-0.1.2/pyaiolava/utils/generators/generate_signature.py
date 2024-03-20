import hashlib
import hmac
import json
from typing import Tuple


def generate_signature(data: dict, api_key: str) -> Tuple[dict, dict]:
    """
    Generates a signature for requests to the Lava API.

    Args:
        data (dict): JSON data required for the method.
        api_key (str): API key for signing.

    Returns:
        headers, new_data (tuple): Headers with signature and JSON data
    """
    new_data = dict(sorted(data.items(), key=lambda x: x[0]))
    json_str = json.dumps(new_data).encode()
    sign = hmac.new(bytes(api_key, 'UTF-8'), json_str, hashlib.sha256).hexdigest()
    headers = {
        'Signature': sign,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    return headers, new_data
