from ...constants import MIN_PAYMENT_TIME, MAX_PAYMENT_TIME


def is_valid_payment_time(minutes: int) -> bool:
    return MIN_PAYMENT_TIME <= minutes <= MAX_PAYMENT_TIME