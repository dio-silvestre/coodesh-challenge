import json, urllib.request
from app.models.articles_model import Article
from fastapi_sqlalchemy import db
import schedule
import time


def populate_db():

    url = "https://api.spaceflightnewsapi.net/v3/articles"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())


    for apidata in data:
        apidata: Article = Article(
            id = apidata['id'],
            featured = apidata['featured'],
            title = apidata['title'],
            url = apidata['url'],
            imageUrl = apidata['imageUrl'],
            newsSite = apidata['newsSite'],
            summary = apidata['summary'],
            publishedAt = apidata['publishedAt'],
            launches = apidata['launches'],
            events = apidata['events']
        )

        article = db.session.query(Article).filter(Article.id == apidata['id']).first()

        if article is None:
            db.add(apidata)
            db.commit()


schedule.every().day.at('09:00').do(populate_db)

while True:
    schedule.run_pending()
    time.sleep(1)