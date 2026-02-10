# this is a fast api application
from fastapi import FastAPI
from routers.auth_routes import auth_router
from routers.user_routes import user_router




app = FastAPI()

@app.get("/") 
async def read_root():
    return {"status": "public"}


app.include_router(auth_router)
app.include_router(user_router)

# this is enough in main file























# @app.post("/users")
# async def create_user(user: UserCreate,admin=Depends(get_current_admin)):
#     name = user.name
#     age = user.age
#     user_dict = {"name": name, "age": age}
#     result = await user_collection.insert_one(user_dict)
#     return {"id": str(result.inserted_id), "name": name, "age": age}


# @app.get("/allusers")
# async def all_users(admin=Depends(get_current_admin)):
#     users = []
#     cursor = user_collection.find({})
#     async for document in cursor:
#         document["_id"] = str(document["_id"])  # Convert ObjectId to string
#         users.append(document)
#     return users



# @app.put("/users/{user_id}")
# async def update_user(user_id: str, user: UpdateUser,admin=Depends(get_current_admin)):
#     update_data = {}
#     if user.name is not None:
#         update_data["name"] = user.name
#     if user.age is not None:
#         update_data["age"] = user.age

#     if update_data:
#         result = await user_collection.update_one(
#             {"_id": ObjectId(user_id)},
#             {"$set": update_data}
#         )
#         if result.modified_count == 1:
#             return {"status": "success", "message": "User updated successfully"}
#     return {"status": "failure", "message": "No fields to update or user not found"}


# @app.delete("/users/{user_id}")
# async def delete_user(user_id: str,admin=Depends(get_current_admin)):
#     if True:
#         result = await user_collection.delete_one({"_id": ObjectId(user_id)})
#         if result.deleted_count == 1:
#             return {"status": "success", "message": "User deleted successfully"}
#     return {"status": "failure", "message": "User not found"}


# @app.post("/signup")
# async def signup(user: UserSignup):
#     hashed_pw = hash_password(user.password)

#     user_dict = {
#         "email": user.email,
#         "password": hashed_pw,
#         "role": user.role
#     }

#     await auth_collection.insert_one(user_dict)
#     return {"message": "User created"}
# from fastapi.security import OAuth2PasswordRequestForm



# @app.post("/login")
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = await auth_collection.find_one({"email": form_data.username})

#     if not user:
#         raise HTTPException(status_code=401, detail="Invalid credentials")

#     if not verify_password(form_data.password, user["password"]):
#         raise HTTPException(status_code=401, detail="Invalid credentials")

#     token = create_access_token({"sub": user["email"], "role": user["role"]})

#     return {
#         "access_token": token,
#         "token_type": "bearer"
#     }



# @app.get("/userssecured")
# async def get_users(current_user=Depends(get_current_user)):
#     users = []
#     async for user in user_collection.find():
#         user["_id"] = str(user["_id"])
#         users.append(user)
#     return users