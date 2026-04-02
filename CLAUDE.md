# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

### Backend (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate          # macOS/Linux
venv\Scripts\activate             # Windows
pip install -r requirements.txt
uvicorn main:app --reload         # dev server at http://localhost:8000
```

- Swagger docs: `http://localhost:8000/docs`
- Health check: `http://localhost:8000/health`

### Docker (Production)

```bash
# Backend + PostgreSQL
cd docker/backend
docker compose up -d

# Frontend (nginx)
cd docker/portal
docker compose up -d
```

The backend `docker-compose.yml` requires a `.env` file at `docker/backend/.env` with:
- `DATABASE_URL`
- `SECRET_KEY`
- `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`

## Architecture

This is a self-hosted personal cloud portal with:
- **Frontend** (`frontend/`): Vanilla HTML/CSS/JS served via nginx. `index.html` is the portal with login/auth. `cloud.html` is the file manager UI.
- **Backend** (`backend/`): Python 3.11 FastAPI app with PostgreSQL via SQLAlchemy.
- **Docker** (`docker/`): Separate compose files for portal (nginx), backend+postgres, code-server, and AI services.

### Backend module layout

- `main.py` — app entry point, CORS config (only `www.myhomecloud.kr` and `cloud.myhomecloud.kr` are allowed), router registration
- `auth/router.py` — register, login, password change endpoints
- `auth/utils.py` — JWT creation/verification (`python-jose`, HS256, 60-min expiry), bcrypt via `passlib`, `get_current_user` dependency
- `files/router.py` — per-user file storage under `/nas/files/{username}/`. Trash is stored at `/nas/files/{username}/.trash/` and hidden from the listing. Delete moves to trash; permanent delete calls `shutil.rmtree`/`os.remove`.
- `system/router.py` — server status (CPU, RAM, disk) via `psutil`
- `core/config.py` — env vars (`SECRET_KEY`, `DATABASE_URL`); defaults to `fallback-dev-key` / localhost postgres when not set
- `database/database.py` — SQLAlchemy engine + session
- `models/user.py` — `User` model (username, hashed_password)

### Frontend auth flow

`script.js` stores the JWT in `localStorage`. All API calls go through a `fetchWithAuth()` wrapper that redirects to the portal on 401 (token expiry). The portal auto-refreshes the server status widget every 30 seconds.

### File storage

Files are stored on a mounted HDD at `/nas/files/{username}/` inside the Docker container (mapped via `volumes: /nas:/nas:rw` in `docker/backend/docker-compose.yml`). The `.trash` subdirectory is excluded from normal listings.

## Key constraints

- CORS is locked to the two production domains. For local frontend dev hitting a local backend, you'll need to temporarily add `http://localhost` to `allow_origins` in `main.py`.
- The `core/config.py` default `DATABASE_URL` points to the Docker service name `mhcloud-postgres`, so running `uvicorn` locally requires overriding `DATABASE_URL` to point to a local/reachable PostgreSQL instance.
