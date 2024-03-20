class AiolavaError(Exception):
    pass

class InvoiceError(Exception):
    pass

class AuthError(AiolavaError):
    pass

class RequestError(AiolavaError):
    pass

class PaymentIdNonUniqueError(InvoiceError):
    """Non-unique payment ID."""
    pass

class MutuallyExclusiveError(InvoiceError):
    """Mutually exclusive IDs"""
    pass

class AmountInvalidError(InvoiceError):
    """Incorrect payment amount."""
    pass

class NoPaymentMethodsError(InvoiceError):
    """Payment methods are not specified."""
    pass

class InvoiceNotFoundError(InvoiceError):
    """Invoice not found."""
    pass

class PaymentTimeInvalidError(InvoiceError):
    """Payment time is invalid."""
    pass