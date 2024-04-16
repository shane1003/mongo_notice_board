from fastapi import APIRouter

from bson import ObjectId
from app.models.schemas.user import get_one_user
from app.config.config import collection_account

router = APIRouter()

@router.get("/{id}")
async def get_account_by_id(id: str):
    account_Info = get_one_user(collection_account.find_one({"_id" : ObjectId(id)}))
    return account_Info