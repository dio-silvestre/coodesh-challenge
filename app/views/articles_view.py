from fastapi import APIRouter, HTTPException, status
import requests
from app.models.articles_model import Article
from app.schemas.articles_schema import ArticleSchema
from fastapi_sqlalchemy import db


router = APIRouter()

@router.get("/", status_code=status.HTTP_200_OK)
def message():
    return "Back-end Challenge 2021 🏅 - Space Flight News"


@router.get("/articles", status_code=status.HTTP_200_OK)
def get_articles(page: int = 1, articles_per_page: int = 10):
    articles = requests.get("https://api.spaceflightnewsapi.net/v3/articles")
    start = (page - 1) * articles_per_page
    end = start + articles_per_page

    return articles.json()[start:end]


@router.get("/articles/{article_id}", status_code=status.HTTP_200_OK)
def get_article_by_id(article_id):
    found_article = requests.get(f"https://api.spaceflightnewsapi.net/v3/articles/{article_id}")

    return found_article.json()


@router.post("/articles", status_code=status.HTTP_201_CREATED)
async def create_articles(article: ArticleSchema):
    
    new_article = Article(
        featured = article.featured,
        title = article.title,
        url = article.url,
        imageUrl = article.imageUrl,
        newsSite = article.newsSite,
        summary = article.summary,
        publishedAt = article.publishedAt
    )

    found_article = db.query(Article).filter(Article.title == new_article.title).first()

    if found_article is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Article already exists")


@router.put("/articles/{article_id}")
def update_article(article_id):
    article = db.query(Article).filter(Article.id == article_id).first()

    db.commit()

    return article


@router.delete("/articles/{article_id}", status_code=status.HTTP_200_OK)
def delete_article(article_id):
    article = db.query(Article).filter(Article.id == article_id).first()
    
    if article is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not found")

    db.delete(article)
    db.commit()

    return article
