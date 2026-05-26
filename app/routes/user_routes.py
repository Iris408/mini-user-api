from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user_model import UserRequest,UserLoginRequest, UserUpdateRequest, User

from app.auth import (
    create_access_token,
    verify_password,
    hash_password,
    get_current_user,
    require_admin
)


# EN: Create router
# JP: ルーター作成
# KR: 라우터 생성

router = APIRouter()


# EN: Create new user
# JP: 新規ユーザー作成
# KR: 새 사용자 생성

@router.post("/register")
def register_user(
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

    hashed_pw = hash_password(
        request.password
    )

    new_user = User(
        username=request.username,
        hashed_password=hashed_pw
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "User registered successfully"
    }

# =========================================
# EN: Login user
# JP: ユーザーログイン
# KR: 사용자 로그인
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

    return {
        "message": "Login successful",
        "user": {
            "id": user.id,
            "username": user.username,
            "role": user.role
        }
    }


# EN: Protected profile route
# JP: 保護プロフィールルート
# KR: 보호 프로필 라우트

@router.get("/profile")
def get_profile(
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.username == current_user["username"]
    ).first()

    return {
        "id": user.id,
        "username": user.username,
        "role": user.role
    }


# EN: Invalid username check
# JP: 無効ユーザー名確認
# KR: 잘못된 사용자 이름 확인

    if not user:

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

# EN: Verify hashed password
# JP: ハッシュ化パスワード確認
# KR: 해시 비밀번호 확인

    valid_password = verify_password(
        request.password,
        user.hashed_password
    )

# EN: Invalid password check
# JP: 無効パスワード確認
# KR: 잘못된 비밀번호 확인

    if not valid_password:

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

# EN: Create JWT token
# JP: JWT トークン作成
# KR: JWT 토큰 생성

    access_token = create_access_token(
        data={
            "sub": user.username
        }
    )

# EN: Return login token
# JP: ログイントークン返却
# KR: 로그인 토큰 반환

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# EN: Get all users from PostgreSQL
# JP: PostgreSQLから全ユーザー取得
# KR: PostgreSQL에서 모든 사용자 조회


@router.get("/users")
def get_users(db: Session = Depends(get_db)):

    users = db.query(User).all()

    return {

        "users": users
    }

# EN: Get one user by ID from PostgreSQL
# JP: PostgreSQL からIDでユーザーを1人取得
# KR: PostgreSQL에서 ID로 사용자 1명 조회

@router.get("/users/{user_id}")
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "user": user
    }

# EN: Update user by ID in PostgreSQL
# JP: PostgreSQL 内のユーザーをIDで更新
# KR: PostgreSQL에서 ID로 사용자 수정

@router.put("/users/{user_id}")
def update_user(
    user_id: int,
    request: UserUpdateRequest,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(User.id == user_id).first()

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


# EN: Admin dashboard route
# JP: 管理者ダッシュボードルート
# KR: 관리자 대시보드 라우트

@router.get("/admin/dashboard")
def admin_dashboard(
    admin_user = Depends(require_admin)
):

    return {
        "message": "Admin dashboard accessed",
        "admin_user": admin_user
    }


# EN: Delete user by ID from PostgreSQL
# JP: PostgreSQL からIDでユーザーを削除
# KR: PostgreSQL에서 ID로 사용자 삭제

@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(User.id == user_id).first()

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


# EN: Admin-only route
# JP: 管理者専用ルート
# KR: 관리자 전용 라우트

@router.get("admin")
def admin_dashboard(
    current_user = Depends(require_admin)
):
    return {
        "message": "Welcome Admin",
        "user": current_user
    }
