from uuid import UUID
from decimal import Decimal

from pydantic import BaseModel, ConfigDict

from app.core.enums import SaleStatus
from app.core.enums import SaleStatus


class SaleCreate(BaseModel):
    user_id: UUID
    brand: str
    earning: Decimal


class SaleResponse(BaseModel):
    id: UUID
    user_id: UUID
    brand: str
    earning: Decimal
    status: SaleStatus
    advance_paid: bool

    model_config = ConfigDict(from_attributes=True)

class SaleStatusUpdate(BaseModel):
    status: SaleStatus