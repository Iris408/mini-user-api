# Setup Guide

This document explains how to run Secure User Management API locally.

## Installation

Clone the repository:

```bash
git clone https://github.com/Iris408/secure-user-management-api
cd secure-user-management-api
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a local `.env` file in the project root.

Example variables:

```env
DATABASE_URL=
SECRET_KEY=
ALGORITHM=
ACCESS_TOKEN_EXPIRE_MINUTES=
```

Never commit real `.env` files or production secrets to GitHub.

Recommended `.gitignore` entries:

```txt
.env
.venv/
__pycache__/
.pytest_cache/
*.pyc
```

## Docker Database Connection

When running with Docker Compose, the backend connects to PostgreSQL using the Docker service name `db`.

```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/secure_user_api_db
```

Start the app with Docker Compose:

```bash
docker compose up --build
```

Local URLs:

```text
http://127.0.0.1:8002
http://127.0.0.1:8002/health
http://127.0.0.1:8002/ready
http://127.0.0.1:8002/docs
```

Restart containers:

```bash
docker compose down
docker compose up --build
```

If your system uses the older Docker Compose command:

```bash
docker-compose up --build
```

## Manual Local Database Connection

If Docker is not available, the project can be run manually.

When running the backend directly with Uvicorn, use `localhost` instead of `db`:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/secure_user_management_api_db
```

Make sure PostgreSQL is running locally and that `secure_user_management_api_db` has already been created.

Run the FastAPI server:

```bash
uvicorn app.main:app --reload --port 8002
```

## Running Tests

This project uses pytest for backend testing.

Run tests with Docker Compose:

```bash
docker compose up -d --build
docker compose exec api pytest
```

Current basic test coverage includes:

- Root endpoint
- Health check endpoint
- Database readiness endpoint
- OpenAPI schema availability