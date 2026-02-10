from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://localhost:27017"

client = AsyncIOMotorClient(MONGO_URL)
db = client["test_db"]

user_collection = db["users"]
auth_collection = db["auth_users"]
