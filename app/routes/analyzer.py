from app.models.analyzer_model import AnalyzeRequest

from fastapi import APIRouter
from app.services.math_service import get_number_type, square_number, multiply_number

router = APIRouter()


@router.get("/analyze_advanced")
def analyze_advanced(number: int, multiply: int = 1):
    number_type = get_number_type(number)

    return {
        "number": number,
        "square": square_number(number),
        "multiplied": multiply_number(number, multiply),
        "type": number_type
    }

@router.post("/analyze")
def analyze_post(request: AnalyzeRequest):
    number_type = get_number_type(request.number)

    return {
        "number": request.number,
        "square": square_number(request.number),
        "multiplied": multiply_number(request.number, request.multiply),
        "type": number_type
    }
