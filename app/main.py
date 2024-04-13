from fastapi import FastAPI
from pymongo import MongoClient


def get_appliaction() -> FastAPI:
    application = FastAPI()
    
    return application

app = get_appliaction()

@app.get("/")
async def root():
    return {"Hello" : "FastAPI!"}