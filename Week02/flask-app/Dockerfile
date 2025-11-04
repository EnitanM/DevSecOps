# syntax=docker/dockerfile:1
# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/go/dockerfile-reference/

# Want to help us make this template better? Share your feedback here: https://forms.gle/ybq9Krt8jtBL3iCk7

ARG PYTHON_VERSION=3.13.7
FROM python:${PYTHON_VERSION}-slim AS base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Create a non-privileged user that the app will run under.
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

# Set the working directory for the application.
WORKDIR /app

COPY requirements.txt .
COPY . .

RUN apt-get update && \
    apt-get install -y curl && \
    pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir -r requirements.txt &&\
    pip install pytest

# Expose configurable port
ENV APP_PORT=8082
ENV APP_MODULE=app:app
ENV GUNICORN_WORKERS=1
ENV GUNICORN_THREADS=2
EXPOSE ${APP_PORT}

CMD gunicorn --bind 0.0.0.0:${APP_PORT} ${APP_MODULE}