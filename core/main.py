from fastapi import FastAPI
from src.routers import language_router


app = FastAPI(title="Online Programming Learning Platform")

app.include_router(language_router.router)