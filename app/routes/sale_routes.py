from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.sale import SaleCreate, SaleResponse
from app.services.sale_service import SaleService

from uuid import UUID

from app.schemas.sale import SaleStatusUpdate

router = APIRouter(
    prefix="/sales",
    tags=["Sales"]
)


@router.post(
    "",
    response_model=SaleResponse
)
def create_sale(
    sale: SaleCreate,
    db: Session = Depends(get_db)
):

    return SaleService.create_sale(db, sale)

@router.patch("/{sale_id}/status")
def update_sale_status(
    
    sale_id: UUID,
    request: SaleStatusUpdate,
    db: Session = Depends(get_db)
):
    
    
    
    

    return SaleService.update_sale_status(
        db,
        sale_id,
        request.status
    )