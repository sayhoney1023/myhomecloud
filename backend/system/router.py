from fastapi import APIRouter, Depends
from auth.utils import get_current_user
from models.user import User
import psutil
import shutil

router = APIRouter(prefix="/system", tags=["system"])

@router.get("/status")
def get_status(current_user: User = Depends(get_current_user)):
    # 디스크 (호스트 마운트)
    try:
        disk = shutil.disk_usage("/nas")
        disk_percent = round(disk.used / disk.total * 100, 1)
        disk_used_gb = round(disk.used / (1024**3), 1)
        disk_total_gb = round(disk.total / (1024**3), 1)
    except:
        disk_percent = 0
        disk_used_gb = 0
        disk_total_gb = 0

    # CPU · RAM (컨테이너 기준)
    cpu_percent = psutil.cpu_percent(interval=0.5)
    ram = psutil.virtual_memory()

    return {
        "disk": {
            "percent": disk_percent,
            "used_gb": disk_used_gb,
            "total_gb": disk_total_gb
        },
        "cpu": {
            "percent": cpu_percent
        },
        "ram": {
            "percent": ram.percent,
            "used_gb": round(ram.used / (1024**3), 1),
            "total_gb": round(ram.total / (1024**3), 1)
        }
    }