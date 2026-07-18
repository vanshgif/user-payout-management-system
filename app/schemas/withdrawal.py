from uuid import UUID
from decimal import Decimal

from pydantic import BaseModel, ConfigDict

from app.core.enums import WithdrawalStatus


class WithdrawalCreate(BaseModel):
    user_id: UUID
    amount: Decimal


class WithdrawalResponse(BaseModel):
    id: UUID
    user_id: UUID
    amount: Decimal
    status: WithdrawalStatus

    model_config = ConfigDict(from_attributes=True)