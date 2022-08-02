from fastapi import FastAPI, Depends
# import models, schemas
# from pydantic import BaseModel
# # from sqlalchemy.orm import Session
# # import sqlalchemy
# from sqlalchemy import create_engine
# from sqlalchemy.orm import Session
# from database import SessionLocal
# from sqlalchemy import Session
import models
from config import engine
models.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

# @app.post("/create-influencer")
# def influencerCreate(influencer:schemas.InfluencerCreate, db:SessionLocal):
#     return "Hello"
#     pass 