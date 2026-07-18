class UserNotFoundException(Exception):
    pass


class SaleNotFoundException(Exception):
    pass


class PayoutNotFoundException(Exception):
    pass


class WithdrawalNotFoundException(Exception):
    pass


class InsufficientBalanceException(Exception):
    pass


class WithdrawalCooldownException(Exception):
    pass


class WithdrawalAlreadyProcessedException(Exception):
    pass


class InvalidSaleStatusException(Exception):
    pass