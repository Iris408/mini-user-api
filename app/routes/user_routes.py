from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user_model import UserRequest, User

from app.auth import (
    hash_password,
    verify_password,
    create_access_token
)

from app.auth import get_current_user


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

# EN: User login route
# JP: ユーザーログインルート
# KR: 사용자 로그인 라우트

@router.post("/login")
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    # EN: Find user by username
    user = db.query(User).filter(
       User.username == form_data.username
    ).first()

    if not user:

        raise HTTPExecption(
            status_code=401,
            detail="Invlaid username or password"
        )

    valid_password = verify_password(
        form_data.password,
        user.hashed_password
    )

    if not valid_password:

        raise HTTPException(
            status_code=401,
            detail="Invlaid username or password"
        )

    access_token = create_access_token(
        data={
            "sub": user.username
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

# EN: Protected profile route
# JP: 保護プロフィールルート
# KR: 보호 프로필 라우트

@router.get("/profile")
def get_profile(
    current_user: str = Depends(get_current_user)
):

    return {
        "message": "Protected profile accessed",
        "current_user": current_user
    }


# EN: Protected profile route
# JP: 保護プロフィールルート
# KR: 보호 프로필 라우트

@router.get("/profile")
def get_profile(
    current_user: str = Depends(get_current_user)
):

    return {
        "message": "Protected profile accessed",
        "current_user": current_user
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


# EN: Get all users from database
# JP: データベースから全ユーザー取得
# KR: 데이터베이스에서 모든 사용자 조회

@router.get("/users")
def get_users(db: Session = Depends(get_db)):

    users = db.query(User).all()

    return {
        "users": users
    }

# EN: Get one user from database by ID
# JP: IDでデータベースから1人のユーザー取得
# KR: ID로 데이터베이스에서 사용자 1명 조회

@router.get("/users/{user_id}")
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(User.id == user_id).first()

    if user:
        return {
            "user": user
        }

    return {
        "error": "User not found"
    }

# EN: Update user in database
# JP: データベース内ユーザー更新
# KR: 데이터베이스 사용자 수정

@router.put("/users/{user_id}")
def update_user(
    user_id: int,
    request: UserRequest,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(User.id == user_id).first()

    if user:

        user.name = request.name
        user.age = request.age

        db.commit()

        db.refresh(user)

        return {
            "message": "User updated",
            "user": user
        }

    return {
        "error": "User not found"
    }

# EN: Delete user from database
# JP: データベースからユーザー削除
# KR: 데이터베이스에서 사용자 삭제

@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(User.id == user_id).first()

    if user:

        db.delete(user)

        db.commit()

        return {
            "message": "User deleted"
        }

    return {
        "error": "User not found"
    }
