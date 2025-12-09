from database.db import Session
from fastapi import APIRouter, Response, Path, HTTPException, status
from models.models import User
from schemas.schema import UserSchema

user = APIRouter(prefix="/api")
session = Session()

@user.post("/add")
async def createuser(data: UserSchema):
    if not data.name:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="user name is required")
    user = User(data.name)
    session.add(user)
    try:
        session.commit()
    except:
        session.rollback()
    session.close()
    return Response(content="user created successfully!", status_code=status.HTTP_201_CREATED)

@user.get("/all")
async def getAllusers():
    return session.query(User).all()

@user.put('/update/{id}')
async def updateuser(id: int, data: UserSchema):
    if not data.name:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="user name is required")
    session.query(User).filter(User.id == id).update({'name': data.name})
    try:
        session.commit()
    except:
        session.rollback()
    session.close()
    return Response(content="user updated successfully", status_code=status.HTTP_200_OK)

@user.delete('/delete/{id}')
async def deleteuser(id: int):
    session.query(User).filter(User.id == id).delete()
    session.commit()
    session.close()
    return Response(content="user deleted successfully", status_code=status.HTTP_200_OK)