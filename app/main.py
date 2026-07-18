from fastapi import FastAPI

from app.database import Base, engine

from app.routes.user_routes import router as user_router
from app.routes.sale_routes import router as sale_router
from app.routes.payout_routes import router as payout_router
# Import all models so SQLAlchemy registers them
from app.models import User, Sale, Payout, Withdrawal
from app.routes.withdrawal_routes import router as withdrawal_router

from app.exceptions.handlers import register_exception_handlers

from app.middleware.logging_middleware import log_requests
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User Payout Management System"
)
app.middleware("http")(log_requests)
register_exception_handlers(app)
app.include_router(user_router)
app.include_router(sale_router)
app.include_router(withdrawal_router)
app.include_router(payout_router)


@app.get("/")
def root():
    return {
        "message": "User Payout Management System API is running 🚀"
    }

