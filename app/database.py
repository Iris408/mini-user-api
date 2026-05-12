from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# EN: PostgreSQL database URL
# JP: PostgreSQL データベースURL
# KR: PostgreSQL 데이터베이스 URL

DATABASE_URL = "postgresql://localhost/mini_user_api_db"


# EN: Create database engine
# JP: データベースエンジン作成
# KR: 데이터베이스 엔진 생성

engine = create_engine(DATABASE_URL)


# EN: Database session
# JP: データベースセッション
# KR: 데이터베이스 세션

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# EN: Base model
# JP: ベースモデル
# KR: 기본 모델

Base = declarative_base()
