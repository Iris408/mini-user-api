import os

from dotenv import load_dotenv

load_dotenv()

# EN: Authentication utilities
# JP: 認証ユーティリティ
# KR: 인증 유틸리티

from passlib.context import CryptContext

# EN: Password hashing configuration
# JP: パスワードハッシュ設定
# KR: 비밀번호 해시 설정

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# EN: Hash password
# JP: パスワードハッシュ化
# KR: 비밀번호 해시화

def hash_password(password: str):

    return pwd_context.hash(password)

# EN: Verify password
# JP: パスワード確認
# KR: 비밀번호 확인

def verify_password(
    plain_password: str,
    hashed_password: str
):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )

from jose import jwt
from jose import JWTError

from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

# EN: JWT configuration
# JP: JWT 設定
# KR: JWT 설정

SECRET_KEY = os.getenv("SECRET_KEY")

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30


# EN: OAuth2 bearer token scheme
# JP: OAuth2 Bearer トークン方式
# KR: OAuth2 Bearer 토큰 방식

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)


# EN: Create JWT access token
# JP: JWT アクセストークン作成
# KR: JWT 액세스 토큰 생성

def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({
        "exp": expire
    })

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


# EN: Verify JWT token
# JP: JWT トークン確認
# KR: JWT 토큰 검증

def verify_token(token: str):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

        if username is None:
            return None

        return username

    except JWTError:

        return None


# EN: Get current authenticated user
# JP: 現在認証ユーザー取得
# KR: 현재 인증 사용자 조회

def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    username = verify_token(token)

    if username is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials"
        )

    return username
