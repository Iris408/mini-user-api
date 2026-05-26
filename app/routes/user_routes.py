from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user_model import (
    User,
    UserRequest,
    UserLoginRequest,
    UserUpdateRequest
)

from app.auth import (
    hash_password,
    verify_password,
    create_access_token,
    get_current_user
)


# =========================================
# EN: Create router
# JP: ルーター作成
# KR: 라우터 생성
# =========================================

router = APIRouter()


# =========================================
# EN: Create new user
# JP: 新規ユーザー作成
# KR: 새 사용자 생성
# =========================================

@router.post("/users")
def create_user(
    request: UserRequest,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.username == request.username
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    new_user = User(
        username=request.username,
        hashed_password=hash_password(request.password),
        role=request.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User created",
        "user": {
            "id": new_user.id,
            "username": new_user.username,
            "role": new_user.role
        }
    }


# =========================================
# EN: Login user and return JWT token
# JP: ユーザーにログインし、JWTトークンを返す
# KR: 사용자 로그인 후 JWT 토큰 반환
# =========================================

@router.post("/login")
def login_user(
    request: UserLoginRequest,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.username == request.username
    ).first()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    if not verify_password(request.password, user.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    access_token = create_access_token(
        data={
            "sub": user.username,
            "role": user.role
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# =========================================
# EN: OAuth2 login route for Swagger Authorize
# JP: Swagger認証用 OAuth2 ログインルート
# KR: Swagger 인증용 OAuth2 로그인 라우트
# =========================================

@router.post("/token")
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.username == form_data.username
    ).first()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    access_token = create_access_token(
        data={
            "sub": user.username,
            "role": user.role
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

# =========================================
# EN: Protected profile route
# JP: 保護プロフィールルート
# KR: 보호 프로필 라우트
# =========================================

@router.get("/profile")
def get_profile(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.username == current_user["username"]
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "message": "Protected profile access granted",
        "user": {
            "id": user.id,
            "username": user.username,
            "role": user.role
        }
    }


# =========================================
# EN: Get all users from PostgreSQL
# JP: PostgreSQL から全ユーザーを取得
# KR: PostgreSQL에서 모든 사용자 조회
# =========================================

@router.get("/users")
def get_users(
    db: Session = Depends(get_db)
):

    users = db.query(User).all()

    return {
        "users": [
            {
                "id": user.id,
                "username": user.username,
                "role": user.role
            }
            for user in users
        ]
    }


# =========================================
# EN: Get one user by ID from PostgreSQL
# JP: PostgreSQL からIDでユーザーを1人取得
# KR: PostgreSQL에서 ID로 사용자 1명 조회
# =========================================

@router.get("/users/{user_id}")
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "user": {
            "id": user.id,
            "username": user.username,
            "role": user.role
        }
    }


# =========================================
# EN: Update user by ID in PostgreSQL
# JP: PostgreSQL 内のユーザーをIDで更新
# KR: PostgreSQL에서 ID로 사용자 수정
# =========================================

@router.put("/users/{user_id}")
def update_user(
    user_id: int,
    request: UserUpdateRequest,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    user.username = request.username
    user.role = request.role

    db.commit()
    db.refresh(user)

    return {
        "message": "User updated",
        "user": {
            "id": user.id,
            "username": user.username,
            "role": user.role
        }
    }


# =========================================
# EN: Delete user by ID from PostgreSQL
# JP: PostgreSQL からIDでユーザーを削除
# KR: PostgreSQL에서 ID로 사용자 삭제
# =========================================

@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    deleted_user = {
        "id": user.id,
        "username": user.username,
        "role": user.role
    }

    db.delete(user)
    db.commit()

    return {
        "message": "User deleted",
        "deleted_user": deleted_user
    }
