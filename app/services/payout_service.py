from decimal import Decimal

from sqlalchemy.orm import Session

from app.models.sales import Sale
from app.models.user import User
from app.models.payout import Payout
from app.core.enums import (
    SaleStatus,
    PayoutStatus,
    PayoutType,
)
from app.services.wallet_service import WalletService


class PayoutService:

    @staticmethod
    def process_advance_payouts(db: Session):

        eligible_sales = db.query(Sale).filter(
            Sale.status == SaleStatus.PENDING,
            Sale.advance_paid == False
        ).all()

        for sale in eligible_sales:

            user = db.query(User).filter(
                User.id == sale.user_id
            ).first()

            advance_amount = sale.earning * Decimal("0.10")

            payout = Payout(
                user_id=user.id,
                sale_id=sale.id,
                amount=advance_amount,
                payout_type=PayoutType.ADVANCE,
                status=PayoutStatus.SUCCESS
            )

            WalletService.credit_wallet(
                user,
                advance_amount
            )

            sale.advance_paid = True

            db.add(payout)

        db.commit()

        return eligible_sales