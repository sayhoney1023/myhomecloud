from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from auth.utils import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

# 임시 유저 저장소 (나중에 DB로 교체할 거예요)
fake_db = {}

class RegisterRequest(BaseModel):
    username: str
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/register")
def register(req: RegisterRequest):
    if req.username in fake_db:
        raise HTTPException(status_code=400, detail="이미 존재하는 아이디입니다")
    
    fake_db[req.username] = hash_password(req.password)
    return {"message": f"{req.username}님 회원가입 완료!"}

@router.post("/login")
def login(req: LoginRequest):
    if req.username not in fake_db:
        raise HTTPException(status_code=401, detail="존재하지 않는 아이디입니다")
    
    if not verify_password(req.password, fake_db[req.username]):
        raise HTTPException(status_code=401, detail="비밀번호가 틀렸습니다")
    
    token = create_access_token({"sub": req.username})
    return {"access_token": token, "token_type": "bearer"}
    