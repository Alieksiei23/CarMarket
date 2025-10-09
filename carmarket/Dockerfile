FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .


CMD python manage.py migrate \
    && gunicorn --bind 0.0.0.0:8000 carmarket.wsgi


