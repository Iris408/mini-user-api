from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.user_model import UserRequest, User
from app.database import SessionLocal, get_db
from app.database import get_db

# EN: Create router
# JP: ルーター作成
# KR: 라우터 생성

router = APIRouter()


# EN: Create new user
# JP: 新規ユーザー作成
# KR: 새 사용자 생성

@router.post("/users")
def create_user(
    request: UserRequest,
    db: Session = Depends(get_db)
):

    new_user = User(
        name=request.name,
        age=request.age
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "User created",
        "user": {
            "id": new_user.id,
            "name": new_user.name,
            "age": new_user.age
        }
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
