# ⬡ MH Cloud

> 개인 홈서버 기반 클라우드 포털 시스템  
> Proxmox + Docker + Cloudflare 로 구축한 완전 자체 호스팅 서비스

🌐 **[www.myhomecloud.kr](https://www.myhomecloud.kr)**  
⚙️ **[api.myhomecloud.kr](https://api.myhomecloud.kr)**

## 블로그
📝 [velog.io/@sayhoney1023](https://velog.io/@sayhoney1023)

---

## 서비스 현황

| 서비스 | 도메인 | 상태 | 설명 |
|--------|--------|------|------|
| 🌐 Portal | [www.myhomecloud.kr](https://www.myhomecloud.kr) | ✅ Online | 포털 (로그인 시스템 완성) |
| ⚙️ API | [api.myhomecloud.kr](https://api.myhomecloud.kr) | ✅ Online | FastAPI 백엔드 (JWT 인증) |
| ☁️ Cloud | [cloud.myhomecloud.kr](https://cloud.myhomecloud.kr) | ✅ Online | 파일 저장 · 공유 · 동기화 |
| 💻 Code | [code.myhomecloud.kr](https://code.myhomecloud.kr) | ✅ Online | 브라우저 기반 VS Code |
| 🤖 AI | [ai.myhomecloud.kr](https://ai.myhomecloud.kr) | ✅ Online | 로컬 AI 챗봇 (DeepSeek-R1:8b) |

> **임시 운영 중인 서비스**  
> Cloud(Nextcloud), AI(Open WebUI)는 오픈소스를 임시로 사용 중입니다.  
> 추후 백엔드 API + 프론트엔드를 직접 제작하여 완전히 대체할 예정입니다.

---

## 인프라 구조

```
인터넷
   ↓
Cloudflare (DDoS 보호 + SSL + IP 숨김)
   ↓
공유기 포트포워딩 (443)
   ↓
Nginx Proxy Manager (리버스 프록시)
   ↓
VM1 - Ubuntu Server  |  RAM 6GB
├── mhcloud-portal    (port 3000)  ✅ UI
├── mhcloud-backend   (port 8000)  ✅ FastAPI + PostgreSQL
├── mhcloud-postgres  (port 5432)  ✅ PostgreSQL DB
├── mhcloud-code      (port 8443)  ✅
├── nextcloud         (port 8080)  ✅ 임시
└── nginx-proxy-manager (port 81) ✅

VM2 - AI Server  |  RAM 8GB · RTX 2060 Super GPU
├── mhcloud-ollama    (port 11434) ✅ GPU 모드
├── mhcloud-ai        (port 3000)  ✅ 임시
└── mhcloud-searxng   (port 8081)  ✅
```

**물리 서버:** Proxmox VE  
**하드웨어:** AMD Ryzen 5 3600 (6C/12T) · DDR4 16GB RAM · RTX 2060 Super (8GB VRAM) · HDD 2TB

---

## 기술 스택

### 인프라
![Proxmox](https://img.shields.io/badge/Proxmox-E57000?style=flat-square&logo=proxmox&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=flat-square&logo=ubuntu&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white)
![Cloudflare](https://img.shields.io/badge/Cloudflare-F38020?style=flat-square&logo=cloudflare&logoColor=white)

### 프론트엔드 (직접 제작 ✅)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

### 백엔드 (직접 제작 ✅)
![Python](https://img.shields.io/badge/Python_3.11-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white)

### 임시 사용 (추후 직접 제작으로 대체 예정)
![Nextcloud](https://img.shields.io/badge/Nextcloud-0082C9?style=flat-square&logo=nextcloud&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat-square&logoColor=white)

### 장기 개발 예정
![Flutter](https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white)

---

## 프로젝트 구조

```
myhomecloud/
├── frontend/                    # 포털 UI
│   ├── index.html               # 메인 포털
│   ├── cloud.html               # 파일 매니저 UI ✅
│   ├── style.css                # 스타일시트
│   └── script.js                # JWT 인증 · 카드 잠금 · 자동 로그아웃
├── backend/                     # FastAPI API 서버 ✅
│   ├── main.py                  # 앱 진입점 · DB 테이블 자동 생성
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── router.py            # 로그인·회원가입·비밀번호 변경 API ✅
│   │   └── utils.py             # JWT·bcrypt·get_current_user 유틸 ✅
│   ├── system/
│   │   ├── __init__.py
│   │   └── router.py            # 서버 상태 API (psutil) ✅
│   ├── files/
│   │   ├── __init__.py
│   │   └── router.py            # 파일 API (업로드·다운로드·삭제·목록·폴더생성) ✅
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py            # 환경변수 설정 (SECRET_KEY 분리) ✅
│   ├── database/
│   │   ├── __init__.py
│   │   └── database.py          # SQLAlchemy 엔진 · 세션 ✅
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py              # User 테이블 모델 ✅
│   ├── Dockerfile
│   └── requirements.txt
├── docker/
│   ├── portal/
│   │   ├── docker-compose.yml
│   │   └── nginx.conf           # 캐시 방지 헤더
│   ├── backend/
│   │   ├── docker-compose.yml   # backend + postgres · /nas 마운트 ✅
│   │   └── .env                 # 환경변수 (git 제외) ✅
│   ├── code-server/docker-compose.yml
│   └── ai/docker-compose.yml
└── README.md
```

---

## 로컬 개발 환경 세팅

```bash
# 1. 저장소 클론
git clone https://github.com/sayhoney1023/myhomecloud.git
cd myhomecloud/backend

# 2. 가상환경 생성 및 활성화
python -m venv venv

# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# 3. 의존성 설치
pip install -r requirements.txt

# 4. 개발 서버 실행
uvicorn main:app --reload
```

| 주소 | 설명 |
|------|------|
| `http://localhost:8000` | API 루트 |
| `http://localhost:8000/health` | 헬스체크 |
| `http://localhost:8000/docs` | Swagger 자동 문서 |

---

## API 엔드포인트

### 현재 구현
| Method | Endpoint | 설명 | 상태 |
|--------|----------|------|------|
| GET | `/` | API 서버 상태 확인 | ✅ |
| GET | `/health` | 헬스체크 | ✅ |
| POST | `/auth/register` | 회원가입 (bcrypt 암호화) | ✅ |
| POST | `/auth/login` | 로그인 (JWT 발급) | ✅ |
| PUT | `/auth/password` | 비밀번호 변경 (JWT 인증 필요) | ✅ |
| GET | `/system/status` | 서버 상태 (CPU · RAM · 디스크) | ✅ |
| GET | `/files/` | 파일 목록 조회 (경로 탐색 지원) | ✅ |
| POST | `/files/upload` | 파일 업로드 (경로 지정 가능) | ✅ |
| GET | `/files/download/{filename:path}` | 파일 다운로드 | ✅ |
| DELETE | `/files/{filename:path}` | 파일 · 폴더 삭제 | ✅ |
| POST | `/files/mkdir` | 폴더 생성 | ✅ |

### 개발 예정
| Method | Endpoint | 설명 |
|--------|----------|------|
| POST | `/ai/chat` | AI 채팅 (Ollama 연동) |
| GET | `/files/share/{id}` | 파일 공유 링크 |

---

## 포털 기능

### 로그인 전
- 서비스 카드 🔒 잠금 표시
- 로그인 · 회원가입 모달 (탭 전환)
- 비밀번호 확인 기능

### 로그인 후
- 서비스 카드 언락 · 정상 클릭 가능
- 헤더에 `username님 👋` 드롭다운 메뉴
- 비밀번호 변경 모달 ✅
- 서버 상태 위젯 실시간 연동 30초 자동 새로고침 (디스크 % · CPU · RAM) ✅
- JWT 토큰 1시간 만료 · 자동 로그아웃

### 파일 매니저 (cloud.html) ✅
- 사용자별 독립 저장공간 (/nas/files/{username}/)
- 파일 업로드 (드래그 앤 드롭 지원)
- 파일 다운로드 · 삭제
- 폴더 생성 · 탐색 · 뒤로가기
- 브라우저 히스토리 연동 (뒤로가기 버튼)
- HDD 2TB 실제 저장공간 연동

---

## 개발 로드맵

### ✅ 완료
| 날짜 | 내용 |
|------|------|
| 2026.03.17 | 개발 환경 세팅 (VS Code + Git + GitHub) |
| 2026.03.17 | 포털 페이지 직접 제작 (HTML/CSS/JS) |
| 2026.03.17 | www.myhomecloud.kr 배포 및 연결 |
| 2026.03.17 | Code-Server 구축 (code.myhomecloud.kr) |
| 2026.03.17 | VM2 생성 및 AI 서버 구축 (Ollama + Open WebUI) |
| 2026.03.17 | GPU 패스스루 완료 (RTX 2060 Super · CUDA 13.0) |
| 2026.03.17 | DeepSeek-R1:8b 모델 · SearXNG 웹 검색 연동 |
| 2026.03.18 | VM 메모리 재배분 (VM1 6GB · VM2 8GB) |
| 2026.03.18 | FastAPI 개발 환경 세팅 · 첫 API 서버 실행 |
| 2026.03.19 | JWT 회원가입 · 로그인 API 구현 (bcrypt 암호화) |
| 2026.03.20 | PostgreSQL 연동 (SQLAlchemy ORM · fake_db 제거) |
| 2026.03.20 | VM1 백엔드 Docker 배포 완료 |
| 2026.03.20 | api.myhomecloud.kr 도메인 연결 |
| 2026.03.20 | 포털 로그인 · 회원가입 API 연동 완료 |
| 2026.03.20 | 카드 잠금 · 로그인 후 언락 · JWT 자동 로그아웃 |
| 2026.03.20 | 포털 UI 글래스모피즘 리디자인 |
| 2026.03.21 | 비밀번호 변경 API + 포털 모달 UI |
| 2026.03.21 | 서버 상태 API (psutil) + 위젯 실시간 연동 |
| 2026.03.22 | SECRET_KEY 환경변수 분리 (.env) |
| 2026.03.22 | HDD 2TB /nas 마운트 연동 |
| 2026.03.22 | 서버 상태 위젯 30초 자동 새로고침 |
| 2026.03.22 | 파일 API 완성 (업로드·다운로드·삭제·목록·폴더생성) |
| 2026.03.22 | 파일 매니저 UI (cloud.html) 제작 |
| 2026.03.22 | 폴더 탐색 · 현재 경로 업로드 · 뒤로가기 |

### 🔨 진행 예정
| 기간 | 내용 |
|------|------|
| 2026.04 | 파일 공유 링크 기능 |
| 2026.04 | AI 채팅 UI 직접 제작 (Open WebUI 대체) |
| 2026.05 | cloud.myhomecloud.kr → 직접 만든 파일 매니저로 교체 |
| 2026.06 | 서브도메인 구조 정리 |
| 2026.07 | 전체 통합 · 버그 수정 · 포트폴리오 정리 |

### 🔜 장기 계획
| 내용 |
|------|
| Flutter 모바일 앱 개발 |
| SSO 통합 로그인 시스템 |
| Kubernetes (K3s) 도입 |
| 사용자별 Code-Server (Replit 클론) |

---

## 보안 구조

| 레이어 | 기술 | 역할 |
|--------|------|------|
| 1 | Cloudflare | DDoS 보호 + IP 숨김 |
| 2 | HTTPS | SSL/TLS 암호화 |
| 3 | Nginx Proxy Manager | 리버스 프록시 |
| 4 | Proxmox VM 격리 | 가상화 보안 |
| 5 | JWT + bcrypt | API 인증 · 비밀번호 암호화 ✅ |
| 6 | CORS | 허용된 도메인만 API 접근 가능 ✅ |
| 7 | .env | SECRET_KEY · DB 비밀번호 환경변수 분리 ✅ |

---

## Docker 컨테이너 현황

| 컨테이너 | 이미지 | VM | 포트 | 상태 |
|----------|--------|-----|------|------|
| mhcloud-portal | nginx:alpine | VM1 | 3000 | ✅ |
| mhcloud-backend | python/fastapi | VM1 | 8000 | ✅ |
| mhcloud-postgres | postgres:16 | VM1 | 5432 | ✅ |
| mhcloud-code | linuxserver/code-server | VM1 | 8443 | ✅ |
| nextcloud_app_1 | nextcloud | VM1 | 8080 | ✅ 임시 |
| nginx-proxy-manager | jc21/nginx-proxy-manager | VM1 | 80/81/443 | ✅ |
| mhcloud-ollama | ollama/ollama | VM2 | 11434 | ✅ GPU |
| mhcloud-ai | open-webui | VM2 | 3000 | ✅ 임시 |
| mhcloud-searxng | searxng/searxng | VM2 | 8081 | ✅ |

---

## 변경 이력

### 2026-03-22
- ✅ SECRET_KEY · DATABASE_URL 환경변수 분리 (.env · docker-compose)
- ✅ HDD 2TB /nas 마운트 연동 (docker-compose volumes)
- ✅ 서버 상태 위젯 30초 자동 새로고침
- ✅ 파일 API 구현 (GET·POST·DELETE · 폴더생성 · 경로 탐색)
- ✅ /nas/files/{username}/ 사용자별 독립 저장공간
- ✅ 파일 매니저 UI 제작 (cloud.html · 글래스모피즘)
- ✅ 드래그 앤 드롭 업로드
- ✅ 폴더 탐색 · 현재 경로 업로드 · 삭제
- ✅ 브라우저 히스토리 연동 뒤로가기

### 2026-03-21
- ✅ 비밀번호 변경 API 구현 (PUT /auth/password)
- ✅ 포털 헤더 드롭다운 메뉴 · 비밀번호 변경 모달
- ✅ 서버 상태 API 구현 (GET /system/status · psutil)
- ✅ 포털 서버 상태 위젯 실시간 연동

### 2026-03-20
- ✅ PostgreSQL 연동 완료 (SQLAlchemy ORM)
- ✅ VM1 백엔드 Docker 배포 · api.myhomecloud.kr 연결
- ✅ 포털 로그인 · 회원가입 API 연동
- ✅ 포털 UI 글래스모피즘 리디자인

### 2026-03-19
- ✅ JWT 회원가입 · 로그인 API 구현
- ✅ bcrypt 비밀번호 암호화

### 2026-03-18
- ✅ VM 메모리 재배분 · FastAPI 개발 환경 세팅

### 2026-03-17
- ✅ GPU 패스스루 · Ollama · DeepSeek-R1:8b · SearXNG

---

## 개발자

**sayhoney1023**
- 컴퓨터공학과 3학년
- 개인 홈서버 직접 구축 · 풀스택 개발 학습 중
- 목표: 모든 서비스를 직접 제작하는 완전 자체 호스팅 플랫폼

---

> 이 프로젝트는 학습 목적으로 진행되는 개인 홈서버 프로젝트입니다.  
> 임시로 사용 중인 오픈소스 서비스들은 순차적으로 직접 제작한 서비스로 대체될 예정입니다.
