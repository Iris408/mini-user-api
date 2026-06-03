# Mini User API

Mini User API is a portfolio-ready FastAPI backend with PostgreSQL, SQLAlchemy, JWT authentication, role-based access control, Docker support, Swagger documentation, Render deployment, and GitHub Actions CI.

## ミニユーザーAPI

Mini User APIは、FastAPI、PostgreSQL、SQLAlchemy、JWT認証、ロールベースアクセス制御、Docker対応、Swaggerドキュメント、Renderデプロイ、GitHub Actions CIを備えたポートフォリオ用バックエンドAPIです。

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

---
## Live Demo / ライブデモ

[Mini User API Swagger Docs](https://mini-user-api.onrender.com/docs)

---

# Installation / インストール

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
### Running Locally
Run the FastAPI server locally:
```bash
uvicorn app.main:app --reload --port 8002
```

### Docker database connection

When running with Docker Compose, the backend connects to PostgreSQL using the Docker service name:
```env
DATABASE_URL =postgresql://postgres:postgres@db:5432/mini_user_api_db
```

```bash
docker compose up --build
```

Open Swagger UI:
```text
http://127.0.0.1:8002/docs
```

If `docker compose` does not work, try:

```bash
docker compose down
```

```bash
docker-compose up --build
```

If `Docker` is not available, the project can still be run manually:
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8002
```

Open Swagger UI:
```text
http://127.0.0.1:8002/docs
```

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

## Tech Stack / 技術スタック

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Uvicorn
- Docker
- Docker Compose
- Render deployment
- JWT Authentication
- bcrypt password hashing
- Git/GitHub
- GitHub Actions

---

## Authentication / 認証

This project includes basic JWT authentication.

Authentication features include:

- Password hashing before storing user passwords
- Login route for username/password validation
- JWT access token generation
- OAuth2 `/token` route for Swagger authorization
- Protected `/profile` route requiring a valid token
 
### API Endpoints | APIエンドポイント

| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/login` | Login and receive JWT token |
| GET | `/profile` | Get authenticated user profile |
| GET | `/users` | Get all users — admin only |

---

## Future Improvements

- Automated testing
- Environment variable documentation cleanup
- Refresh token support
- Improved role-based access control
- Docker production optimisation
- Deployment automation improvements
