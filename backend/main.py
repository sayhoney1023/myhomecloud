from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auth.router import router as auth_router
from system.router import router as system_router
from files.router import router as files_router
from database.database import engine, Base
import models.user

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="MH Cloud API",
    description="MH Cloud 백엔드 API 서버",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://www.myhomecloud.kr"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(system_router)
app.include_router(files_router)

@app.get("/")
def read_root():
    return {"message": "MH Cloud API 서버입니다 🚀"}

@app.get("/health")
def health_check():
    return {"status": "ok"}