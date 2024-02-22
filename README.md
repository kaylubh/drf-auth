# LAB - Class 33

## Project: Authentication & Production Server

### Author: [Caleb Hemphill](https://github.com/kaylubh)

Extends [Django REST Framework & Docker](https://github.com/kaylubh/drf-api) and [Django REST Framework Permissions & Docker Postgresql](https://github.com/kaylubh/drf-api-permissions-postgres) projects to add API authentication. Deployed in a local Docker container with Postgresql.

## Setup

### Requirements - Run

1. Ensure Docker Desktop is installed and running

### Requirements - Develop / Test

1. Create and activate a virtual environment

    `python3 -m venv .venv`

    `source .venv/bin/activate` (Linux/Mac)

    `source .venv/Scripts/activate` (Windows)

1. Install packages

    `pip install -r requirements.txt`

## Run

1. Run `docker compose up` from root of project directory in order to interact with the API

1. ***In a separate terminal process, same directory*** Create a superuser: `docker compose exec web python manage.py createsuperuser`

    - Required to login to admin console and create users at `http://localhost:8000/admin/`
    - API permissions require an authenticated user in order to view/edit data

1. In a browser navigate to: `http://localhost:8000/api/v1/penguins/`

    - Adjust `localhost` as necessary to match your runtime configuration

1. Login to your superuser or other created user if necessary

1. In order to view resources individually, append the "id" to the path

    - Example: `http://localhost:8000/api/v1/penguins/1`

## Tests

From root of project directory run `python manage.py test`
