from uuid import UUID
from decimal import Decimal

from sqlalchemy.orm import Session

from app.models.user import User
from app.models.sales import Sale
from app.models.payout import Payout

from app.schemas.sale import SaleCreate

from app.core.enums import (
    SaleStatus,
    PayoutType,
    PayoutStatus,
)

from app.services.wallet_service import WalletService

from app.exceptions.custom_exceptions import (
    UserNotFoundException,
    SaleNotFoundException,
    InvalidSaleStatusException,
)


class SaleService:

    @staticmethod
    def create_sale(db: Session, sale_data: SaleCreate):

        user = db.query(User).filter(
            User.id == sale_data.user_id
        ).first()

        if not user:
            raise UserNotFoundException()

        sale = Sale(
            user_id=sale_data.user_id,
            brand=sale_data.brand,
            earning=sale_data.earning,
            status=SaleStatus.PENDING,
        )

        db.add(sale)
        db.commit()
        db.refresh(sale)

        return sale

    @staticmethod
    def update_sale_status(
        db: Session,
        sale_id: UUID,
        new_status: SaleStatus,
    ):

        sale = db.query(Sale).filter(
            Sale.id == sale_id
        ).first()

        if not sale:
            raise SaleNotFoundException()

        user = db.query(User).filter(
            User.id == sale.user_id
        ).first()

        if not user:
            raise UserNotFoundException()

        if sale.status != SaleStatus.PENDING:
            raise InvalidSaleStatusException(
                "Only pending sales can be updated."
            )

        # ------------------------
        # APPROVED
        # ------------------------
        if new_status == SaleStatus.APPROVED:

            existing_final_payout = db.query(Payout).filter(
                Payout.sale_id == sale.id,
                Payout.payout_type == PayoutType.FINAL,
            ).first()

            if existing_final_payout:
                raise InvalidSaleStatusException(
                    "Final payout already processed."
                )

            remaining_amount = sale.earning * Decimal("0.90")

            payout = Payout(
                user_id=user.id,
                sale_id=sale.id,
                amount=remaining_amount,
                payout_type=PayoutType.FINAL,
                status=PayoutStatus.SUCCESS,
            )

            WalletService.credit_wallet(
                user,
                remaining_amount,
            )

            db.add(payout)

        # ------------------------
        # REJECTED
        # ------------------------
        elif new_status == SaleStatus.REJECTED:

            if sale.advance_paid:

                adjustment = sale.earning * Decimal("0.10")

                payout = Payout(
                    user_id=user.id,
                    sale_id=sale.id,
                    amount=-adjustment,
                    payout_type=PayoutType.ADJUSTMENT,
                    status=PayoutStatus.SUCCESS,
                )

                WalletService.debit_wallet(
                    user,
                    adjustment,
                )

                db.add(payout)

        else:
            raise InvalidSaleStatusException(
                "Invalid sale status."
            )

        sale.status = new_status

        db.commit()
        db.refresh(sale)

        return sale