# ⬡ MH Cloud

> 개인 홈서버 기반 클라우드 포털 시스템  
> Proxmox + Docker + Cloudflare 로 구축한 자체 호스팅 서비스

🌐 **[www.myhomecloud.kr](https://www.myhomecloud.kr)**

---

## 🖥️ 서비스

| 서비스 | 도메인 | 상태 | 설명 |
|--------|--------|------|------|
| ☁️ Cloud | [cloud.myhomecloud.kr](https://cloud.myhomecloud.kr) | ✅ Online | 파일 저장 · 공유 · 동기화 |
| 💻 Code | [code.myhomecloud.kr](https://code.myhomecloud.kr) | 🔨 Coming Soon | 브라우저에서 바로 코딩 |
| 🤖 AI | [ai.myhomecloud.kr](https://ai.myhomecloud.kr) | 🔨 Coming Soon | 로컬 AI 챗봇 서비스 |

---

## 🏗️ 인프라 구조

```
인터넷
   ↓
Cloudflare (도메인 보호 + SSL)
   ↓
공유기 포트포워딩 (443)
   ↓
Nginx Proxy Manager
   ↓
Ubuntu Server VM (Docker)
   ↓
┌─────────────────────────────────┐
│  mhcloud-portal   (port 3000)   │
│  Nextcloud        (port 8080)   │
│  nginx-proxy-manager            │
└─────────────────────────────────┘
```

---

## 🛠️ 기술 스택

### 인프라
![Proxmox](https://img.shields.io/badge/Proxmox-E57000?style=flat-square&logo=proxmox&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=flat-square&logo=ubuntu&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white)
![Cloudflare](https://img.shields.io/badge/Cloudflare-F38020?style=flat-square&logo=cloudflare&logoColor=white)

### 프론트엔드
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

### 예정
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Flutter](https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white)

---

## 📁 프로젝트 구조

```
myhomecloud/
├── frontend/
│   ├── index.html          # 메인 페이지
│   ├── style.css           # 스타일
│   └── script.js           # 동작
├── backend/                # API 서버 (개발 예정)
├── docker/
│   └── portal/
│       └── docker-compose.yml
└── README.md
```

---

## 🗓️ 개발 로드맵

| 기간 | 내용 | 상태 |
|------|------|------|
| 2026.03 | 포털 페이지 제작 및 배포 | ✅ 완료 |
| 2026.03 | www.myhomecloud.kr 연결 | ✅ 완료 |
| 2026.04 | 백엔드 API 개발 (FastAPI) | 🔨 예정 |
| 2026.05 | 로그인 / 인증 시스템 | 🔨 예정 |
| 2026.06 | Code-Server 구축 | 🔨 예정 |
| 2026.06 | AI 서버 구축 (Ollama) | 🔨 예정 |
| 2026.07 | 전체 통합 및 마무리 | 🔨 예정 |
| 2026.08~ | Kubernetes 도입 | 🔜 미정 |
| 2026.08~ | Flutter 모바일 앱 | 🔜 미정 |

---

## 🔒 보안 구조

| 레이어 | 기술 | 역할 |
|--------|------|------|
| 1 | Cloudflare | DDoS 보호 + IP 숨김 |
| 2 | HTTPS | SSL/TLS 암호화 |
| 3 | Nginx Proxy Manager | 리버스 프록시 |
| 4 | Proxmox VM | 가상화 격리 |

---

## 👨‍💻 개발자

**sayhoney1023**
- 소프트웨어공학과 3학년
- 개인 홈서버 구축 및 풀스택 개발 학습 중

---

> 학습 목적으로 진행되는 개인 홈서버 구축 프로젝트.
