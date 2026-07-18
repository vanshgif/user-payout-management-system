import uuid

from sqlalchemy import Column, String, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    username = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False)

    wallet_balance = Column(Numeric(10, 2), default=0)

    sales = relationship("Sale", back_populates="user")

    payouts = relationship("Payout", back_populates="user")

    withdrawals = relationship("Withdrawal", back_populates="user")