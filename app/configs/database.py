from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()


engine = create_engine(os.getenv("SQLALCHEMY_DATABASE_URL"))

Base = declarative_base()
