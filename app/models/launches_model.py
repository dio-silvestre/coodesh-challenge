from sqlalchemy import Column, Integer, String, ForeignKey

from app.configs.database import Base


class Launch(Base):
    __tablename__ = "launches"

    id = Column(Integer, primary_key=True)
    provider = Column(String)
    article_id = Column(String, ForeignKey('articles.id'), nullable=False)
