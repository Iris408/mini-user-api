# API Reference

This document lists the main API endpoints used by Mini User API.

## Core Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/` | API root status check |
| GET | `/health` | Health check endpoint |
| GET | `/ready` | Database readiness check |
| GET | `/docs` | Swagger API documentation |
| GET | `/openapi.json` | OpenAPI schema |

## Authentication Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Login and receive JWT token |

## User Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/users/me` | Get current authenticated user |
| GET | `/users` | Admin-only user list |

## Swagger Docs

Swagger UI is available locally at:

```text
http://127.0.0.1:8002/docs
```

Live Swagger UI is available at:

```text
https://mini-user-api.onrender.com/docs
```

## API Notes

Authenticated routes require a JWT access token in the `Authorization` header.

Example format:

```text
Authorization: Bearer your_access_token
```

Main backend responsibilities:

- Validate request and response data
- Register users
- Hash passwords before storing them
- Authenticate users
- Generate JWT access tokens
- Protect authenticated routes
- Restrict admin routes by user role
- Check app and database readiness