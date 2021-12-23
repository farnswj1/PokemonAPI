# Pokemon API
This is an API that provides data on Pokemon.

## Setup
The project uses the following:
- Python 3.8
- Django 3.2.8
- MySQL 8
- Redis 5
- Nginx 1.21
- Docker
- Docker Compose

For additional information on project specifications, see the ```Pipfile```.

### Environment
In the ```api/``` directory, create a ```.env``` file
that contains the following environment variables:
```
SECRET_KEY=[somerandomstring]

DEBUG=False
ALLOWED_HOSTS=*

DB_ENGINE=django.db.backends.mysql
DB_NAME=PokemonAPI
DB_HOST=mysql
DB_USER=root
DB_PASSWORD=password
DB_PORT=3306

REDIS_URL=redis://redis:6379/1
```
The database variables can be changed as desired. However, make sure to update
the environment variables in ```docker-compose.yml``` as well.

## Building
The project uses Docker. Ensure Docker and Docker Compose are installed before continuing.

To build, run ```docker-compose build```

## Running
To run the web API, run ```docker-compose up -d```, then 
go to http://localhost/api/pokemon/ using your web browser.

## Populating the Database
This project provides data to use for the project.
Populating the database should only be done once to avoid duplicate data. 
To do so, run ```docker exec -it backend python manage.py loaddata data.json```.

To create a staff user, run ```docker exec -it backend python manage.py createsuperuser```
and fill out the fields in the prompt.

## Issues
While this project is intended to be used as an API, it can be 
used to visually see the data using Django Rest Framework's templates.
However, there are several issues with this:
  1. The static files are currently not being served.
  2. The URLs in the Django Rest Framework pages may not work.
