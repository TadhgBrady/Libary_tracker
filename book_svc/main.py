from fastapi import FastAPI
from app.interfaces.api.routes.books import router

app = FastAPI()

app.include_router(router,prefix="/books")