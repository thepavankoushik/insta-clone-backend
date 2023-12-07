from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm.session import Session
from db.database import get_db
from routers.schemas import CommentBase
from db import db_comment
from auth.oauth2 import get_current_user
from .schemas import UserAuth

router = APIRouter(
    prefix = '/comment',
    tags = ['comment']
)

@router.get("/all/{post_id}")
def get_all(post_id: int, db: Session = Depends(get_db)):
    return db_comment.get_all(db, post_id)

@router.post('/')
def create(request: CommentBase, db: Session = Depends(get_db)):
    return db_comment.create(db, request)