import os

from dotenv import load_dotenv
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext


load_dotenv()


# =========================================
# EN: OAuth2 token scheme for protected routes
# JP: 保護ルート用 OAuth2 トークンスキーム
# KR: 보호된 라우트용 OAuth2 토큰 스키마
# =========================================

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token"
)


# =========================================
# EN: Authentication utilities
# JP: 認証ユーティリティ
# KR: 인증 유틸리티
# =========================================

from passlib.context import CryptContext


# =========================================
# EN: Password hashing configuration
# JP: パスワードハッシュ設定
# KR: 비밀번호 해시 설정
# =========================================

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# =========================================
# EN: Hash password
# JP: パスワードハッシュ化
# KR: 비밀번호 해시화
# =========================================

def hash_password(password: str):

    return pwd_context.hash(password)


# =========================================
# EN: Verify password
# JP: パスワード確認
# KR: 비밀번호 확인
# =========================================

def verify_password(
    plain_password: str,
    hashed_password: str
):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )


# =========================================
# EN: JWT configuration
# JP: JWT 設定
# KR: JWT 설정
# =========================================

SECRET_KEY = "temporary_secret_key_change_later"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# =========================================
# EN: Create JWT access token
# JP: JWT アクセストークン作成
# KR: JWT 액세스 토큰 생성
# =========================================

def create_access_token(data: dict):

    token_data = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    token_data.update(
        {
            "exp": expire
        }
    )

    encoded_jwt = jwt.encode(
        token_data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


# =========================================
# EN: Verify JWT token
# JP: JWT トークン確認
# KR: JWT 토큰 검증
# =========================================

def verify_token(token: str):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")
        role = payload.get("role")

        if username is None:
            return None

        return {
            "username": username,
            "role": role
        }

    except JWTError:
        return None


# =========================================
# EN: Get current authenticated user
# JP: 現在認証ユーザー取得
# KR: 현재 인증 사용자 조회
# =========================================

def get_current_user(token: str = Depends(oauth2_scheme)):

    user_data = verify_token(token)

    if user_data is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

    return user_data


# =========================================
# EN: Admin permission checker
# JP: 管理者権限確認
# KR: 관리자 권한 확인
# =========================================

def require_admin(current_user = Depends(get_current_user)):

    if current_user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return current_user
