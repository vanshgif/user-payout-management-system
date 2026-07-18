from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.payout_service import PayoutService

router = APIRouter(
    prefix="/payouts",
    tags=["Payouts"]
)


@router.post("/process-advance")
def process_advance_payouts(
    db: Session = Depends(get_db)
):
    sales = PayoutService.process_advance_payouts(db)

    return {
        "message": "Advance payouts processed successfully",
        "processed_sales": len(sales)
    }