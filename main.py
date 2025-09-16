from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from auth.router import auth_router
from portfolio.router import portfolio_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(auth_router)
app.include_router(portfolio_router)