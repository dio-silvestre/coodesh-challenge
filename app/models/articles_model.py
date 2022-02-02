from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.configs.database import Base
from app.models.launches_model import Launch
from app.models.events_model import Event


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    featured = Column(Boolean, default=False)
    title = Column(String, nullable=False)
    url = Column(String, nullable=False)
    imageUrl = Column(String, nullable=False)
    newsSite = Column(String, nullable=False)
    summary = Column(String)
    publishedAt = Column(String, nullable=False)

    launches = relationship(Launch, backref="article")
    events = relationship(Event, backref="event")
