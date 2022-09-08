# gutenberg-api
FastAPI Implementation of Project Gutenberg Library

## How to Run

Project comes with pre-configured  `docker-compose` file which can be run by the command:

`docker compose up --build`

Alternatively, one can run it with pgadmin also, by:

`docker compose --profile=pg-admin up`

The above command will setup all the required containers: fastapi, postgres, pgadmin(optional) and intialize the gutenberg dump data on its first run.

The api can be accessed via `localhost:8000/docs` along with swagger documentation.
