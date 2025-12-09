from database.db import Session
from fastapi import APIRouter, Response, Path, HTTPException, status
from models.models import User
from schemas.user import UserSchema

user = APIRouter(prefix="/user")
session = Session()

@user.post("/create-user")
async def createUser(data: UserSchema):
    user = User(
        name=data.name, 
        password=data.password,
        email = data.email,
        height = data.height,
        weight = data.weight
    )
    session.add(user)
    session.commit()
    session.close()
    
    return Response(content="User created", status_code=status.HTTP_201_CREATED)
