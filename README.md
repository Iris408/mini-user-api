![Backend CI](https://github.com/Iris408/mini-user-api/actions/workflows/backend-ci.yml/badge.svg)
![Docker CI](https://github.com/Iris408/mini-user-api/actions/workflows/docker-ci.yml/badge.svg)

# Mini User API / ミニユーザーAPI

Mini User API is a portfolio-ready FastAPI backend with PostgreSQL, SQLAlchemy, JWT authentication, role-based access control, Docker support, Swagger documentation, Render deployment, and GitHub Actions CI.

Mini User APIは、FastAPI、PostgreSQL、SQLAlchemy、JWT認証、ロールベースアクセス制御、Docker対応、Swaggerドキュメント、Renderデプロイ、GitHub Actions CIを備えたポートフォリオ用バックエンドAPIです。

## Live Demo / ライブデモ

JWT Backend deployed on Render:
* [Mini User API Swagger Docs](https://mini-user-api.onrender.com/docs)
* [Mini User API Root Endpoint](https://mini-user-api.onrender.com)

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

## Architecture / アーキテクチャ

### Backend

- FastAPI application
- Modular route structure
- SQLAlchemy ORM models
- PostgreSQL database connection
- JWT authentication
- Role-based access control

### Database

- PostgreSQL
- User records stored through SQLAlchemy models
- Database connection configured with `DATABASE_URL`

### DevOps / Deployment

- Docker and Docker Compose for local containerized development
- Render deployment for the live backend
- GitHub Actions for backend and Docker CI
- Swagger UI for API testing and documentation

## API Endpoints | APIエンドポイント

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API status check |
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Login and receive JWT token |
| GET | `/users/me` | Get current authenticated user |
| GET | `/users` | Admin-only user list |
| GET | `/docs` | Swagger API documentation |
| GET | `/health` | Health check endpoint |

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

### Docker database connection

When running with Docker Compose, the backend connects to PostgreSQL using the Docker service name `db`.

```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/mini_user_api_db
```

Ensure Docker Desktop is open and running:

```bash
docker compose up --build
```
Open the local API:
```text
http://127.0.0.1:8002
http://127.0.0.1:8002/health
http://127.0.0.1:8002/docs
```

If `docker compose` does not work, try restarting the containers:

```bash
docker compose down
docker compose up --build
```

If your system uses the older `Docker Compose` command try:

```bash
docker-compose up --build
```

### Manual local database connection

If `Docker` is not available, the project can still be run manually.

When running the backend directly with `Uvicorn`, use `localhost` instead of `db`:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/mini_user_api_db
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the FastAPI server:
```bash
uvicorn app.main:app --reload --port 8002
```

Open the local API:
```text
http://127.0.0.1:8002
http://127.0.0.1:8002/health
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

* Root endpoint
* Health check endpoint
* Database readiness endpoint
* OpenAPI schema availability

現在の基本的なテスト範囲は以下です。

* ルートエンドポイント
* ヘルスチェックエンドポイント
* データベース準備状況エンドポイント
* OpenAPIスキーマの可用性

各エンドポイントはSwagger UIから確認・テストできます。認証が必要なルートでは、JWTアクセストークンを `Authorization` ヘッダーに付与してリクエストします。

## Environment Variables / 環境変数

Create a local `.env` file in the project root.

```env
DATABASE_URL=
SECRET_KEY=
ALGORITHM=
ACCESS_TOKEN_EXPIRE_MINUTES=
```

## CI/CD / 継続的インテグレーション

This project uses GitHub Actions for automated checks.

Current workflows:

- `backend-ci.yml` runs backend checks and tests.
- `docker-ci.yml` checks Docker build/container setup.

The goal of CI is to make sure changes are tested before they are merged into the main branch.

## Known Limitations / 現在の制限

- Free Render services may sleep after inactivity.
- Refresh tokens are not implemented yet.
- Password reset is not implemented yet.
- Test coverage is currently basic.
- Admin functionality is intentionally simple for portfolio scope.

## Future Improvements / 今後の改善

### Testing

- Expand authentication route tests
- Add protected route tests
- Add admin-only route tests
- Add database integration tests

### Authentication

- Add refresh token support
- Add password reset flow
- Add email verification

### DevOps

- Improve Docker production configuration
- Add deployment automation improvements
- Add structured logging
- Add monitoring/uptime checks

### Frontend Integration

- Connect to a polished React/TypeScript frontend
- Add demo user and demo admin login flow