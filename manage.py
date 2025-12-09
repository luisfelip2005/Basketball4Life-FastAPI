import os

# -------------------------------------------------------------------------------------------------
with open("requirements.txt", "w") as file:
    file.write("""h11
mysql-connector-python
PyJWT
PyMySQL
pyOpenSSL
pyparsing
PySocks
SQLAlchemy
sqlparse
trio-websocket
virtualenv
whitenoise
uvicorn
fastapi
gunicorn""")

os.system("pip install -r requirements.txt --break-system-packages")

# -------------------------------------------------------------------------------------------------

paste = "src"
file = "app.py"
path = os.path.join(paste, file)

# Cria a pasta se ela não existir
os.makedirs(paste, exist_ok=True)

with open(path, "w") as file:
    file.write("""from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# uvicorn main:app --reload

app = FastAPI()

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(task)
               """)
    
# -------------------------------------------------------------------------------------------------

with open("server.py", "w") as file:
    file.write("""# uvicorn main:server --reload --port 8000              

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.app:app", host="0.0.0.0", port=8000, reload=True)""")

# -------------------------------------------------------------------------------------------------

paste = "src/"
file = ".env"
path = os.path.join(paste, file)

# Cria a pasta se ela não existir
os.makedirs(paste, exist_ok=True)

with open(path, "w") as file:
    file.write("")

# -------------------------------------------------------------------------------------------------

with open("Dockerfile", "w") as file:
    file.write("""FROM python:3.9-slim-buster

COPY ./config ./config 
COPY ./models ./models
COPY ./routes ./routes
COPY ./schemas ./schemas

# COPY ./database.sqlite3 ./database.sqlite3
COPY ./main.py ./main.py
COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]

# sudo docker build -t fastapi .
# sudo docker run -p 3000:5000 fastapi
# http://localhost:3000/docs""")

# -------------------------------------------------------------------------------------------------

with open(".gitignore", "w") as file:
    file.write("""# Python-generated files
__pycache__/
*.py[oc]
build/
dist/
wheels/
*.egg-info

# Virtual environments
.venv
.env               
""")

# -------------------------------------------------------------------------------------------------

paste = "src/routes"
file = "route.py"
path = os.path.join(paste, file)

# Cria a pasta se ela não existir
os.makedirs(paste, exist_ok=True)

with open(path, "w") as file:
    file.write("""from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel
from sqlalchemy.orm import Session

from ..database.models import get_db
import json
from datetime import datetime

router = APIRouter()""")


# -------------------------------------------------------------------------------------------------

paste = "src/database"
file = "db.py"
path = os.path.join(paste, file)

# Cria a pasta se ela não existir
os.makedirs(paste, exist_ok=True)

with open(path, "w") as file:
    file.write("""from sqlalchemy.orm import Session
from . import models

""")

# -------------------------------------------------------------------------------------------------

paste = "src/database"
file = "models.py"
path = os.path.join(paste, file)

# Cria a pasta se ela não existir
os.makedirs(paste, exist_ok=True)

with open(path, "w") as file:
    file.write("""from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

engine = create_engine('sqlite:///database.db', echo=True)
Base = declarative_base()


# Create your tables here
class Example(Base):
    __tablename__ = 'example'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    


Base.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()""")