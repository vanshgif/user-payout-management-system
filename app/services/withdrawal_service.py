from datetime import datetime, timedelta
from uuid import UUID

from sqlalchemy.orm import Session

from app.exceptions.custom_exceptions import UserNotFoundException, WithdrawalNotFoundException
from app.models.user import User
from app.models.withdrawal import Withdrawal
from app.core.enums import WithdrawalStatus
from app.schemas.withdrawal import WithdrawalCreate
from app.services.wallet_service import WalletService
from app.exceptions.custom_exceptions import  WithdrawalAlreadyProcessedException

class WithdrawalService:

    @staticmethod
    def create_withdrawal(db: Session, withdrawal_data: WithdrawalCreate):

        # Find user
        user = db.query(User).filter(User.id == withdrawal_data.user_id).first()

        if not user:
            raise ()

        # Check last successful/pending withdrawal
        last_withdrawal = (
            db.query(Withdrawal)
            .filter(
                Withdrawal.user_id == withdrawal_data.user_id,
                Withdrawal.status.in_(
                    [
                        WithdrawalStatus.PENDING,
                        WithdrawalStatus.SUCCESS,
                    ]
                ),
            )
            .order_by(Withdrawal.created_at.desc())
            .first()
        )

        if last_withdrawal:
            time_difference = datetime.utcnow() - last_withdrawal.created_at

            if time_difference < timedelta(hours=24):
                remaining = timedelta(hours=24) - time_difference
                hours = int(remaining.total_seconds() // 3600)
                minutes = int((remaining.total_seconds() % 3600) // 60)

                raise ValueError(
                    f"You can withdraw again after {hours} hour(s) and {minutes} minute(s)."
                )

        # Debit wallet (WalletService already validates balance)
        WalletService.debit_wallet(user, withdrawal_data.amount)

        withdrawal = Withdrawal(
            user_id=withdrawal_data.user_id,
            amount=withdrawal_data.amount,
            status=WithdrawalStatus.PENDING,
        )

        db.add(withdrawal)
        db.commit()
        db.refresh(withdrawal)

        return withdrawal

    @staticmethod
    def get_withdrawal(db: Session, withdrawal_id: UUID):

        withdrawal = (
            db.query(Withdrawal)
            .filter(Withdrawal.id == withdrawal_id)
            .first()
        )

        if not withdrawal:
            raise WithdrawalNotFoundException()

        return withdrawal

    @staticmethod
    def get_user_withdrawals(db: Session, user_id: UUID):

        return (
            db.query(Withdrawal)
            .filter(Withdrawal.user_id == user_id)
            .order_by(Withdrawal.created_at.desc())
            .all()
        )

    @staticmethod
    def update_status(
        db: Session,
        withdrawal_id: UUID,
        status: WithdrawalStatus,
    ):

        withdrawal = (
            db.query(Withdrawal)
            .filter(Withdrawal.id == withdrawal_id)
            .first()
        )

        if not withdrawal:
            raise ValueError("Withdrawal not found.")

        # Prevent duplicate processing
        if withdrawal.status != WithdrawalStatus.PENDING:
            raise WithdrawalAlreadyProcessedException()

        withdrawal.status = status

        # Refund wallet if failed or cancelled
        if status in [
            WithdrawalStatus.FAILED,
            WithdrawalStatus.CANCELLED,
        ]:
            user = (
                db.query(User)
                .filter(User.id == withdrawal.user_id)
                .first()
            )

            WalletService.credit_wallet(user, withdrawal.amount)

        db.commit()
        db.refresh(withdrawal)

        return withdrawal