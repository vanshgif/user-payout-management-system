from decimal import Decimal

from app.models.user import User


class WalletService:

    @staticmethod
    def credit_wallet(user: User, amount: Decimal):
        user.wallet_balance += amount

    @staticmethod
    def debit_wallet(user: User, amount: Decimal):
        if user.wallet_balance < amount:
            raise ValueError("Insufficient wallet balance")

        user.wallet_balance -= amount