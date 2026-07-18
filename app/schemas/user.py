from uuid import UUID
from decimal import Decimal

from pydantic import BaseModel, EmailStr, ConfigDict


class UserCreate(BaseModel):
    username: str
    email: EmailStr


class UserResponse(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    wallet_balance: Decimal

    model_config = ConfigDict(from_attributes=True)