from fastapi import FastAPI
from auth.router import router as auth_router

app = FastAPI(
    title="MH Cloud API",
    description="MH Cloud 백엔드 API 서버",
    version="0.1.0"
)

app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"message": "MH Cloud API 서버입니다 🚀"}

@app.get("/health")
def health_check():
    return {"status": "ok"}