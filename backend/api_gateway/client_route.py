
from fastapi import APIRouter

router = APIRouter()

# Routes utilisateur (placeholder)
@router.get("/users")
def list_users():
	return {"users": []}
