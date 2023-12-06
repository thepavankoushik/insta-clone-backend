from fastapi import FastAPI
from db import models
from db.database import engine
from routers.user import router as UserRouter


app = FastAPI()
app.include_router(UserRouter)

@app.get("/")
def root():
    return {"message": "Hello World"}

models.Base.metadata.create_all(bind=engine)


