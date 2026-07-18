from uuid import UUID

from sqlalchemy.orm import Session

from app.models.sales import Sale
from app.models.user import User
from app.schemas.sale import SaleCreate
from app.core.enums import SaleStatus

from decimal import Decimal

from app.models.payout import Payout
from app.core.enums import (
    PayoutType,
    PayoutStatus,
)
from app.services.wallet_service import WalletService

class SaleService:

    @staticmethod
    def create_sale(db: Session, sale_data: SaleCreate):

        # Check whether user exists
        user = db.query(User).filter(
            User.id == sale_data.user_id
        ).first()

        if not user:
            raise ValueError("User not found")

        # Create Sale
        sale = Sale(
            user_id=sale_data.user_id,
            brand=sale_data.brand,
            earning=sale_data.earning,
            status=SaleStatus.PENDING
        )

        db.add(sale)

        db.commit()

        db.refresh(sale)

        return sale

@staticmethod
def update_sale_status(
    db: Session,
    sale_id,
    new_status: SaleStatus
):

    sale = db.query(Sale).filter(
        Sale.id == sale_id
    ).first()

    if not sale:
        raise ValueError("Sale not found")

    user = db.query(User).filter(
        User.id == sale.user_id
    ).first()

    sale.status = new_status

    # APPROVED
    if new_status == SaleStatus.APPROVED:
        existing_payout = db.query(Payout).filter(
            Payout.sale_id == sale.id,
            Payout.payout_type == PayoutType.FINAL
        ).first()

    if existing_payout:
        raise ValueError("Final payout already processed.")

    remaining_amount = sale.earning * Decimal("0.90")

    payout = Payout(
        user_id=user.id,
        sale_id=sale.id,
        amount=remaining_amount,
        payout_type=PayoutType.FINAL,
        status=PayoutStatus.SUCCESS
    )

    WalletService.credit_wallet(
        user,
        remaining_amount
    )

    db.add(payout)

    db.commit()

    db.refresh(sale)

    return sale