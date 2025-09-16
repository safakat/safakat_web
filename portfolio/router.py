from fastapi import APIRouter
from portfolio.home import home_router
from portfolio.features import features_router

portfolio_router = APIRouter()

portfolio_router.include_router(home_router)
portfolio_router.include_router(features_router)