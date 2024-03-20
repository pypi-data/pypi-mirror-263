import hashlib
import hmac
import json


async def is_valid_signature(data: dict, api_key: str, sign_token: str) -> bool:
    """
    Checking the signature contained in the headers of webhooks from the Lava API.

    Args:
        data (dict): Returned payment details.
        api_key (str): API key Business Lava API
        sign_token (str): Signature, in headers['authorization']
    """
    new_data = dict(sorted(data.items(), key=lambda x: x[0]))
    json_str = json.dumps(new_data, separators=(',', ':')).encode()
    new_sign = hmac.new(bytes(api_key, 'UTF-8'), json_str, hashlib.sha256).hexdigest()
    return new_sign == sign_token