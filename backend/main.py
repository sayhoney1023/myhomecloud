from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from auth.router import router as auth_router
from system.router import router as system_router
from files.router import router as files_router
from database.database import engine, Base
import models.user

Base.metadata.create_all(bind=engine)

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(
    title="MH Cloud API",
    description="MH Cloud 백엔드 API 서버",
    version="0.1.0"
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://www.myhomecloud.kr",
                   "https://cloud.myhomecloud.kr"],
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
    