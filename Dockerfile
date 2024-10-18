FROM python:3.10
LABEL maintainer="derepovskiy98@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y postgresql-client && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . .

RUN mkdir -p /files/media && \
    adduser --disabled-password --no-create-home my_user && \
    chown -R my_user /files/media && \
    chmod -R 755 /files/media

USER my_user
