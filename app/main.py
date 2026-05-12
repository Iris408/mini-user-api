from fastapi import FastAPI
from app.routes.analyzer import router as analyzer_router
from app.routes.user_routes import router as user_router
from app.database import engine, Base
from app.models.user_model import User

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(analyzer_router)
app.include_router(user_router)


@app.get("/")
def home():
    return {"message": "Backend project is structured!"}
