# ⬡ MH Cloud

> 개인 홈서버 기반 클라우드 포털 시스템  
> Proxmox + Docker + Cloudflare 로 구축한 완전 자체 호스팅 서비스

🌐 **[www.myhomecloud.kr](https://www.myhomecloud.kr)**

---

##  서비스 현황

| 서비스 | 도메인 | 상태 | 설명 |
|--------|--------|------|------|
| ☁️ Cloud | [cloud.myhomecloud.kr](https://cloud.myhomecloud.kr) | ✅ Online | 파일 저장 · 공유 · 동기화 |
| 💻 Code | [code.myhomecloud.kr](https://code.myhomecloud.kr) | ✅ Online | 브라우저 기반 VS Code |
| 🤖 AI | [ai.myhomecloud.kr](https://ai.myhomecloud.kr) | ✅ Online | 로컬 AI 챗봇 (DeepSeek-R1) |

>  **임시 운영 중인 서비스**  
> Cloud(Nextcloud), AI(Open WebUI)는 오픈소스를 임시로 사용 중입니다.  
> 추후 백엔드 API + 프론트엔드를 직접 제작하여 완전히 대체할 예정입니다.

---
## 🏗️ 인프라 구조

    인터넷
       ↓
    Cloudflare (DDoS 보호 + SSL + IP 숨김)
       ↓
    공유기 포트포워딩 (443)
       ↓
    Nginx Proxy Manager (리버스 프록시)
       ↓
    VM1 - Ubuntu Server (192.168.0.175)
    ├── mhcloud-portal    (port 3000)  ✅
    ├── mhcloud-code      (port 8443)  ✅
    ├── nextcloud         (port 8080)  ✅ 임시
    └── nginx-proxy-manager (port 81) ✅
    
    VM2 - AI Server (192.168.0.116)
    ├── mhcloud-ollama    (port 11434) ✅ 임시
    └── mhcloud-ai        (port 3000)  ✅ 임시

**물리 서버:** Proxmox VE  
**하드웨어:** AMD Ryzen 5 3600 (6C/12T) · DDR4 16GB RAM · RTX 2060 Super (8GB VRAM)


---

##  기술 스택

### 인프라
![Proxmox](https://img.shields.io/badge/Proxmox-E57000?style=flat-square&logo=proxmox&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=flat-square&logo=ubuntu&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white)
![Cloudflare](https://img.shields.io/badge/Cloudflare-F38020?style=flat-square&logo=cloudflare&logoColor=white)

### 프론트엔드 (직접 제작)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

### 임시 사용 (추후 직접 제작으로 대체 예정)
![Nextcloud](https://img.shields.io/badge/Nextcloud-0082C9?style=flat-square&logo=nextcloud&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat-square&logoColor=white)

### 개발 예정
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Flutter](https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white)

---

##  프로젝트 구조

    myhomecloud/
    ├── frontend/                    # 포털 UI (직접 제작 ✅)
    │   ├── index.html
    │   ├── style.css
    │   └── script.js
    ├── backend/                     # API 서버 (개발 예정 🔨)
    ├── docker/
    │   ├── portal/
    │   │   └── docker-compose.yml   # 포털 컨테이너 ✅
    │   ├── code-server/
    │   │   └── docker-compose.yml   # Code-Server ✅
    │   └── ai/
    │       └── docker-compose.yml   # Ollama + Open WebUI ✅
    └── README.md
---

##  개발 로드맵

### ✅ 완료
| 날짜 | 내용 |
|------|------|
| 2026.03 | 개발 환경 세팅 (VS Code + Git + GitHub) |
| 2026.03 | 포털 페이지 직접 제작 (HTML/CSS/JS) |
| 2026.03 | www.myhomecloud.kr 배포 및 연결 |
| 2026.03 | Code-Server 구축 (code.myhomecloud.kr) |
| 2026.03 | VM2 생성 및 AI 서버 구축 (Ollama + Open WebUI) |
| 2026.03 | ai.myhomecloud.kr 연결 완료 |

### 🔨 진행 예정
| 기간 | 내용 |
|------|------|
| 2026.04 | **FastAPI 백엔드 개발 시작** |
| 2026.04 | 파일 업로드 / 다운로드 API |
| 2026.04 | SQLite → PostgreSQL DB 연동 |
| 2026.05 | 로그인 / 회원가입 API (JWT 인증) |
| 2026.05 | 포털 로그인 시스템 연동 |
| 2026.06 | **클라우드 파일 서버 UI 직접 제작** (Nextcloud 대체) |
| 2026.06 | **AI 채팅 UI 직접 제작** (Open WebUI 대체, Ollama API 연동) |
| 2026.07 | 전체 통합 · 버그 수정 · 포트폴리오 정리 |

### 🔜 장기 계획
| 내용 |
|------|
| Kubernetes (K3s) 도입 |
| Flutter 모바일 앱 개발 |
| SSO 통합 로그인 시스템 |
| GPU 패스스루 (RTX 2060 Super) |
| 사용자별 Code-Server (Replit 클론) |

---

##  보안 구조

| 레이어 | 기술 | 역할 |
|--------|------|------|
| 1 | Cloudflare | DDoS 보호 + IP 숨김 |
| 2 | HTTPS | SSL/TLS 암호화 |
| 3 | Nginx Proxy Manager | 리버스 프록시 |
| 4 | Proxmox VM 격리 | 가상화 보안 |
| 5 | Code-Server 비밀번호 | 코드 서버 접근 제어 |

---

##  Docker 컨테이너 현황

| 컨테이너 | 이미지 | VM | 포트 | 상태 |
|----------|--------|-----|------|------|
| mhcloud-portal | nginx:alpine | VM1 | 3000 | ✅ |
| mhcloud-code | linuxserver/code-server | VM1 | 8443 | ✅ |
| nextcloud_app_1 | nextcloud | VM1 | 8080 | ✅ (임시) |
| nginx-proxy-manager | jc21/nginx-proxy-manager | VM1 | 80/81/443 | ✅ |
| nextcloud_db_1 | mariadb | VM1 | 3306 | ✅ |
| mhcloud-ollama | ollama/ollama | VM2 | 11434 | ✅ |
| mhcloud-ai | open-webui | VM2 | 3000 | ✅ |
| mhcloud-ollama | ollama/ollama | VM2 | 11434 | ✅ GPU |
| mhcloud-searxng | searxng/searxng | VM2 | 8081 | ✅ |

---

### 2026-03-17
- ✅ GPU 패스스루 완료 (RTX 2060 Super)
- ✅ Ubuntu 24.04 UEFI 재설치
- ✅ NVIDIA Driver 580 + CUDA 13.0
- ✅ Docker + NVIDIA Container Toolkit
- ✅ Ollama GPU 모드 실행
- ✅ DeepSeek-R1:8b 모델 설치
- ✅ SearXNG 웹 검색 연동
- ✅ MH Cloud AI 이름 설정

---

##  개발자

**sayhoney1023**
- 컴퓨터공학과 3학년
- 개인 홈서버 직접 구축 · 풀스택 개발 학습 중
- 목표 : 모든 서비스를 직접 제작하는 완전 자체 호스팅 플랫폼

---

> 이 프로젝트는 학습 목적으로 진행되는 개인 홈서버 프로젝트입니다.  
> 임시로 사용 중인 오픈소스 서비스들은 순차적으로 직접 제작한 서비스로 대체될 예정입니다.