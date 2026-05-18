from pydantic import BaseModel

from sqlalchemy import Column, Integer, String
from app.database import Base


# EN: Pydantic request model
# JP: Pydantic リクエストモデル
# KR: Pydantic 요청 모델

class UserRequest(BaseModel):
    username: str
    password: str


# EN: SQLAlchemy database model
# JP: SQLAlchemy データベースモデル
# KR: SQLAlchemy 데이터베이스 모델

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String, unique=True, index=True)

    hashed_password = Column(String)
