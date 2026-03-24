from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from fastapi.responses import FileResponse
from auth.utils import get_current_user
from models.user import User
import os
import shutil
from pydantic import BaseModel

class RenameRequest(BaseModel):
    new_name: str

@router.put("/rename/{filename:path}")
def rename_file(
    filename: str,
    req: RenameRequest,
    current_user: User = Depends(get_current_user)
):
    user_dir = get_user_dir(current_user.username)
    old_path = os.path.join(user_dir, filename)
    new_path = os.path.join(os.path.dirname(old_path), req.new_name)

    if not os.path.exists(old_path):
        raise HTTPException(status_code=404, detail="파일을 찾을 수 없습니다")
    
    if os.path.exists(new_path):
        raise HTTPException(status_code=400, detail="이미 존재하는 이름입니다")
    
    os.rename(old_path, new_path)
    return {"message": f"{req.new_name}으로 변경 완료!"}

router = APIRouter(prefix="/files", tags=["files"])

BASE_DIR = "/nas/files"

def get_user_dir(username: str) -> str:
    user_dir = os.path.join(BASE_DIR, username)
    os.makedirs(user_dir, exist_ok=True)
    return user_dir

@router.get("/")
def list_files(
    path: str = "",
    current_user: User = Depends(get_current_user)
):
    user_dir = os.path.join(get_user_dir(current_user.username), path)
    files = []
    for filename in os.listdir(user_dir):
        filepath = os.path.join(user_dir, filename)
        stat = os.stat(filepath)
        files.append({
            "name": filename,
            "type": "folder" if os.path.isdir(filepath) else "file",
            "size_mb": round(stat.st_size / (1024**2), 2) if os.path.isfile(filepath) else None,
            "modified": stat.st_mtime
        })
    return {"files": files}

@router.post("/upload")
def upload_file(
    file: UploadFile = File(...),
    path: str = "",
    current_user: User = Depends(get_current_user)
):
    user_dir = os.path.join(get_user_dir(current_user.username), path)
    os.makedirs(user_dir, exist_ok=True)
    file_path = os.path.join(user_dir, file.filename)
    
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    
    return {"message": f"{file.filename} 업로드 완료!"}

@router.get("/download/{filename:path}")
def download_file(
    filename: str,
    current_user: User = Depends(get_current_user)
):
    user_dir = get_user_dir(current_user.username)
    file_path = os.path.join(user_dir, filename)
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="파일을 찾을 수 없습니다")
    
    return FileResponse(path=file_path, filename=filename)

@router.delete("/{filename:path}")
def delete_file(
    filename: str,
    current_user: User = Depends(get_current_user)
):
    user_dir = get_user_dir(current_user.username)
    file_path = os.path.join(user_dir, filename)
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="파일을 찾을 수 없습니다")
    
    if os.path.isdir(file_path):
        shutil.rmtree(file_path)  # 폴더 삭제
    else:
        os.remove(file_path)  # 파일 삭제
    
    return {"message": f"{filename} 삭제 완료!"}

@router.post("/mkdir")
def create_folder(
    folder_name: str,
    current_user: User = Depends(get_current_user)
):
    user_dir = get_user_dir(current_user.username)
    folder_path = os.path.join(user_dir, folder_name)
    
    if os.path.exists(folder_path):
        raise HTTPException(status_code=400, detail="이미 존재하는 폴더입니다")
    
    os.makedirs(folder_path)
    return {"message": f"{folder_name} 폴더 생성 완료!"}

