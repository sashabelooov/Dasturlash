from fastapi import FastAPI
from routers import languages_router
# from database import create_table


app = FastAPI(title="W3Schools Clone API")

app.include_router(languages_router.router)


# @app.on_event("startup")
# async def on_startup():
#     await create_table()