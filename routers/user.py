from fastapi import APIRouter
from .schemas import UserDisplay, UserBase
from fastapi import Depends
from sqlalchemy.orm.session import Session
from db.database import get_db
from db.db_user import  create_user as db_create_user

router = APIRouter(
    prefix='/user',
    tags=['user']
)

@router.post("/", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_create_user(db, request)

