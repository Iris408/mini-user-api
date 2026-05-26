# Mini User API / ミニユーザーAPI

Mini User API is a backend CRUD application built with FastAPI, PostgreSQL, and SQLAlchemy.
 
## Mini User APIは、FastAPI、PostgreSQL、およびSQLAlchemyを使用して構築されたバックエンドCRUDアプリケーションです。

---

The project allows users to:

- Create users
- Read users
- Update users
- Delete users

The application uses persistent PostgreSQL database storage instead of temporary in-memory storage.

---

## Tech Stack / 技術スタック

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Uvicorn
- Docker
- Docker Compose
- JWT Authentication
- bcrypt password hashing
- Git/GitHub

---

## Features / 機能

- RESTful CRUD API
- PostgreSQL database integration
- SQLAlchemy ORM
- Dependency injection
- Modular backend architecture
- JSON request validation
- Swagger API documentation
- Password hashing with bcrypt
- JWT access token generation
- OAuth2 token route for Swagger authorization
- Protected user profile route
- Dockerized FastAPI and PostgreSQL setup

---

## Authentication / 認証

This project includes basic JWT authentication.

Authentication features include:

- Password hashing before storing user passwords
- Login route for username/password validation
- JWT access token generation
- OAuth2 `/token` route for Swagger authorization
- Protected `/profile` route requiring a valid token

---

## Project Structure / プロジェクト構成

```text
app/
├── routes/
│   └── user_routes.py
├── models/
│   └── user_model.py
├── services/
├── database.py
└── main.py
```

---

## Installation / インストール

• Clone Respository

```bash
git clone https://github.com/Iris408/mini-user-api
```

• Move into project folder
```bash
cd mini-user-api
```

• Install dependencies
```bash
pip install -r requirements.txt
```
 
• Start PostgreSQL
```bash
psql postgres
```
```SQL
CREATE DATABASE mini_user_api_db;
```

• Exit PostgreSQL:
```SQL
\q
```
• Run FastAPI server
```bash
uvicorn app.main:app --reload --port 8002
```
---

## Run with Docker

```bash
docker compose up --build
```

• Open Swagger UI
```text
http://127.0.0.1:8002/docs
```

```text
If `docker compose` does not work on someone’s machine, they can try:
```

```bash
docker-compose up --build
```

---
 
## API Endpoints | APIエンドポイント

| Method | Endpoint | Description |
|---|---|---|
| POST | `/users` | Create a new user |
| POST | `/login` | Login user with JSON request |
| POST | `/token` | OAuth2 token login for Swagger authorization |
| GET | `/profile` | Get protected user profile |
| GET | `/users` | Get all users |
| GET | `/users/{user_id}` | Get one user by ID |
| PUT | `/users/{user_id}` | Update a user |
| DELETE | `/users/{user_id}` | Delete a user |

--- 

## Current Status

- Full PostgreSQL-backed CRUD functionality
- SQLAlchemy database models
- FastAPI dependency injection
- Persistent database storage
- Password hashing with bcrypt
- JWT authentication
- OAuth2 Swagger authorization support
- Protected `/profile` route
- Docker support for FastAPI and PostgreSQL
- Swagger API testing via `/docs`

---

## Future Improvements

- AWS deployment
- Frontend integration
- CI/CD pipelines
- Automated testing
- Improved role-based access control
- Refresh token support
