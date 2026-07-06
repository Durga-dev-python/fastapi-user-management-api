from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="User Management API")

@app.get("/")
def home():
    return {"message": "FastAPI is running successfully"}

app.include_router(router)
