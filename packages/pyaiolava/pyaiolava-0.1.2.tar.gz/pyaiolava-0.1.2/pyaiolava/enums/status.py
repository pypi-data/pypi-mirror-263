from enum import StrEnum


class InvoiceStatus(StrEnum):
    ERROR = 'error'
    CANCEL = 'cancel'
    PENDING = 'pending'
    SUCCESS = 'success'
    CREATED = 'created'
    EXPIRED = 'expired'