![Backend CI](https://github.com/Iris408/mini-user-api/actions/workflows/backend-ci.yml/badge.svg)

# Mini User API / ミニユーザーAPI

Mini User API is a portfolio-ready FastAPI backend with PostgreSQL, SQLAlchemy, JWT authentication, role-based access control, Docker support, Swagger documentation, Render deployment, and GitHub Actions CI.

Mini User APIは、FastAPI、PostgreSQL、SQLAlchemy、JWT認証、ロールベースアクセス制御、Docker対応、Swaggerドキュメント、Renderデプロイ、GitHub Actions CIを備えたポートフォリオ用バックエンドAPIです。

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

## Live Demo / ライブデモ

JWT Backend deployed on Render:
* [Mini User API Swagger Docs](https://mini-user-api.onrender.com/docs)
* [Mini User API Root Endpoint](https://mini-user-api.onrender.com)


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
### Running Locally
Run the FastAPI server locally:
```bash
uvicorn app.main:app --reload --port 8002
```

Open Swagger UI:
```text
http://127.0.0.1:8002/docs
```

### Docker database connection

When running with Docker Compose, the backend connects to PostgreSQL using the Docker service name:
```env
DATABASE_URL =postgresql://postgres:postgres@db:5432/mini_user_api_db
```

Ensure Docker Desktop is open and running:
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

### Running Tests / テスト実行

This project uses pytest for backend testing.

このプロジェクトでは、バックエンドテストに pytest を使用しています。

**Run tests with Docker Compose**
Make sure the Docker containers are running:
```bash
docker compose up -d --build
```

Run the test suite inside the API container:
```bash
docker compose exec api pytest
```

**Current test coverage / 現在のテスト範囲**

Current basic test coverage includes:

* Health check endpoint
* OpenAPI schema availability

現在の基本的なテスト範囲は以下です。

* ヘルスチェックエンドポイント
* OpenAPIスキーマの確認

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
- Role-based admin-only user list
- Dockerized FastAPI and PostgreSQL setup
- Backend CI pipeline with GitHub Actions
- Basic backend testing with pytest

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
- pytest
- Git/GitHub
- GitHub Actions

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
| GET | `/` | API status check |
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Login and receive JWT token |
| GET | `/users/me` | Get current authenticated user |
| GET | `/users` | Admin-only user list |
| GET | `/docs` | Swagger API documentation |

各エンドポイントはSwagger UIから確認・テストできます。認証が必要なルートでは、JWTアクセストークンを `Authorization` ヘッダーに付与してリクエストします。

## Future Improvements

* Expand automated test coverage
* Add authentication route tests
* Add protected route tests
* Add admin-only route tests
* Environment variable documentation cleanup
* Refresh token support
* Improved role-based access control
* Docker production optimisation
* Deployment automation improvements