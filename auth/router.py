from fastapi import APIRouter
from auth.login import login_router


auth_router = APIRouter()

auth_router.include_router(login_router)