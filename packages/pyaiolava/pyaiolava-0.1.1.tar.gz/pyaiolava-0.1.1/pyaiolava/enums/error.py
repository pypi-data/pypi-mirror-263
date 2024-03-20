from enum import StrEnum


class InvoiceError(StrEnum):
    ORDERID_NOT_UNIQUE = 'orderId'
    NO_PAYMENT_METHODS = 'includeService.0'