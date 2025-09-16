from fastapi import APIRouter,Request
from fastapi.responses import HTMLResponse
from config import templates

login_router = APIRouter()

@login_router.get('/login',response_class=HTMLResponse)
async def login(request:Request):
    return templates.TemplateResponse(
        request=request, name="auth/login.html"
    )
