from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database.database import get_db
from models.user import User
from auth.utils import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

class RegisterRequest(BaseModel):
    username: str
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/register")
def register(req: RegisterRequest, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == req.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="이미 존재하는 아이디입니다")
    
    new_user = User(
        username=req.username,
        hashed_password=hash_password(req.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": f"{req.username}님 회원가입 완료!"}

@router.post("/login")
def login(req: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == req.username).first()
    if not user:
        raise HTTPException(status_code=401, detail="존재하지 않는 아이디입니다")
    
    if not verify_password(req.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="비밀번호가 틀렸습니다")
    
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
    