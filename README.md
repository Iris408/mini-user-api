# Mini User API / ミニユーザーAPI / 미니 사용자 API

A beginner-friendly backend CRUD API built with Python and FastAPI.

Python と FastAPI を使用して作成した初心者向けバックエンド CRUD API プロジェクトです。

Python 과 FastAPI를 사용해 만든 초보자용 백엔드 CRUD API 프로젝트입니다.

---

# Features / 機能 / 기능

## English
- Create users
- Get all users
- Get one user by ID
- Update users
- Delete users
- Analyze numbers
- JSON request bodies
- Modular project structure

## 日本語
- ユーザー作成
- 全ユーザー取得
- IDでユーザー取得
- ユーザー更新
- ユーザー削除
- 数値分析
- JSONリクエストボディ
- モジュール型プロジェクト構成

## 한국어
- 사용자 생성
- 모든 사용자 조회
- ID로 사용자 조회
- 사용자 수정
- 사용자 삭제
- 숫자 분석
- JSON 요청 본문
- 모듈형 프로젝트 구조

---

# Tech Stack / 技術スタック / 기술 스택

- Python
- FastAPI
- Pydantic
- Uvicorn

---

# Project Structure / プロジェクト構成 / 프로젝트 구조

```text
app/
├── main.py
├── routes/
│   ├── analyzer.py
│   └── user_routes.py
├── models/
│   ├── analyzer_model.py
│   └── user_model.py
└── services/
    ├── math_service.py
    └── user_service.py
