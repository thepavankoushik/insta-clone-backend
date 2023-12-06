from fastapi import APIRouter, Depends, status
from sqlalchemy.orm.session import Session
from db.database import get_db
from fastapi.exceptions import HTTPException
from routers.schemas import PostBase
from db import db_post
from .schemas import PostDisplay

router = APIRouter(
    prefix = '/post',
    tags = ['post']
)

image_url_types = ['absolute', 'relative']

@router.post("/", response_model=PostDisplay)
def create(request: PostBase, db: Session = Depends(get_db)):
    if request.image_url_type not in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
                            detail="Invalid image_url_type")
    return db_post.create(db, request)
    