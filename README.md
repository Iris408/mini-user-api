# Mini User API / ミニユーザーAPI

Mini User API is a FastAPI backend with PostgreSQL and SQLAlchemy, providing JWT authentication 
and role-based access control for the JWT Authentication Dashboard frontend.

Mini User APIは、JWT認証ダッシュボードフロントエンド向けに、JWT認証とロールベースアクセス制御を提供する
FastAPIバックエンドです。

---

The project allows users to:

- Create users
- Read users
- Update users
- Delete users

The application uses persistent PostgreSQL database storage instead of temporary in-memory storage.

---

## Current Status

| Status Item | Complete |
|---|---|
| Backend deployed on Render | ✅ |
| PostgreSQL database connected | ✅ |
| JWT authentication working | ✅ |
| Role-based access control working | ✅ |
| Docker support added | ✅ |
| Swagger API documentation available | ✅ |
| Backend CI workflow added with GitHub Actions | ✅ |
| Backend CI passing | ✅ |

---

## Portfolio Ready v1 / ポートフォリオ準備完了 v1

| Area |	Status |
| --- | --- |
| Backend API	| ✅ Complete |
| PostgreSQL database	| ✅ Connected |
| JWT authentication	| ✅ Working |
| Role-based access control	| ✅ Working |
| Docker support	| ✅ Complete |
| Render deployment	| ✅ Live |
| Swagger API documentation	| ✅ Available |
| GitHub Actions CI	| ✅ Passing |

This project is portfolio-ready as a deployed backend API with authentication, database persistence, Docker support, role-based access control, Swagger documentation, and CI checks.

---

## Live Demo / ライブデモ

```text
https://mini-user-api.onrender.com/docs
```

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
- Backend CI pipeline with GitHub Actions

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

## Installation / インストール

Clone the repository:

```bash
git clone https://github.com/Iris408/mini-user-api
```

Move into project folder:
```bash
cd mini-user-api
```

Install dependencies:
```bash
pip install -r requirements.txt
```
 
Start PostgreSQL:
```bash
psql postgres
```
```SQL
CREATE DATABASE mini_user_api_db;
```

Exit PostgreSQL:
```SQL
\q
```
Run the FastAPI server:
```bash
uvicorn app.main:app --reload --port 8002
```
---

## Run with Docker

```bash
docker compose up --build
```

Open Swagger UI:
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
| GET | `/users` | Get all users - admin only |
| GET | `/users/{user_id}` | Get one user by ID |
| PUT | `/users/{user_id}` | Update a user |
| DELETE | `/users/{user_id}` | Delete a user |
| GET | `/` | Home/Health check |

---

## Future Improvements

- Refresh token support
- Deployment automation improvements
- Automated testing
- Improved role-based access control
- Docker production optimisation
