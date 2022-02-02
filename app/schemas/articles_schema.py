from pydantic import BaseModel

class ArticleSchema(BaseModel):
    id: int
    featured: bool
    title: str
    url: str
    imageUrl: str
    newsSite: str
    summary: str
    publishedAt: str
    launches: list
    events: list

    class Config:
        orm_mode = True