# Reservamos Challenge

A challenge project to compare future forecasts for certain destinations.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

License: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Run locally with Docker

Create a `.env` file with the following API Key (OpenWeather API Key with subscription for one-call requests):

    OPENWEATHER_API_KEY="<your-api-key>"

Build the project with docker:

    $ docker compose -f local.yml build

Then, open a terminal at the project root and run the following for local development:

    $ docker compose -f local.yml up

See detailed [cookiecutter-django Docker documentation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html).

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy reservamos_challenge

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).

## Tasks

#### Priority
- [x] Read and understand the requirement
- [x] Configure a new Django Cookiecutter project
- [x] Test OpenWeatherMap API endpoint
- [x] Test Reservamos cities API endpoint
- [x] Create GET endpoint view
- [x] Create business logic for endpoint
- [x] Refactor and reduce response time
- [x] Test endpoint from an API Client
- [x] Agregar procesamiento paralelo
- [x] Agregar caché

#### Extra
- [ ] Create a behavior test to verify requirement is working as expected
- [ ] Launch project to the cloud
- [ ] Create a basic front-end client
