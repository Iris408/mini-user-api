from pydantic import BaseModel


# EN: User request model
# JP: ユーザーリクエストモデル
# KR: 사용자 요청 모델

class UserRequest(BaseModel):
    name: str
    age: int
