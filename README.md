![Backend CI](https://github.com/Iris408/mini-user-api/actions/workflows/backend-ci.yml/badge.svg)
![Docker CI](https://github.com/Iris408/mini-user-api/actions/workflows/docker-ci.yml/badge.svg)

# Mini User API / ミニユーザーAPI

Mini User API is a portfolio-ready FastAPI backend project built with PostgreSQL, SQLAlchemy, JWT authentication, role-based access control, Docker, Swagger documentation, Render deployment, pytest, and GitHub Actions CI.

Mini User APIは、FastAPI、PostgreSQL、SQLAlchemy、JWT認証、ロールベースアクセス制御、Docker、Swaggerドキュメント、Renderデプロイ、pytest、GitHub Actions CIを使用したポートフォリオ用バックエンドAPIです。

---

## Live Demo / ライブデモ

JWT backend deployed on Render:

- [Mini User API Root Endpoint](https://mini-user-api.onrender.com)
- [Mini User API Health Check](https://mini-user-api.onrender.com/health)
- [Mini User API Readiness Check](https://mini-user-api.onrender.com/ready)
- [Mini User API Swagger Docs](https://mini-user-api.onrender.com/docs)

---

## Portfolio Status / ポートフォリオステータス

| Area | Status |
|---|---|
| Backend API | ✅ Complete |
| PostgreSQL database | ✅ Connected |
| JWT authentication | ✅ Working |
| Role-based access control | ✅ Working |
| Docker support | ✅ Complete |
| Render deployment | ✅ Live |
| Swagger API documentation | ✅ Available |
| Backend tests | ✅ Basic coverage added |
| GitHub Actions backend CI | ✅ Passing |
| GitHub Actions Docker CI | ✅ Passing |

---

## Features / 機能

- RESTful FastAPI backend
- PostgreSQL database integration
- SQLAlchemy ORM models
- Dependency injection
- Modular backend route structure
- JSON request validation
- Swagger API documentation
- Password hashing with bcrypt
- JWT access token generation
- OAuth2 token route for Swagger authorization
- Protected authenticated user route
- Role-based admin-only user list
- Dockerized FastAPI and PostgreSQL setup
- Health check endpoint
- Database readiness endpoint
- Backend testing with pytest
- GitHub Actions CI workflows
- Render deployment

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
- pytest
- Git / GitHub
- GitHub Actions
- Render

---

## Architecture / アーキテクチャ

### Backend

The backend is built with FastAPI and organized using modular route files.

Main backend responsibilities:

- Handle API requests
- Validate request and response data
- Manage user registration and login
- Hash passwords before storing them
- Generate JWT access tokens
- Protect authenticated routes
- Restrict admin-only routes by role

### Database

PostgreSQL is used as the relational database.

SQLAlchemy is used to:

- Define database models
- Connect FastAPI to PostgreSQL
- Create and query user records
- Manage database sessions

### Authentication

Authentication uses JWT access tokens.

Basic authentication flow:

1. User registers with a username and password.
2. Password is hashed before being stored.
3. User logs in with valid credentials.
4. Backend returns a JWT access token.
5. Protected routes require the token in the `Authorization` header.
6. Admin-only routes check the authenticated user role.

### DevOps / Deployment

The project includes:

- Docker Compose for local containerized development
- Render for live backend deployment
- GitHub Actions for backend CI and Docker CI
- Swagger UI for live API testing
- Health and readiness endpoints for deployment checks

---

## API Endpoints / APIエンドポイント

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API root status check |
| GET | `/health` | Health check endpoint |
| GET | `/ready` | Database readiness check |
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Login and receive JWT token |
| GET | `/users/me` | Get current authenticated user |
| GET | `/users` | Admin-only user list |
| GET | `/docs` | Swagger API documentation |
| GET | `/openapi.json` | OpenAPI schema |

各エンドポイントはSwagger UIから確認・テストできます。認証が必要なルートでは、JWTアクセストークンを `Authorization` ヘッダーに付与してリクエストします。

---

## Installation / インストール

Clone the repository:

```bash
git clone https://github.com/Iris408/mini-user-api
```

Move into the project folder:

```bash
cd mini-user-api
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables / 環境変数

Create a local `.env` file in the project root.

Example variables:

```env
DATABASE_URL=
SECRET_KEY=
ALGORITHM=
ACCESS_TOKEN_EXPIRE_MINUTES=
```

Never commit real `.env` files or production secrets to GitHub.

Make sure `.gitignore` includes:

```txt
.env
.venv/
__pycache__/
.pytest_cache/
*.pyc
```

---

## Docker Database Connection / Dockerデータベース接続

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
http://127.0.0.1:8002/ready
http://127.0.0.1:8002/docs
```

If `docker compose` does not work, try restarting the containers:

```bash
docker compose down
docker compose up --build
```

If your system uses the older Docker Compose command, try:

```bash
docker-compose up --build
```

---

## Manual Local Database Connection / 手動ローカルデータベース接続

If Docker is not available, the project can still be run manually.

When running the backend directly with Uvicorn, use `localhost` instead of `db`:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/mini_user_api_db
```

Make sure PostgreSQL is running locally and that `mini_user_api_db` has already been created.

Run the FastAPI server:

```bash
uvicorn app.main:app --reload --port 8002
```

Open the local API:

```text
http://127.0.0.1:8002
http://127.0.0.1:8002/health
http://127.0.0.1:8002/ready
http://127.0.0.1:8002/docs
```

---

## Running Tests / テスト実行

This project uses pytest for backend testing.

このプロジェクトでは、バックエンドテストに pytest を使用しています。

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

現在の基本的なテスト範囲は以下です。

- ルートエンドポイント
- ヘルスチェックエンドポイント
- データベース準備確認エンドポイント
- OpenAPIスキーマの確認

---

## CI/CD / 継続的インテグレーション

This project uses GitHub Actions for automated checks.

Current workflows:

- `backend-ci.yml` runs backend checks and pytest tests.
- `docker-ci.yml` checks Docker build and container setup.

The goal of CI is to make sure changes are tested before they are merged into the main branch.

---

## Screenshots / スクリーンショット

Screenshots can be added to the `screenshots/` folder.

Recommended screenshots:

```txt
screenshots/
  01-swagger-docs.png
  02-root-endpoint.png
  03-health-endpoint.png
  04-ready-endpoint.png
  05-github-actions-ci.png
  06-render-deployment.png
```

Example README usage:

```md
![Swagger Docs](screenshots/01-swagger-docs.png)
```

---

## Known Limitations / 現在の制限

- Free Render services may sleep after inactivity.
- Refresh tokens are not implemented yet.
- Password reset is not implemented yet.
- Test coverage is currently basic.
- Admin functionality is intentionally simple for portfolio scope.
- CORS origins are currently configured in the backend code and can be moved to environment variables later.

---

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
- Improve role-based access control

### DevOps

- Improve Docker production configuration
- Add deployment automation improvements
- Add structured logging
- Add monitoring or uptime checks
- Move CORS origins into environment variables

### Frontend Integration

- Connect to a polished React/TypeScript frontend
- Add demo user and demo admin login flow
- Add frontend screenshots and demo walkthrough

---

## Project Purpose / プロジェクトの目的

This project was built to practice real junior backend engineering skills, including API design, authentication, database persistence, Docker, testing, deployment, and CI workflows.

このプロジェクトは、API設計、認証、データベース永続化、Docker、テスト、デプロイ、CIワークフローなど、ジュニアバックエンドエンジニアに必要な実践的スキルを練習するために作成しました。