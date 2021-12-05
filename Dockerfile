# base image
FROM python:3.8

# set environment variables
ENV PYTHONUNBUFFERED 1

# set directory
WORKDIR /app

# install dependencies
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv
RUN pipenv install --system --deploy

# add application
COPY PokemonAPI ./
EXPOSE 8000
