from pyaiolava.constants import MIN_PAYMENT_AMOUNT, MAX_PAYMENT_AMOUNT


def is_valid_amount(amount: float) -> bool:
    return MIN_PAYMENT_AMOUNT <= amount <= MAX_PAYMENT_AMOUNT
