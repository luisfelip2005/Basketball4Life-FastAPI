from pydantic import BaseModel
from datetime import datetime

class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    password: str
    height: str
    weight: str
    created_at: datetime