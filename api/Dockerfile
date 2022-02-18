# base image
FROM python:3.8

# set environment variables
ENV PYTHONUNBUFFERED 1

# set directory
WORKDIR /app

# add application and install dependencies
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
COPY api supervisord.conf docker-entrypoint.sh ./

# expose port(s)
EXPOSE 8000

# entrypoint
RUN chmod a+x docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]
