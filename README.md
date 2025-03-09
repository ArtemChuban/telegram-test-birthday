# Birthday Tracker Telegram Mini App

## Description
Frontend uses VueJS as the framework and Pinia to manage the state.
The server part uses unicorn, which runs FastAPI app, and the turtle orm is used as an orm.
Postgresql is used as the database.
Bot uses long-polling, since the webhook can only be configured using a server with tls server (obviously, the real application will use a webhook).

## Start up

Requirements:
- docker
- docker-compose

Copy `.env` file
```sh
cp .env.example .env
```

Build and up containers
```sh
docker-compose up -d --build
```

## Env variables in `.env`
- `TELEGRAM_BOT_TOKEN` - token fron @BotFather
- `POSTGRES_HOST` - in docker just leave `postgres` (container name of database)
- `POSTGRES_PORT` - change if port of database changes
- `POSTGRES_USER`, `POSTGRES_PASSWORD` - postgres credentials
- `POSTGRES_DB` - name of database in postgres
- `WEB_APP_URL` - copy from @BotFather after creating web app
- `API_URL` - FastAPI backend url
- `USE_TEST_SERVER` - leave `true` if bot works in test Telegram environment, `false` otherwise (production environment)
