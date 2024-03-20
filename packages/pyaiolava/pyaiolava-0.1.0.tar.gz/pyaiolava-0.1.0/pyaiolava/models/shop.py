from pydantic import BaseModel


class BalanceModel(BaseModel):
    current_amount: float | None = None
    frozen_amount: float | None = None