# Project Details

This document contains additional technical notes for Mini User API.

## Architecture

```text
FastAPI Backend
      ↓
SQLAlchemy ORM
      ↓
PostgreSQL Database
```

## Backend Responsibilities

The backend is built with FastAPI and organized using modular route files.

Main backend responsibilities:

- Handle API requests
- Validate request and response data
- Manage user registration and login
- Hash passwords before storing them
- Generate JWT access tokens
- Protect authenticated routes
- Restrict admin-only routes by role
- Expose health and readiness endpoints
- Provide Swagger API documentation

## Database

PostgreSQL is used as the relational database.

SQLAlchemy is used to:

- Define database models
- Connect FastAPI to PostgreSQL
- Create and query user records
- Manage database sessions

## DevOps / Deployment

The project includes:

- Docker Compose for local containerized development
- Render for live backend deployment
- GitHub Actions for backend CI and Docker CI
- Swagger UI for live API testing
- Health and readiness endpoints for deployment checks

## Known Limitations

- Free Render services may sleep after inactivity.
- Refresh tokens are not implemented yet.
- Password reset is not implemented yet.
- Test coverage is currently basic.
- Admin functionality is intentionally simple for portfolio scope.
- CORS origins can be moved to environment variables later if needed.

## Future Improvements

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
- Move CORS origins into environment variables if needed

### Frontend Integration

- Connect to a polished React/TypeScript frontend
- Add demo user and demo admin login flow
- Add frontend screenshots and demo walkthrough

## What I Learned

Through this project, I practiced:

- FastAPI backend structure
- REST API design
- PostgreSQL database integration
- SQLAlchemy ORM models
- Password hashing
- JWT authentication
- OAuth2 token flow in Swagger
- Protected routes
- Role-based access control
- Docker Compose development
- Render deployment
- pytest backend testing
- GitHub Actions CI workflows