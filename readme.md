# FastAPI Patient Medication Interview Assessment  

## Overview

This project is a part of an interview process, and it is FastAPI application designed to manage medication requests. The system is designed including automatic database migrations with Alembic, static type checking with `mypy`, code formatting with `black`, and linting with `flake8` (although due to the short time available, the highlighted problems have not been fixed).

## Assumptions

- The project is not production ready. For that reasons you will not find routes and other topics.
- Per assumptions, there is no authentication.
- you will test the app on an already populated database.

## Getting Started

### Prerequisites

- Docker
- Docker Compose
- an empty database to connect to the app (the docker compose will automatically create the tables)

### .ENV variables

you need to create a .env file and add the following variables:

- DRIVER_NAME=postgresql+psycopg
- DATABASE_HOSTNAME=postgres
- DATABASE_PORT=5432
- DATABASE_PASSWORD= [YOUR_DATABASE_PASSWORD]
- DATABASE_NAME= [YOUR_DATABASE_NAME]
- DATABASE_USERNAME= [YOUR_DATABASE_USERNAME]

### Running the Application

1. **Clone the Repository**

   ```sh
   git clone git@github.com:devsimone/Patient-Medication.git
   ```

2. **Start the Application**

   Use Docker Compose to build and start the application and its services (including the database):

   ```sh
   docker-compose up --build
   ```

   This command builds the Docker containers for the application and starts them. Alembic migrations are automatically applied, so your database schema will be up to date.


3. **Access the Application**

   Once the containers are running, you can access the FastAPI Swagger UI at:

   ```
   http://localhost:8000/docs
   ```

   This page allows you to test the API endpoints directly from your browser.

### Running Static Type Checking, Linting, and Formatting

To ensure code quality and consistency, this project uses `mypy` for static type checking, `flake8` for linting, and `black` for code formatting.

- **mypy**

  To run mypy for static type checking, use the following command:

  ```sh
  docker-compose run api mypy /app
  ```

  Replace `/app` with the path to your application code if different.

- **flake8**

  For linting with flake8, execute:

  ```sh
  docker-compose run api flake8 /app
  ```

- **black**

  To format your code with black, run:

  ```sh
  docker-compose run api black /app --check
  ```

  Remove `--check` to apply changes instead of just checking them.

An additional step will be to integrate the above checks with Pre-commit Hooks in GitHub or GitLab

### Testing

Create a test database in the following format [DB_NAME_test] and then, to run tests, execute the following command:

```sh
docker-compose run api pytest
```

This will run all the tests defined in `tests` directory.

If you are testing the endpoints locally, remember to change the ENV Variable:
- DATABASE_HOSTNAME

### Notes

Due to the short time available, the docker-compose for testing and linting does not work. However, you should be able to run and test the docker-compose manually.