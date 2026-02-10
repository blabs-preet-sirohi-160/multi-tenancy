# this is a fast api application
from fastapi import FastAPI
from routers.auth_routes import auth_router
from routers.user_routes import user_router




app = FastAPI()

@app.get("/") 
async def read_root():
    return {"status": "public", "message": "test ci!"}


app.include_router(auth_router)
app.include_router(user_router)

# this is enough in main file
# lets test ci