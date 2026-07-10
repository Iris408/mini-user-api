from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base, get_db
from app.models.user_model import User
from app.routes.user_routes import router as user_router

from sqlalchemy import text
from sqlalchemy.orm import Session


app = FastAPI()

# EN: Allow frontend apps to call this backend API
# JP: フロントエンドアプリがこのバックエンドAPIを呼び出せるようにする

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://jwt-authentication-dashboard-sepia.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(user_router)

@app.get("/")
def root():
    return {
        "message": "Mini User API is running",
        "status": "ok",
        "docs": "/docs"
    }

@app.get("/health")
def health_check():
    return {
        "status": "ok", 
        "service": "mini-user-api"
    }

@app.get("/ready")
def readiness_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {
            "status": "ready",
            "database": "connected",
            "service": "mini-user-api"
        }
    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Database unavailable"
        )
