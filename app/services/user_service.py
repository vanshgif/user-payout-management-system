from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate


class UserService:

    @staticmethod
    def create_user(db: Session, user_data: UserCreate):

        user = User(
            username=user_data.username,
            email=user_data.email
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    @staticmethod
    def get_user(db: Session, user_id):

        return db.query(User).filter(User.id == user_id).first()