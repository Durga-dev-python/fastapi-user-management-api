from fastapi import FastAPI
from app.routes import router
from app.database import Base, engine

app = FastAPI(title="User Management API")

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "API is running"}

app.include_router(router)
