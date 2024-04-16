from fastapi import FastAPI
from pymongo import MongoClient
from app.routes.api import router


def get_appliaction() -> FastAPI:
    application = FastAPI()
    application.include_router(router)

    return application

app = get_appliaction()

@app.get("/")
async def root():
    return {"Hello" : "FastAPI!"}