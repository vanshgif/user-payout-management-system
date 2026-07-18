import uuid

from sqlalchemy import Column, Numeric, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database import Base
from app.core.enums import PayoutType, PayoutStatus


class Payout(Base):
    __tablename__ = "payouts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )

    sale_id = Column(
        UUID(as_uuid=True),
        ForeignKey("sales.id"),
        nullable=False
    )

    amount = Column(Numeric(10, 2), nullable=False)

    payout_type = Column(
        Enum(PayoutType),
        nullable=False
    )

    status = Column(
        Enum(PayoutStatus),
        default=PayoutStatus.PENDING,
        nullable=False
    )

    user = relationship("User", back_populates="payouts")

    sale = relationship("Sale", back_populates="payouts")