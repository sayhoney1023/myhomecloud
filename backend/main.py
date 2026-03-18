from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "MH Cloud API 서버입니다 🚀"}

@app.get("/health")
def health_check():
    return {"status": "ok"}