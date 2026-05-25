# Mini User API / ミニユーザーAPI / 미니 사용자 API

Mini User API is a backend CRUD application built with FastAPI, PostgreSQL, and SQLAlchemy.
Mini User APIは、FastAPI、PostgreSQL、およびSQLAlchemyを使用して構築されたバックエンドCRUDアプリケーションです。
Mini User API는 FastAPI, PostgreSQL 및 SQLAlchemy를 사용하여 구축된 백엔드 CRUD 애플리케이션입니다.

---

The project allows users to:

- Create users
- Read users
- Update users
- Delete users

The application uses persistent PostgreSQL database storage instead of temporary in-memory storage.

---

## Tech Stack / 技術スタック / 기술 스택

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Uvicorn
- Git/GitHub

---

## Features / 機能 / 기능

- RESTful CRUD API
- PostgreSQL database integration
- SQLAlchemy ORM
- Dependency injection
- Modular backend architecture
- JSON request validation
- Swagger API documentation

---

## Project Structure / プロジェクト構成 / 프로젝트 구조

```text
app/
├── routes/
│   └── user_routes.py
├── models/
│   └── user_model.py
├── services/
├── database.py
└── main.py

---

## Installation / インストール / 설치

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
```SQL
CREATE DATABASE mini_user_api_db;

Exit PostgreSQL:
```SQL
\q
```
• Run FastAPI server
```bash
uvicorn app.main:app --reload --port 8002
```

•Open Swagger UI
http://127.0.0.1:8002/docs

---
 
## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/users` | Create a new user |
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
- Swagger API testing via `/docs`

---

## Future Improvements

- JWT authentication
- Docker support
- AWS deployment
- Frontend integration
- CI/CD pipelines
