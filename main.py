from fastapi import FastAPI
from db import models
from db.database import engine
from routers.user import router as UserRouter
from routers.post import router as PostRouter
from fastapi.staticfiles import StaticFiles
from auth.authentication import router as AuthRouter
from routers.comment import router as CommentRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(UserRouter)
app.include_router(PostRouter)
app.include_router(AuthRouter)
app.include_router(CommentRouter)



@app.get("/")
def root():
    return {"message": "Hello World"}

origins = [
    'http://localhost:3000'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


models.Base.metadata.create_all(bind=engine)

app.mount('/images', StaticFiles(directory='images'), name='images')



