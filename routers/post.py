from fastapi import APIRouter, Depends, status, UploadFile, File
from sqlalchemy.orm.session import Session
from db.database import get_db
from fastapi.exceptions import HTTPException
from routers.schemas import PostBase, UserAuth
from db import db_post
from .schemas import PostDisplay
import random
import string
from auth.oauth2 import get_current_user

router = APIRouter(
    prefix = '/post',
    tags = ['post']
)

image_url_types = ['absolute', 'relative']

@router.post("/", response_model=PostDisplay)
def create(request: PostBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    if request.image_url_type not in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
                            detail="Invalid image_url_type")
    return db_post.create(db, request)
    
@router.get("/all", response_model=list[PostDisplay])
def get_all(db: Session = Depends(get_db)):
    return db_post.get_all(db)

@router.post("/image")
def upload_image(image: UploadFile=File(...), current_user: UserAuth = Depends(get_current_user)):
    letters = string.ascii_letters
    rand_str = ''.join(random.choice(letters) for i in range(10))
    new = f'_{rand_str}.'
    filename = new.join(image.filename.rsplit('.', 1))
    path = f'./images/{filename}'
    with open(path, 'wb') as f:
        f.write(image.file.read())
    return {'filename': path}
