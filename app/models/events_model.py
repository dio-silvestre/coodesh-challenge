from sqlalchemy import Column, Integer, String, ForeignKey

from app.configs.database import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    provider = Column(String)
    article_id = Column(String, ForeignKey('articles.id'), nullable=False)
