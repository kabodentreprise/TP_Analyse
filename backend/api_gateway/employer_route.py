
from fastapi import APIRouter

router = APIRouter()

@router.get("/employers")
def list_employers():
	return {"employers": []}
