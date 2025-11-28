
from fastapi import APIRouter

router = APIRouter()

@router.get("/admin")
def admin_root():
	return {"admin": True}
