# EN: Python base image
# JP: Python ベースイメージ
# KR: Python 베이스 이미지

FROM python:3.13

# EN: Working directory
# JP: 作業ディレクトリ
# KR: 작업 디렉토리

WORKDIR /app

# EN: Copy requirements
# JP: requirements コピー
# KR: requirements 복사

COPY requirements.txt .

# EN: Install dependencies
# JP: 依存関係インストール
# KR: 의존성 설치

RUN pip install --no-cache-dir -r requirements.txt

# EN: Copy project files
# JP: プロジェクトファイルコピー
# KR: 프로젝트 파일 복사

COPY . .

# EN: Start FastAPI server
# JP: FastAPI サーバー起動
# KR: FastAPI 서버 시작

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8002"]
