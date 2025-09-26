FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
WORKDIR .    # /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN

# CMD ["python3.11", "app/manage.py", "runserver", "0.0.0.0:8080" ]
CMD python carmarket/manage.py migrate \
    && python carmarket/manage.py runserver 0.0.0.0:8000

