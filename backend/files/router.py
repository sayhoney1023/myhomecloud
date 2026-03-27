from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from fastapi.responses import FileResponse
from auth.utils import get_current_user
from models.user import User
import os
import shutil
from pydantic import BaseModel


router = APIRouter(prefix="/files", tags=["files"])

BASE_DIR = "/nas/files"

# 파일 보기 

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
        if filename == '.trash': 
            continue #휴지통 파일은 안보이게 설정
        filepath = os.path.join(user_dir, filename)
        stat = os.stat(filepath)
        files.append({
            "name": filename,
            "type": "folder" if os.path.isdir(filepath) else "file",
            "size_mb": round(stat.st_size / (1024**2), 2) if os.path.isfile(filepath) else None,
            "modified": stat.st_mtime
        })
    return {"files": files}

#업로드

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

#다운로드

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

#폴더 생성 

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

#파일 이름 변경

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

#파일 이동

class MoveRequest(BaseModel):
    dest_path: str

@router.put("/move/{filename:path}")
def move_file(
    filename: str,
    req: MoveRequest,
    current_user: User = Depends(get_current_user)
):
    user_dir = get_user_dir(current_user.username)
    old_path = os.path.join(user_dir, filename)
    new_path = os.path.join(user_dir, req.dest_path, os.path.basename(filename))

    if not os.path.exists(old_path):
        raise HTTPException(status_code=404, detail="파일을 찾을 수 없습니다")
    
    if os.path.exists(new_path):
        raise HTTPException(status_code=400, detail="이미 존재하는 파일입니다")

    os.makedirs(os.path.dirname(new_path), exist_ok=True)
    shutil.move(old_path, new_path)
    return {"message": f"{req.dest_path}로 이동 완료!"}

#최근 항목 불러오기

@router.get("/recent")
def get_recent_files(
    limit: int = 20,
    current_user: User = Depends(get_current_user)
):
    user_dir = get_user_dir(current_user.username)
    files = []
    
    for root, dirs, filenames in os.walk(user_dir):
        for filename in filenames:
            filepath = os.path.join(root, filename)
            stat = os.stat(filepath)
            rel_path = os.path.relpath(filepath, user_dir)
            files.append({
                "name": filename,
                "path": rel_path,
                "type": "file",
                "size_mb": round(stat.st_size / (1024**2), 2),
                "modified": stat.st_mtime
            })
    
    files.sort(key=lambda x: x['modified'], reverse=True)
    return {"files": files[:limit]}

#휴지통 기능 + 삭제 로직

TRASH_DIR = ".trash"

@router.delete("/{filename:path}")
def delete_file(
    filename: str,
    current_user: User = Depends(get_current_user)
):
    user_dir = get_user_dir(current_user.username)
    file_path = os.path.join(user_dir, filename)
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="파일을 찾을 수 없습니다")
    
    # 휴지통으로 이동
    trash_dir = os.path.join(user_dir, TRASH_DIR)
    os.makedirs(trash_dir, exist_ok=True)
    trash_path = os.path.join(trash_dir, os.path.basename(file_path))
    
    # 같은 이름 있으면 타임스탬프 추가
    if os.path.exists(trash_path):
        import time
        base, ext = os.path.splitext(os.path.basename(file_path))
        trash_path = os.path.join(trash_dir, f"{base}_{int(time.time())}{ext}")
    
    shutil.move(file_path, trash_path)
    return {"message": f"{filename} 휴지통으로 이동했습니다"}


@router.get("/trash")
def get_trash(current_user: User = Depends(get_current_user)):
    user_dir = get_user_dir(current_user.username)
    trash_dir = os.path.join(user_dir, TRASH_DIR)
    os.makedirs(trash_dir, exist_ok=True)
    
    items = []
    for name in os.listdir(trash_dir):
        filepath = os.path.join(trash_dir, name)
        stat = os.stat(filepath)
        items.append({
            "name": name,
            "type": "folder" if os.path.isdir(filepath) else "file",
            "size_mb": round(stat.st_size / (1024**2), 2) if os.path.isfile(filepath) else None,
            "modified": stat.st_mtime
        })
    return {"files": items}


@router.post("/trash/restore/{filename}")
def restore_file(
    filename: str,
    current_user: User = Depends(get_current_user)
):
    user_dir = get_user_dir(current_user.username)
    trash_path = os.path.join(user_dir, TRASH_DIR, filename)
    restore_path = os.path.join(user_dir, filename)
    
    if not os.path.exists(trash_path):
        raise HTTPException(status_code=404, detail="파일을 찾을 수 없습니다")
    
    if os.path.exists(restore_path):
        raise HTTPException(status_code=400, detail="같은 이름의 파일이 이미 있습니다")
    
    shutil.move(trash_path, restore_path)
    return {"message": f"{filename} 복원 완료!"}


@router.delete("/trash/{filename}")
def delete_permanently(
    filename: str,
    current_user: User = Depends(get_current_user)
):
    user_dir = get_user_dir(current_user.username)
    trash_path = os.path.join(user_dir, TRASH_DIR, filename)
    
    if not os.path.exists(trash_path):
        raise HTTPException(status_code=404, detail="파일을 찾을 수 없습니다")
    
    if os.path.isdir(trash_path):
        shutil.rmtree(trash_path)
    else:
        os.remove(trash_path)
    return {"message": f"{filename} 영구 삭제 완료!"}