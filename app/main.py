from fastapi import FastAPI
from app.views.articles_view import router
from app.scripts.populate_db import populate_db
from fastapi_sqlalchemy import DBSessionMiddleware, db
import os


# populate_db()

app = FastAPI()

app.include_router(router)
