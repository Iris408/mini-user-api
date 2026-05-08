from pydantic import BaseModel


class AnalyzeRequest(BaseModel):
    number: int
    multiply: int = 1
