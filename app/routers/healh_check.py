from fastapi import APIRouter

router_health_check = APIRouter()

@router_health_check.get("/health")
async def health_check():
    return {"message": "Routers are working."}

