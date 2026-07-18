import uuid

from sqlalchemy import Column, String, Numeric, Enum, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database import Base
from app.core.enums import SaleStatus


class Sale(Base):
    __tablename__ = "sales"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )

    brand = Column(String, nullable=False)

    earning = Column(Numeric(10, 2), nullable=False)

    status = Column(
        Enum(SaleStatus),
        default=SaleStatus.PENDING,
        nullable=False
    )

    advance_paid = Column(Boolean,default=False, nullable=False)

    user = relationship("User", back_populates="sales")

    payouts = relationship("Payout", back_populates="sale")