from fastapi import APIRouter, Depends
from bson import ObjectId
from db import user_collection
from models import UserCreate, UpdateUser
from dependency import get_current_user, get_current_admin

user_router = APIRouter(prefix="/users", tags=["Users"])

@user_router.post("")
async def create_user(
    user: UserCreate,
    admin=Depends(get_current_admin)
):
    result = await user_collection.insert_one({
        "name": user.name,
        "age": user.age
    })
    return {"id": str(result.inserted_id)}



@user_router.get("")
async def get_users(current_user=Depends(get_current_user)):
    users = []
    async for u in user_collection.find():
        u["_id"] = str(u["_id"])
        users.append(u)
    return users


@user_router.put("/{user_id}")
async def update_user(
    user_id: str,
    user: UpdateUser,
    admin=Depends(get_current_admin)
):
    await user_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": user.dict(exclude_none=True)}
    )
    return {"message": "Updated"}



@user_router.delete("/{user_id}")
async def delete_user(
    user_id: str,
    admin=Depends(get_current_admin)
):
    await user_collection.delete_one({"_id": ObjectId(user_id)})
    return {"message": "Deleted"}
