from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from db import auth_collection, user_collection
from security import hash_password, verify_password
from auth import create_access_token
from models import UserSignup

auth_router = APIRouter(prefix="/auth", tags=["Auth"])

@auth_router.post("/signup")
async def signup(user: UserSignup):
    hashed_pw = hash_password(user.password)
    result = await auth_collection.insert_one({
        "email": user.email,
        "password": hashed_pw,
        "role": user.role
    })
    auth_user_id = result.inserted_id

    await user_collection.insert_one({
    "owner_id": auth_user_id,
    "name": "",
    "age": 0
})
    return {"message": "User created"}


@auth_router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await auth_collection.find_one({"email": form_data.username})

    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({
        "sub": user["email"],
        "role": user["role"],
        "user_id": str(user["_id"])
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }
