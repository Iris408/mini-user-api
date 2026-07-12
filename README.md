![Backend CI](https://github.com/Iris408/mini-user-api/actions/workflows/backend-ci.yml/badge.svg)
![Docker CI](https://github.com/Iris408/mini-user-api/actions/workflows/docker-ci.yml/badge.svg)

# Mini User API

Mini User API is a FastAPI backend project built with PostgreSQL, SQLAlchemy, JWT authentication, role-based access control, Docker, pytest, Render deployment, Swagger documentation, and GitHub Actions CI.

The project demonstrates practical junior backend engineering skills including API design, authentication, password hashing, protected routes, admin-only access, database persistence, health checks, Docker support, testing, and CI/CD workflows.

## Live Demo

JWT backend deployed on Render:

- [Root Endpoint](https://mini-user-api.onrender.com)
- [Health Check](https://mini-user-api.onrender.com/health)
- [Readiness Check](https://mini-user-api.onrender.com/ready)
- [Swagger API Docs](https://mini-user-api.onrender.com/docs)

## Current Status

| Area | Status |
| --- | --- |
| FastAPI backend | ✅ Complete |
| PostgreSQL database | ✅ Connected |
| SQLAlchemy ORM | ✅ Complete |
| JWT authentication | ✅ Working |
| Password hashing | ✅ Working |
| Role-based access control | ✅ Working |
| Docker support | ✅ Complete |
| Render deployment | ✅ Live |
| Swagger API documentation | ✅ Available |
| Backend tests | ✅ Basic coverage added |
| Backend CI | ✅ Passing |
| Docker CI | ✅ Passing |

## Features

- RESTful FastAPI backend
- PostgreSQL database integration
- SQLAlchemy ORM models
- User registration and login
- Password hashing with bcrypt
- JWT access token generation
- OAuth2 token route for Swagger authorization
- Protected authenticated user route
- Role-based admin-only user list
- Health check endpoint
- Database readiness endpoint
- Dockerized FastAPI and PostgreSQL setup
- Backend testing with pytest
- GitHub Actions backend and Docker CI
- Render deployment

## Tech Stack

| Area | Technologies |
| --- | --- |
| Backend | Python, FastAPI, SQLAlchemy, Uvicorn |
| Database | PostgreSQL |
| Authentication | JWT, OAuth2, bcrypt password hashing |
| Testing | pytest |
| DevOps / Tooling | Docker, Docker Compose, GitHub Actions, Render, Git, GitHub |

## Screenshots

| Swagger API Docs | Root Endpoint | Health Check |
| --- | --- | --- |
| ![Swagger API Docs](screenshots/01-swagger-docs.png) | ![Root Endpoint](screenshots/02-root-endpoint.png) | ![Health Check](screenshots/03-health-endpoint.png) |

| Database Readiness | GitHub Actions CI | Render Deployment |
| --- | --- | --- |
| ![Database Readiness](screenshots/04-ready-endpoint.png) | ![GitHub Actions CI](screenshots/05-github-actions-ci.png) | ![Render Deployment](screenshots/06-render-deployment.png) |

## Quick Start

Clone the repository:

```bash
git clone https://github.com/Iris408/mini-user-api
cd mini-user-api
```

Run with Docker Compose:

```bash
docker compose up --build
```

Local API:

```text
http://127.0.0.1:8002
```

Swagger Docs:

```text
http://127.0.0.1:8002/docs
```

Run tests:

```bash
docker compose exec api pytest
```

## Documentation

More detailed project documentation is available in the `docs/` folder.

| Document | Description |
| --- | --- |
| [Setup Guide](./docs/setup.md) | Environment variables, Docker setup, manual setup, and test commands |
| [API Reference](./docs/api-reference.md) | Main API endpoints and route notes |
| [Auth Flow](./docs/auth-flow.md) | JWT authentication, protected routes, and admin-only access |
| [Project Details](./docs/project-details.md) | Architecture, limitations, future improvements, and learning notes |
| [CI/CD Notes](./docs/ci-cd.md) | Backend CI and Docker CI workflow notes |

## Project Summary

Mini User API is a backend portfolio project built to practise real API development skills: user authentication, JWT token handling, role-based access control, PostgreSQL persistence, Dockerized development, health checks, testing, deployment, and CI/CD validation.

## Author

Built by Iris408