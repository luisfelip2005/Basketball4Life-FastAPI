# uvicorn main:server --reload --port 8000              
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.db import create_tables
from routes.route import router

# uvicorn main:app --reload

create_tables()

app = FastAPI()
app.include_router(router)

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(task)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)