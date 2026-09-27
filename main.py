from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models
import database
from auth import router as auth_router

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="abinash swain")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)

@app.get("/")
def home ():
    return {"hello": "god"}
