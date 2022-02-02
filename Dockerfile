FROM python:3.9

WORKDIR /app

COPY . .

EXPOSE 8000

RUN pip install --upgrade pip && pip install -r ./requirements.txt && alembic revision --autogenerate -m "New Migration"

CMD alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000