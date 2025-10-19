from fastapi import FastAPI
from routers import programming_language_service
# from database import create_table


app = FastAPI(title="W3Schools Clone API")

app.include_router(programming_language_service.router)


# @app.on_event("startup")
# async def on_startup():
#     await create_table()