# ⬡ MH Cloud

> 개인 홈서버 기반 클라우드 포털 시스템  
> Proxmox + Docker + Cloudflare 로 구축한 완전 자체 호스팅 서비스

🌐 **[www.myhomecloud.kr](https://www.myhomecloud.kr)**
## 블로그
📝 [velog.io/@sayhoney1023](https://velog.io/@sayhoney1023)
---

## 서비스 현황

| 서비스 | 도메인 | 상태 | 설명 |
|--------|--------|------|------|
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
VM1 - Ubuntu Server (192.168.0.175)  |  RAM 6GB
├── mhcloud-portal    (port 3000)  ✅
├── mhcloud-backend   (port 8000)  🔨 개발 중 (FastAPI)
├── mhcloud-code      (port 8443)  ✅
├── nextcloud         (port 8080)  ✅ 임시
└── nginx-proxy-manager (port 81) ✅

VM2 - AI Server (192.168.0.117)  |  RAM 8GB · RTX 2060 Super GPU
├── mhcloud-ollama    (port 11434) ✅ GPU 모드
├── mhcloud-ai        (port 3000)  ✅ 임시
└── mhcloud-searxng   (port 8081)  ✅
```

**물리 서버:** Proxmox VE  
**하드웨어:** AMD Ryzen 5 3600 (6C/12T) · DDR4 16GB RAM · RTX 2060 Super (8GB VRAM)

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

### 백엔드 (직접 제작 🔨)
![Python](https://img.shields.io/badge/Python_3.14-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)

### 임시 사용 (추후 직접 제작으로 대체 예정)
![Nextcloud](https://img.shields.io/badge/Nextcloud-0082C9?style=flat-square&logo=nextcloud&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat-square&logoColor=white)

### 장기 개발 예정
![Flutter](https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white)

---

## 프로젝트 구조

```
myhomecloud/
├── frontend/                    # 포털 UI (직접 제작 ✅)
│   ├── index.html
│   ├── style.css
│   └── script.js
├── backend/                     # FastAPI API 서버 (개발 중 🔨)
│   ├── main.py                  # 앱 진입점
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── router.py            # 로그인·회원가입 API ✅
│   │   └── utils.py             # JWT·bcrypt 유틸 ✅
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py            # 환경 설정 ✅
│   ├── venv/                    # Python 가상환경 (git 제외)
│   └── requirements.txt
├── docker/
│   ├── portal/docker-compose.yml
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
| POST | `/auth/register` | 회원가입 | ✅ |
| POST | `/auth/login` | 로그인 (JWT 발급) | ✅ |

### 개발 예정
| Method | Endpoint | 설명 |
|--------|----------|------|
| GET | `/files` | 파일 목록 조회 |
| POST | `/files/upload` | 파일 업로드 |
| DELETE | `/files/{id}` | 파일 삭제 |
| POST | `/ai/chat` | AI 채팅 (Ollama 연동) |

---

## 개발 로드맵

### ✅ 완료
| 날짜 | 내용 |
|------|------|
| 2026.03 | 개발 환경 세팅 (VS Code + Git + GitHub) |
| 2026.03 | 포털 페이지 직접 제작 (HTML/CSS/JS) |
| 2026.03 | www.myhomecloud.kr 배포 및 연결 |
| 2026.03 | Code-Server 구축 (code.myhomecloud.kr) |
| 2026.03 | VM2 생성 및 AI 서버 구축 (Ollama + Open WebUI) |
| 2026.03 | ai.myhomecloud.kr 연결 완료 |
| 2026.03 | GPU 패스스루 완료 (RTX 2060 Super · CUDA 13.0) |
| 2026.03 | DeepSeek-R1:8b 모델 · SearXNG 웹 검색 연동 |
| 2026.03 | VM 메모리 재배분 (VM1 6GB · VM2 8GB) |
| 2026.03 | FastAPI 개발 환경 세팅 · 첫 API 서버 실행 |
| 2026.03 | JWT 회원가입 · 로그인 API 구현 (bcrypt 암호화) |

### 🔨 진행 예정
| 기간 | 내용 |
|------|------|
| 2026.04 | PostgreSQL DB 연동 (fake_db 교체) |
| 2026.04 | 파일 업로드 · 다운로드 API |
| 2026.05 | 포털 로그인 시스템 연동 |
| 2026.06 | Cloud UI 직접 제작 (Nextcloud 대체) |
| 2026.06 | AI 채팅 UI 직접 제작 (Open WebUI 대체) |
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

---

## Docker 컨테이너 현황

| 컨테이너 | 이미지 | VM | 포트 | 상태 |
|----------|--------|-----|------|------|
| mhcloud-portal | nginx:alpine | VM1 | 3000 | ✅ |
| mhcloud-backend | python/fastapi | VM1 | 8000 | 🔨 개발 중 |
| mhcloud-code | linuxserver/code-server | VM1 | 8443 | ✅ |
| nextcloud_app_1 | nextcloud | VM1 | 8080 | ✅ 임시 |
| nginx-proxy-manager | jc21/nginx-proxy-manager | VM1 | 80/81/443 | ✅ |
| nextcloud_db_1 | mariadb | VM1 | 3306 | ✅ |
| mhcloud-ollama | ollama/ollama | VM2 | 11434 | ✅ GPU |
| mhcloud-ai | open-webui | VM2 | 3000 | ✅ 임시 |
| mhcloud-searxng | searxng/searxng | VM2 | 8081 | ✅ |

---

## 변경 이력

### 2026-03-19
- ✅ JWT 회원가입 · 로그인 API 구현
- ✅ bcrypt 비밀번호 암호화 적용
- ✅ 프로젝트 구조 분리 (auth/ · core/)
- ✅ Swagger 문서 자동 생성 확인
- ✅ 에러 케이스 검증 (400 중복 아이디 · 401 비밀번호 틀림)

### 2026-03-18
- ✅ VM 메모리 재배분 (VM1 8GB→6GB · VM2 6GB→8GB)
- ✅ Ollama `KEEP_ALIVE=1m` 설정
- ✅ FastAPI 개발 환경 세팅 · 첫 API 서버 실행

### 2026-03-17
- ✅ GPU 패스스루 완료 (RTX 2060 Super)
- ✅ Ubuntu 24.04 UEFI 재설치
- ✅ NVIDIA Driver 580 + CUDA 13.0
- ✅ Docker + NVIDIA Container Toolkit
- ✅ Ollama GPU 모드 실행
- ✅ DeepSeek-R1:8b 모델 설치
- ✅ SearXNG 웹 검색 연동

---

## 개발자

**sayhoney1023**
- 컴퓨터공학과 3학년
- 개인 홈서버 직접 구축 · 풀스택 개발 학습 중
- 목표: 모든 서비스를 직접 제작하는 완전 자체 호스팅 플랫폼

---

> 이 프로젝트는 학습 목적으로 진행되는 개인 홈서버 프로젝트입니다.  
> 임시로 사용 중인 오픈소스 서비스들은 순차적으로 직접 제작한 서비스로 대체될 예정입니다.
