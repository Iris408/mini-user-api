from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base
from app.models.user_model import User
from app.routes.user_routes import router as user_router


app = FastAPI()

# EN: Allow frontend apps to call this backend API
# JP: フロントエンドアプリがこのバックエンドAPIを呼び出せるようにする

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://jwt-authentication-dashboard-sepia.vercel.app/"
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
def home():
    return {"message": "Backend project is structured!"}
