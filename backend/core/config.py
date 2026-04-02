import os
import warnings

SECRET_KEY = os.getenv("SECRET_KEY", "fallback-dev-key")
if SECRET_KEY == "fallback-dev-key":
    warnings.warn("SECRET_KEY가 설정되지 않았습니다. 프로덕션 환경에서는 반드시 환경변수로 설정하세요.", stacklevel=2)

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://mhcloud:mhcloud1234@mhcloud-postgres:5432/mhclouddb")

ALLOW_REGISTRATION = os.getenv("ALLOW_REGISTRATION", "false").lower() == "true"
