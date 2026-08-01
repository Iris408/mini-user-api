# Auth Flow

This document explains the authentication flow used by Secure User Management API.

## Authentication Type

Secure User Management API uses JWT access token authentication.

The project includes:

- User registration
- Password hashing
- Login route
- JWT access token generation
- Protected user route
- Admin-only route
- OAuth2 token flow for Swagger authorization

## Basic Flow

```text
1. User registers with username and password.
2. Backend hashes the password before storing it.
3. User logs in with valid credentials.
4. Backend returns a JWT access token.
5. Client sends the token in the Authorization header.
6. Protected routes verify the token.
7. Admin-only routes also check the authenticated user's role.
```

## Password Hashing

Passwords are hashed before being saved.

This means the plain-text password should not be stored in the database.

## JWT Login

When a user logs in successfully, the backend returns an access token.

Example token usage:

```text
Authorization: Bearer your_access_token
```

## Protected Route

The `/users/me` route requires a valid JWT token.

It returns the currently authenticated user.

## Admin-only Route

The `/users` route is restricted to admin users.

This demonstrates basic role-based access control.

## Future Auth Improvements

- Add refresh token support
- Add password reset flow
- Add email verification
- Improve role-based access control
- Add more authentication route tests