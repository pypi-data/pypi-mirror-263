import random
import string


def generate_payment_id(length: int = 10) -> str:
    """
    Generates a unique payment ID. Use the payment ID in your system, this generator is for testing purposes.

    Args:
        length (int, optional): Length of ID.

    Returns:
        str: Unique payment ID.
    """
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))
