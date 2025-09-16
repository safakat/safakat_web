from fastapi import APIRouter,Request
from fastapi.responses import HTMLResponse
from config import templates

features_router = APIRouter()

@features_router.get('/features',response_class=HTMLResponse)
async def features(request:Request):
    return templates.TemplateResponse(
        request=request, name="portfolio/features.html"
    )