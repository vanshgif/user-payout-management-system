from uuid import UUID
from decimal import Decimal

from pydantic import BaseModel, ConfigDict

from app.core.enums import PayoutStatus, PayoutType


class PayoutResponse(BaseModel):
    id: UUID
    user_id: UUID
    sale_id: UUID
    amount: Decimal
    payout_type: PayoutType
    status: PayoutStatus

    model_config = ConfigDict(from_attributes=True)