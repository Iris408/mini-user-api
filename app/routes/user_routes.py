from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.models.user_model import UserRequest, User
from app.database import SessionLocal

# EN: Create router
# JP: ルーター作成
# KR: 라우터 생성

router = APIRouter()


# EN: Create new user
# JP: 新規ユーザー作成
# KR: 새 사용자 생성

@router.post("/users")
def create_user(request: UserRequest):

    db: Session = SessionLocal()

    new_user = User(
        name=request.name,
        age=request.age
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    db.close()

    return {
        "message": "User created",
        "user": {
            "id": new_user.id,
            "name": new_user.name,
            "age": new_user.age
        }
    }

# EN: Get all users
# JP: 全ユーザー取得
# KR: 모든 사용자 가져오기

@router.get("/users")
def get_users():
    return {
        "users": users
    }

# EN: Get user by ID
# JP: IDでユーザー取得
# KR: ID로 사용자 조회

@router.get("/users/{user_id}")
def get_user(user_id: int):

    for user in users:
        if user["id"] == user_id:
            return {"user": user}

    return {"error": "User not found"}


# EN: Update user by ID
# JP: IDでユーザー更新
# KR: ID로 사용자 수정

@router.put("/users/{user_id}")
def update_user(user_id: int, request: UserRequest):

    for user in users:
        if user["id"] == user_id:
            user["name"] = request.name
            user["age"] = request.age

            return {
                "message": "User updated",
                "user": user
            }

    return {"error": "User not found"}


# EN: Delete user by ID
# JP: IDでユーザー削除
# KR: ID로 사용자 삭제

@router.delete("/users/{user_id}")
def delete_user(user_id: int):

    for user in users:
        if user["id"] == user_id:
            users.remove(user)

            return {
                "message": "User deleted",
                "deleted_user": user
            }

    return {"error": "User not found"}


# EN: Get user by ID
# JP: IDでユーザー取得
# KR: ID로 사용자 조회

@router.get("/users/{user_id}")
def get_user(user_id: int):

    for user in users:

        if user["id"] == user_id:
            return {
                "user": user
            }

    return {
        "error": "User not found"
    }

# EN: Delete user by ID
# JP: IDでユーザー削除
# KR: ID로 사용자 삭제

@router.delete("/users/{user_id}")
def delete_user(user_id: int):

    for user in users:

        if user["id"] == user_id:
            users.remove(user)

            return {
                "message": "User deleted",
                "deleted_user": user
            }

    return {
        "error": "User not found"
    }

# EN: Update user by ID
# JP: IDでユーザー更新
# KR: ID로 사용자 수정

@router.put("/users/{user_id}")
def update_user(user_id: int, request: UserRequest):

    for user in users:

        if user["id"] == user_id:

            user["name"] = request.name
            user["age"] = request.age

            return {
                "message": "User updated",
                "user": user
            }

    return {
        "error": "User not found"
    }
