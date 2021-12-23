# base image
FROM python:3.8

# set environment variables
ENV PYTHONUNBUFFERED 1

# set directory
WORKDIR /app

# add application and install dependencies
COPY Pipfile Pipfile.lock api ./
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

# expose port(s)
EXPOSE 8000
