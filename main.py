from fastapi import FastAPI
from db import models
from db.database import engine
from routers.user import router as UserRouter
from routers.post import router as PostRouter
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(UserRouter)
app.include_router(PostRouter)

@app.get("/")
def root():
    return {"message": "Hello World"}

models.Base.metadata.create_all(bind=engine)

app.mount('/images', StaticFiles(directory='images'), name='images')



