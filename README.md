# ⬡ MH Cloud

> 개인 홈서버 기반 클라우드 포털 시스템
> Proxmox + Docker + Cloudflare 로 구축한 자체 호스팅 서비스

🌐 **[www.myhomecloud.kr](https://www.myhomecloud.kr)**

---

##  서비스

| 서비스 | 도메인 | 상태 | 설명 |
|--------|--------|------|------|
| ☁️ Cloud | [cloud.myhomecloud.kr](https://cloud.myhomecloud.kr) | ✅ Online | 파일 저장 · 공유 · 동기화 |
| 💻 Code | [code.myhomecloud.kr](https://code.myhomecloud.kr) | ✅ Online | 브라우저에서 바로 코딩 |
| 🤖 AI | [ai.myhomecloud.kr](https://ai.myhomecloud.kr) | 🔨 Coming Soon | 로컬 AI 챗봇 서비스 |

---

##  인프라 구조

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
┌─────────────────────────────────────┐
│  mhcloud-portal   (port 3000)       │
│  mhcloud-code     (port 8443)       │
│  Nextcloud        (port 8080)       │
│  nginx-proxy-manager  (port 81)     │
└─────────────────────────────────────┘
```

---

##  기술 스택

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

##  프로젝트 구조

```
myhomecloud/
├── frontend/
│   ├── index.html              # 메인 포털 페이지
│   ├── style.css               # 스타일
│   └── script.js               # 동작
├── backend/                    # API 서버 (개발 예정)
├── docker/
│   ├── portal/
│   │   └── docker-compose.yml  # 포털 컨테이너 (nginx)
│   └── code-server/
│       └── docker-compose.yml  # Code-Server 컨테이너
└── README.md
```

---

##  작업 일지

### 2026년 3월 17일

#### 환경 세팅
- VS Code + Git 개발 환경 구성
- GitHub 저장소 생성 및 로컬 클론
- 프로젝트 폴더 구조 세팅 (`frontend` / `backend` / `docker`)

#### 포털 페이지 제작
- HTML / CSS / JS 로 포털 메인 페이지 제작
- 다크 모드 미니멀 디자인 적용
- 서비스 카드 3개 구성 (Cloud / Code / AI)
- 로그인 모달 UI 구현
- Live Server 로 로컬 테스트 완료

#### 서버 배포
- Ubuntu VM 에 GitHub 저장소 클론
- `nginx:alpine` Docker 컨테이너로 포털 서빙
- `docker-compose.yml` 작성 및 실행
- Nginx Proxy Manager 에서 `www.myhomecloud.kr` 연결
- Cloudflare DNS A 레코드 추가 (`www` / `@` / `ai`)
- `https://www.myhomecloud.kr` 실제 접속 성공 🎉

#### Code-Server 구축
- `lscr.io/linuxserver/code-server` Docker 이미지 사용
- 비밀번호 인증 설정
- `8443` 포트로 컨테이너 실행
- Nginx Proxy Manager 에서 `code.myhomecloud.kr` 연결
- PC / 아이패드 브라우저에서 VS Code 접속 성공 🎉

#### Git 트러블슈팅
- VM 로컬 파일과 GitHub 파일 충돌 해결
- `.bak` 백업 후 `git pull` 정상화
- Git 작업 순서 확립
  - Windows에서 작성 → push → VM에서 pull

---

## 🗓️ 개발 로드맵

| 기간 | 내용 | 상태 |
|------|------|------|
| 2026.03.14 | 개발 환경 세팅 | ✅ 완료 |
| 2026.03.16 | 포털 페이지 제작 및 배포 | ✅ 완료 |
| 2026.03.16 | www.myhomecloud.kr 연결 | ✅ 완료 |
| 2026.03.17 | Code-Server 구축 | ✅ 완료 |
| 2026.04. ~ | 백엔드 API 개발 (FastAPI) | 🔨 예정 |
| 2026.04. ~ | 파일 서버 직접 제작 | 🔨 예정 |
| 2026.05. ~ | 로그인 / 인증 시스템 (JWT) | 🔨 예정 |
| 2026.06. ~ | AI 서버 구축 (Ollama) | 🔨 예정 |
| 2026.07. ~ | 전체 통합 및 마무리 | 🔨 예정 |
| 2026.08. ~ | Kubernetes 도입 | 🔜 미정 |
| 2026.08. ~ | Flutter 모바일 앱 | 🔜 미정 |
| 미정 | SSO 통합 로그인 | 🔜 미정 |
| 미정 | 사용자별 Code-Server (Replit 클론) | 🔜 미정 |

---

##  보안 구조

| 레이어 | 기술 | 역할 |
|--------|------|------|
| 1 | Cloudflare | DDoS 보호 + IP 숨김 |
| 2 | HTTPS | SSL/TLS 암호화 |
| 3 | Nginx Proxy Manager | 리버스 프록시 |
| 4 | Proxmox VM | 가상화 격리 |
| 5 | Code-Server 비밀번호 | 코드 서버 접근 제어 |

---

##  Docker 컨테이너 현황

| 컨테이너 | 이미지 | 포트 | 상태 |
|----------|--------|------|------|
| mhcloud-portal | nginx:alpine | 3000 | ✅ 운영중 |
| mhcloud-code | linuxserver/code-server | 8443 | ✅ 운영중 |
| nextcloud_app_1 | nextcloud | 8080 | ✅ 운영중 |
| nginx-proxy-manager | jc21/nginx-proxy-manager | 80/81/443 | ✅ 운영중 |
| nextcloud_db_1 | mariadb | 3306 | ✅ 운영중 |

---

##  개발자

**sayhoney1023**
- 컴퓨터공학과 3학년
- 개인 홈서버 구축 및 풀스택 개발 학습 중
- 목표 : 모든 서비스를 직접 제작하는 완전 자체 호스팅 플랫폼

---

> 이 프로젝트는 학습 목적으로 진행되는 개인 홈서버 프로젝트입니다.