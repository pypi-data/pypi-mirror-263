from datetime import datetime
from typing import List

from pydantic import BaseModel

from ..enums import InvoiceStatus


class NewInvoiceModel(BaseModel):
    id: str | None = None
    shop_id: str | None = None
    shop_name: str | None = None
    amount: int | None = None
    payment_url: str | None = None

    payment_methods: List[str] | None = None

    status: int | None = None
    comment: str | None = None
    expired_at: datetime | None = None

class OldInvoiceModel(BaseModel):
    id: str | None = None
    payment_id: str | int = None
    shop_id: str | None = None
    amount: int | None = None

    payment_methods: List[str] | None = None
    fail_url: str | None = None
    success_url: str | None = None
    webhook_url: str | None = None

    status: InvoiceStatus | None = None
    custom_data: str | None = None
    error_message: str | None = None
    expired_at: datetime | None = None