from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions.custom_exceptions import *


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(UserNotFoundException)
    async def user_not_found(request: Request, exc: UserNotFoundException):
        return JSONResponse(
            status_code=404,
            content={"detail": "User not found."}
        )

    @app.exception_handler(SaleNotFoundException)
    async def sale_not_found(request: Request, exc: SaleNotFoundException):
        return JSONResponse(
            status_code=404,
            content={"detail": "Sale not found."}
        )

    @app.exception_handler(PayoutNotFoundException)
    async def payout_not_found(request: Request, exc: PayoutNotFoundException):
        return JSONResponse(
            status_code=404,
            content={"detail": "Payout not found."}
        )

    @app.exception_handler(WithdrawalNotFoundException)
    async def withdrawal_not_found(request: Request, exc: WithdrawalNotFoundException):
        return JSONResponse(
            status_code=404,
            content={"detail": "Withdrawal not found."}
        )

    @app.exception_handler(InsufficientBalanceException)
    async def insufficient_balance(request: Request, exc: InsufficientBalanceException):
        return JSONResponse(
            status_code=400,
            content={"detail": "Insufficient wallet balance."}
        )

    @app.exception_handler(WithdrawalCooldownException)
    async def cooldown(request: Request, exc: WithdrawalCooldownException):
        return JSONResponse(
            status_code=400,
            content={"detail": str(exc)}
        )

    @app.exception_handler(WithdrawalAlreadyProcessedException)
    async def processed(request: Request, exc: WithdrawalAlreadyProcessedException):
        return JSONResponse(
            status_code=400,
            content={"detail": "Withdrawal already processed."}
        )

    @app.exception_handler(InvalidSaleStatusException)
    async def invalid_status(request: Request, exc: InvalidSaleStatusException):
        return JSONResponse(
            status_code=400,
            content={"detail": str(exc)}
        )