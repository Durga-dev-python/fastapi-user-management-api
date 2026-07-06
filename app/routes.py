from fastapi import APIRouter

router = APIRouter()

users = []

@router.post("/users")
def create_user(user: dict):
    users.append(user)
    return {"message": "User created", "user": user}

@router.get("/users")
def get_users():
    return users
