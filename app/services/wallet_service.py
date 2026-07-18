from decimal import Decimal

from app.models.user import User
from app.exceptions.custom_exceptions import InsufficientBalanceException


class WalletService:

    @staticmethod
    def credit_wallet(user: User, amount: Decimal):
        user.wallet_balance += amount

    @staticmethod
    def debit_wallet(user: User, amount: Decimal):
        if user.wallet_balance < amount:
            raise InsufficientBalanceException()

        user.wallet_balance -= amount