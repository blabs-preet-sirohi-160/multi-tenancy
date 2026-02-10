from pydantic import BaseModel
from typing import Optional

# Auth model (signup only)
class UserSignup(BaseModel):
    email: str
    password: str
    role: Optional[str] = "user"


# Domain model (business data)
class UserCreate(BaseModel):
    name: str
    age: int
    

# Update model
class UpdateUser(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
