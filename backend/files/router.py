from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from fastapi.responses import FileResponse
from auth.utils import get_current_user
from models.user import User
import os
import shutil

router = APIRouter(prefix="/files", tags=["files"])

BASE_DIR = "/host/nas/files"

def get_user_dir(username: str) -> str:
    user_dir = os.path.join(BASE_DIR, username)
    os.makedirs(user_dir, exist_ok=True)
    return user_dir

@router.get("/")
def list_files(current_user: User = Depends(get_current_user)):
    user_dir = get_user_dir(current_user.username)
    files = []
    for filename in os.listdir(user_dir):
        filepath = os.path.join(user_dir, filename)
        stat = os.stat(filepath)
        files.append({
            "name": filename,
            "size_mb": round(stat.st_size / (1024**2), 2),
            "modified": stat.st_mtime
        })
    return {"files": files}

@router.post("/upload")
def upload_file(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user)
):
    user_dir = get_user_dir(current_user.username)
    file_path = os.path.join(user_dir, file.filename)
    
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    
    return {"message": f"{file.filename} 업로드 완료!"}

@router.get("/download/{filename}")
def download_file(
    filename: str,
    current_user: User = Depends(get_current_user)
):
    user_dir = get_user_dir(current_user.username)
    file_path = os.path.join(user_dir, filename)
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="파일을 찾을 수 없습니다")
    
    return FileResponse(path=file_path, filename=filename)

@router.delete("/{filename}")
def delete_file(
    filename: str,
    current_user: User = Depends(get_current_user)
):
    user_dir = get_user_dir(current_user.username)
    file_path = os.path.join(user_dir, filename)
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="파일을 찾을 수 없습니다")
    
    os.remove(file_path)
    return {"message": f"{filename} 삭제 완료!"}
    