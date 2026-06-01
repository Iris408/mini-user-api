import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

# EN: Database URL can come from environment variable
# JP: データベースURLは環境変数から取得可能
# KR: 데이터베이스 URL은 환경 변수에서 가져올 수 있음

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://amagloire@localhost:5432/mini_user_api_db"
)

if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)


# EN: Create database engine
# JP: データベースエンジン作成
# KR: 데이터베이스 엔진 생성

engine = create_engine(DATABASE_URL)


# EN: Create database session
# JP: データベースセッション作成
# KR: 데이터베이스 세션 생성

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# EN: Base class for database models
# JP: データベースモデル用ベースクラス
# KR: 데이터베이스 모델용 기본 클래스

Base = declarative_base()


# EN: Dependency for database session
# JP: データベースセッション用依存関係
# KR: 데이터베이스 세션용 의존성

def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
