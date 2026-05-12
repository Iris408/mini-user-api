## Mini User API / ミニユーザーAPI / 미니 사용자 API

Mini User API is a backend CRUD application built using FastAPI, PostgreSQL, and SQLAlchemy.

The project allows users to:
* Create Users
* Read Users
* Update Users
* Delete Users

The application uses persistent PostgreSQL database storage instead of temporary in-memory storage.

---

## Tech Stack / 技術スタック / 기술 스택

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Uvicorn
* Git/GitHub

---

## Features / 機能 / 기능

* RESTful CRUD API
* PostgreSQL data integration
* SQLAlchemy ORM
* Dependency injection
* Modular backend architecture
* JSON request validation
* Swagger API documentation

---

## Project Structure / プロジェクト構成 / 프로젝트 구조

```text
app/
├── routes/
├── models/
├── services/
├── database.py
├── main.py
```
---

## Installation / インストール / 설치

### Clone repository

```bash
git clone https://github.com/Iris408/mini-user-api
```
### Move into project folder

```bash
cd mini_user_api
```
### Install dependencies

```bash
pip install -r requirements.txt
```
### Start PostgreSQL

```bash
brew services start postgresql@18
```
### Run FastAPI server

```bash
uvicorn app.main:app --reload --port 8002
```
### Open Swagger UI

```text
http://127.0.0.1:8002/docs
```
---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | /users | Create a new user |
| GET | /users | Get all users |
| GET | /users/{id} | Get one user by ID |
| PUT | /users/{id} | Update a user |
| DELETE | /users/{id} | Delete a user |
---

## Future Improvements

* JWT authentication
* Docker support
* AWS deployment
* Frontend integration
* CI/CD pipelines

---

## Japanese / 日本語

このプロジェクトは FastAPI、PostgreSQL、SQLAlchemy を使用したバックエンド CRUD API です。

---

## Korean / 한국어

이 프로젝트는 FastAPI, PostgreSQL, SQLAlchemy를 사용한 백엔드 CRUD API 입니다.
