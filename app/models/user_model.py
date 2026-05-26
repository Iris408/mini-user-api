from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from app.database import Base


# =========================================
# EN: Request model for creating a user
# JP: ユーザー作成用リクエストモデル
# KR: 사용자 생성 요청 모델
# =========================================

class UserRequest(BaseModel):
    username: str
    password: str
    role: str = "user"

class UserLoginRequest(BaseModel):
    username: str
    password: str

class UserUpdateRequest(BaseModel):
    username: str
    role: str = "user"

# =========================================
# EN: Request model for updating a user
# JP: ユーザー更新用リクエストモデル
# KR: 사용자 수정 요청 모델
# =========================================

class UserUpdateRequest(BaseModel):
    username: str
    role: str = "user"


# =========================================
# EN: SQLAlchemy database model for users table
# JP: users テーブル用 SQLAlchemy データベースモデル
# KR: users 테이블용 SQLAlchemy 데이터베이스 모델
# =========================================

class User(Base):

    __tablename__ = "users"

    # EN: Unique user ID
    # JP: 一意のユーザーID
    # KR: 고유 사용자 ID
    id = Column(Integer, primary_key=True, index=True)

    # EN: Username used for login
    # JP: ログイン用ユーザー名
    # KR: 로그인용 사용자 이름
    username = Column(String, unique=True, index=True)

    # EN: Hashed password stored safely
    # JP: 安全に保存されるハッシュ化パスワード
    # KR: 안전하게 저장되는 해시된 비밀번호
    hashed_password = Column(String)

    # EN: User role, for example "user" or "admin"
    # JP: ユーザー権限。例: "user" または "admin"
    # KR: 사용자 역할. 예: "user" 또는 "admin"
    role = Column(String, default="user")
