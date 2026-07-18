from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.withdrawal import (
    WithdrawalCreate,
    WithdrawalResponse,
)
from app.core.enums import WithdrawalStatus
from app.services.withdrawal_service import WithdrawalService

router = APIRouter(
    prefix="/withdrawals",
    tags=["Withdrawals"]
)


@router.post(
    "/",
    response_model=WithdrawalResponse,
    summary="Create a Withdrawal"
)
def create_withdrawal(
    withdrawal_data: WithdrawalCreate,
    db: Session = Depends(get_db)
):
    return WithdrawalService.create_withdrawal(
        db,
        withdrawal_data
    )


@router.get(
    "/{withdrawal_id}",
    response_model=WithdrawalResponse,
    summary="Get Withdrawal by ID"
)
def get_withdrawal(
    withdrawal_id: UUID,
    db: Session = Depends(get_db)
):
    return WithdrawalService.get_withdrawal(
        db,
        withdrawal_id
    )


@router.get(
    "/user/{user_id}",
    response_model=list[WithdrawalResponse],
    summary="Get User Withdrawals"
)
def get_user_withdrawals(
    user_id: UUID,
    db: Session = Depends(get_db)
):
    return WithdrawalService.get_user_withdrawals(
        db,
        user_id
    )


@router.patch(
    "/{withdrawal_id}/status",
    response_model=WithdrawalResponse,
    summary="Update Withdrawal Status"
)
def update_withdrawal_status(
    withdrawal_id: UUID,
    status: WithdrawalStatus,
    db: Session = Depends(get_db)
):
    return WithdrawalService.update_status(
        db,
        withdrawal_id,
        status,
    )