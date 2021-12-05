# Pokemon API
This is an API that provides data on Pokemon.

## Setup
The project uses the following:
- Python 3.8
- Django 3.2.8
- MySQL 8
- Docker

For additional information on project specifications, see the ```Pipfile```.

### Environment
In the root directory, create a ```.env``` file 
that contains the following environment variables:
```
SECRET_KEY=[somerandomstring]

DB_ENGINE=django.db.backends.mysql
DB_NAME=PokemonAPI
DB_HOST=mysql
DB_USER=root
DB_PASSWORD=password
DB_PORT=3306
```
The database variables can be changed is desired. However, make sure to update 
the environment variables in ```docker-compose.yml``` as well.

## Building
The project uses Docker. Ensure Docker and Docker Compose are installed before continuing.

To build, run ```docker-compose build```

## Running
To run the web API, run ```docker-compose up -d```, then 
go to http://localhost:8000/pokemon/ using your web browser.
