# Flask Application

This is a Flask application that is Dockerized for ease of deployment and testing. It includes testing capabilities with `pytest` and `pytest-flask`.

## Features

- Flask web server with Docker support
- Environment configuration for development
- Testing setup using `pytest` and `pytest-flask`
- Docker Compose for managing app and test containers

## Requirements

The following packages are required for the project:

- `Flask==3.0.1`
- `pytest==8.3.3`
- `pytest-flask==1.3.0`

These dependencies are listed in the `requirements.txt` file.

## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/andrepbo/flask-app.git
cd flask-app
```

### Install Dependencies

To install the dependencies, you can use `pip` with the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Docker Setup

This project uses Docker and Docker Compose for running the application and the tests. Ensure Docker is installed on your system.

To build and run the application using Docker:

```bash
docker-compose up --build
```

The application will be accessible at `http://localhost:5001`.

### Running Tests

You can run the tests in a separate Docker container using the following command:

```bash
docker-compose run test
```

This will execute the tests located in `test_app.py`.

## Configuration

The environment variables are configured within the `docker-compose.yml` file. Important variables include:

- `FLASK_APP`: The entry point for the Flask application (`app.py`).
- `FLASK_RUN_HOST`: Host configuration for running the Flask app (`0.0.0.0`).
- `FLASK_ENV`: Environment mode (`development`).
- `FLASK_DEBUG`: Enables debug mode.

## File Overview

- `app.py`: The main Flask application file.
- `test_app.py`: The file containing tests using `pytest` and `pytest-flask`.
- `Dockerfile`: Docker instructions for setting up the application container.
- `docker-compose.yml`: Docker Compose configuration for running the application and test services.