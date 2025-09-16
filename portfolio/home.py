from fastapi import APIRouter,Request
from fastapi.responses import HTMLResponse
from config import templates

home_router = APIRouter()

@home_router.get('/',response_class=HTMLResponse)
async def home(request:Request):
    return templates.TemplateResponse(
        request=request, name="portfolio/home.html"
    )