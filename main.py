from fastapi import FastAPI
from routes import users, posts
import models
from database import engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(posts.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI by Fajeri Innovate"}
