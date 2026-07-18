import uuid

from sqlalchemy import Column, Numeric, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database import Base
from app.core.enums import WithdrawalStatus


class Withdrawal(Base):
    __tablename__ = "withdrawals"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )

    amount = Column(
        Numeric(10, 2),
        nullable=False
    )

    status = Column(
        Enum(WithdrawalStatus),
        default=WithdrawalStatus.PENDING,
        nullable=False
    )

    user = relationship(
        "User",
        back_populates="withdrawals"
    )