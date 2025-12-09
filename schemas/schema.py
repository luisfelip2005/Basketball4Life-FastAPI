from pydantic import BaseModel
from datetime import datetime

class UserSchema(BaseModel):
    id: int
    name: str
    created_at: datetime