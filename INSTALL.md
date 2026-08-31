# INSTALL — Deploy api_fastapi + frontend to Another Server

This guide covers clean install on a fresh Ubuntu 22.04/24.04 server. Tested with Python 3.14 + FastAPI 0.141 + MySQL 8 + Node 20+.

Backend: `app/main.py:1` (FastAPI, 3 MySQL DBs, JWT HS256 8h)
Frontend: `frontend/` (React 18 + TypeScript + Vite 6 + shadcn/ui + TanStack Query)

---

## 0. Prerequisites

```bash
# System updates
sudo apt update && sudo apt upgrade -y

# Essential tools
sudo apt install -y git curl build-essential

# Python 3.14 (or 3.11+ if 3.14 unavailable — backend requires >=3.11)
python3 --version
# If Python 3.14 not in apt, use deadsnakes or pyenv:
sudo add-apt-repository ppa:deadsnakes/ppa -y && sudo apt update
sudo apt install -y python3.14 python3.14-venv python3.14-dev

# Node 20+ (for frontend)
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs
node --version && npm --version  # expect v20.x / 11.x

# Nginx (reverse proxy + static)
sudo apt install -y nginx

# MySQL client (DBs are remote; server only needs client/driver)
sudo apt install -y mysql-client
# PyMySQL is used, no system MySQL server required on app server unless you host DBs locally
```

### 0.1 Network / DB Notes

`app/core/config.py:5` loads `.env` from repo root via `load_dotenv(".env")` — cwd must be repo root.  
`app/database/{api_fastapi,iot,sistemit}.py` each create separate `mysql+pymysql` engines (`pool_pre_ping=True`).  
Default hosts in production are `192.168.10.220/.223` (internal). On a new server outside VPN you must either:

- open VPN/tunnel to those IPs, **or**
- change `.env` DB hosts to reachable hosts (or move DBs to new server).

`app/core/security.py:38` (`get_current_user`) always hits `api_fastapi` DB — even `GET /devices/*` and `GET /atk` require that DB up.

---

## 1. Clone & Layout

```bash
cd /opt   # or /home/<user>
sudo git clone https://github.com/<org>/api_fastapi.git
sudo chown -R $USER:$USER api_fastapi
cd api_fastapi
ls -la
# expect: app/ frontend/ req.txt folder_sctructure.md INSTALL.md .gitignore (no .env)
```

---

## 2. Backend Install

### 2.1 Python venv + deps

```bash
python3.14 -m venv venv
# or: python3 -m venv venv
venv/bin/pip install --upgrade pip
venv/bin/pip install -r req.txt
# req.txt: fastapi==0.141.1 uvicorn==0.52.4 sqlalchemy==2.0.52 pymysql==1.2.0 pyjwt==2.13.0 python-dotenv==1.2.3
```

### 2.2 Env file (repo root/.env) — gitignored

Create `/opt/api_fastapi/.env` (cwd must be repo root, `app/core/config.py:5` reads `.env` relative to cwd):

```ini
# --- JWT ---
SECRET_KEY=change-me-generate-with-openssl-rand-hex-32
SESSION_SECRET=change-me-another-random-64-chars
# ALGORITHM is hardcoded HS256 in app/core/config.py:9

# --- api_fastapi DB (User) — app/database/api_fastapi.py ---
API_FASTAPI_DB_HOST=192.168.10.220
API_FASTAPI_DB_PORT=3306
API_FASTAPI_DB_USER=api_user
API_FASTAPI_DB_PASSWORD=strong-password
API_FASTAPI_DB_NAME=api_fastapi

# --- iot DB (Device, IspSpeedtest) — app/database/iot.py ---
IOT_DB_HOST=192.168.10.223
IOT_DB_PORT=3306
IOT_DB_USER=iot_user
IOT_DB_PASSWORD=strong-password
IOT_DB_NAME=iot

# --- sistemit DB (Atk) — app/database/sistemit.py ---
SISTEMIT_DB_HOST=192.168.10.223
SISTEMIT_DB_PORT=3306
SISTEMIT_DB_USER=sistemit_user
SISTEMIT_DB_PASSWORD=strong-password
SISTEMIT_DB_NAME=sistemit
```

Generate secrets:

```bash
openssl rand -hex 32   # for SECRET_KEY
openssl rand -hex 32   # for SESSION_SECRET
```

> `.env` example in repo only has `DB_HOST/DB_PORT/DB_USER/DB_PASSWORD/DB_NAME/SESSION_SECRET` (legacy). New server must use the 17 vars above matching `app/core/config.py:7-30`. Keep file `chmod 600`.

### 2.3 Verify DB connectivity

```bash
# quick Python check (no server needed)
venv/bin/python -c "
import os; from dotenv import load_dotenv; load_dotenv('.env')
from sqlalchemy import create_engine, URL
from app.core.config import *
url = URL.create('mysql+pymysql', username=API_FASTAPI_DB_USER, password=API_FASTAPI_DB_PASSWORD, host=API_FASTAPI_DB_HOST, port=int(API_FASTAPI_DB_PORT), database=API_FASTAPI_DB_NAME)
print('URL:', url.render_as_string(hide_password=True))
e = create_engine(url, pool_pre_ping=True)
with e.connect() as c: print(c.execute(c.exec_driver_sql('SELECT 1')).scalar())
print('api_fastapi DB OK')
"
# repeat for IOT_DB_* and SISTEMIT_DB_*
```

### 2.4 Run dev (manual) & smoke test

```bash
# must run from repo root so load_dotenv(".env") finds file
venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
# or: venv/bin/python -m uvicorn app.main:app --reload

# in another terminal:
curl -i http://127.0.0.1:8000/
# {"message":"FastAPI API is running"}

curl -i http://127.0.0.1:8000/docs        # Swagger
curl -i http://127.0.0.1:8000/openapi.json

# auth test (replace user/pass with real row in `user` table — password is MD5 hex, app/core/security.py:14)
curl -s -X POST http://127.0.0.1:8000/auth/login -H 'Content-Type: application/json' \
  -d '{"username":"admin","password":"admin123"}' | jq
# expect: {"access_token":"...","token_type":"bearer","user":{...}}

TOKEN=$(curl -s -X POST http://127.0.0.1:8000/auth/login -H 'Content-Type: application/json' \
  -d '{"username":"admin","password":"admin123"}' | jq -r .access_token)

curl -s http://127.0.0.1:8000/auth/me -H "Authorization: Bearer $TOKEN" | jq
curl -s http://127.0.0.1:8000/devices/list -H "Authorization: Bearer $TOKEN" | jq | head
curl -s "http://127.0.0.1:8000/devices/isp_speedtest?period=2026-01" -H "Authorization: Bearer $TOKEN" | jq | head
curl -s http://127.0.0.1:8000/atk -H "Authorization: Bearer $TOKEN" | jq | head
```

If `401` or `500` on `/auth/me`, check `SECRET_KEY` matches token generation and `api_fastapi` DB row exists.

### 2.5 Systemd service (production)

Create `/etc/systemd/system/api_fastapi.service`:

```ini
[Unit]
Description=api_fastapi — FastAPI IoT API
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/opt/api_fastapi
# WorkingDirectory MUST be repo root so .env is found (app/core/config.py:5)
Environment="PATH=/opt/api_fastapi/venv/bin"
ExecStart=/opt/api_fastapi/venv/bin/uvicorn app.main:app --host 127.0.0.1 --port 8000 --workers 2
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now api_fastapi
sudo systemctl status api_fastapi
journalctl -u api_fastapi -f
```

> For HTTPS/multiple workers, put gunicorn+uvicorn workers or run behind Nginx (next section). Add `uvicorn[standard]` if you need `httptools`.

### 2.6 CORS (if frontend on different origin)

Backend currently has no `CORSMiddleware`. If Nginx serves API and frontend on different ports/domains, add in `app/main.py:7`:

```python
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(CORSMiddleware, allow_origins=["https://your-frontend.com"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
```

Then `sudo systemctl restart api_fastapi`.

### 2.7 Firewall

```bash
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
# do NOT expose 8000 publicly if Nginx proxies to 127.0.0.1:8000
sudo ufw enable
```

---

## 3. Frontend Install

### 3.1 Env

`frontend/src/config/env.ts:1` reads `import.meta.env.VITE_API_BASE_URL` with fallback `http://localhost:8000`.

Create `frontend/.env` (also `.env.example` exists):

```ini
VITE_API_BASE_URL=https://api.yourdomain.com
# local dev: http://localhost:8000
# if serving API under same Nginx as frontend, can be /api and add proxy in vite.config.ts:1 / nginx
```

### 3.2 Install & build

```bash
cd /opt/api_fastapi/frontend

# install (uses package.json:1 — react 18, vite 6, tailwind 3, shadcn)
npm ci        # or npm install
# if shadcn components missing (should be committed in src/components/ui/):
npx shadcn@latest init -d   # only if components.json not present
npx shadcn@latest add button input label card table badge alert skeleton  # as needed

# dev
npm run dev   # http://0.0.0.0:5173

# prod build
npm run build # tsc -b + vite build → frontend/dist/
ls -lh dist/
# preview locally (optional)
npm run preview -- --host 0.0.0.0 --port 4173
```

### 3.3 Serve static via Nginx

Build output is `frontend/dist/` (gitignored). Nginx should serve it:

```bash
# after build:
sudo mkdir -p /var/www/api_fastapi
sudo cp -r /opt/api_fastapi/frontend/dist/* /var/www/api_fastapi/
# or make Nginx root point directly to /opt/api_fastapi/frontend/dist
```

---

## 4. Nginx — Single Server (API + Frontend)

Example `/etc/nginx/sites-available/api_fastapi`:

```nginx
# Frontend — static
server {
    listen 80;
    server_name yourdomain.com;

    # frontend static
    root /opt/api_fastapi/frontend/dist;
    index index.html;

    # API — proxy to uvicorn
    location /auth/ {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
    location /devices/ {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
    location /atk {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
    location /docs {
        proxy_pass http://127.0.0.1:8000;
    }
    location /openapi.json {
        proxy_pass http://127.0.0.1:8000;
    }
    location = / {
        proxy_pass http://127.0.0.1:8000;
        # or serve frontend index.html if API root should not be proxied:
        # try_files $uri $uri/ /index.html;
    }

    # SPA fallback — must be last
    location / {
        try_files $uri $uri/ /index.html;
    }

    # Optional: if you want /api prefix instead of direct /auth, add:
    # location /api/ { proxy_pass http://127.0.0.1:8000/; }
    # and set VITE_API_BASE_URL=/api
}
```

Enable:

```bash
sudo ln -s /etc/nginx/sites-available/api_fastapi /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```

**Two-domain variant:** serve `api.yourdomain.com` → `proxy_pass 127.0.0.1:8000` and `yourdomain.com` → `root /opt/.../dist`. Then set `VITE_API_BASE_URL=https://api.yourdomain.com` and enable CORS (2.6).

HTTPS:

```bash
sudo apt install -y certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com -d api.yourdomain.com
```

---

## 5. Checklist — New Server

- [ ] `git clone` + `venv/bin/pip install -r req.txt` OK
- [ ] `.env` (17 vars, `chmod 600`, cwd=repo root) — DB hosts reachable
- [ ] `venv/bin/uvicorn app.main:app` + `curl /` + `POST /auth/login` OK
- [ ] `systemd` service enabled, `journalctl -u api_fastapi` clean
- [ ] `frontend/.env` `VITE_API_BASE_URL` points to API (public URL or `/api`)
- [ ] `cd frontend && npm ci && npm run build` OK, `dist/` present
- [ ] Nginx serves `dist` + proxies `/auth` `/devices` `/atk` to `127.0.0.1:8000`
- [ ] `curl https://yourdomain.com/auth/me` with token 200, frontend login flow works
- [ ] `ufw` + `certbot` HTTPS

---

## 6. Updates / Rollback

```bash
cd /opt/api_fastapi
git pull
venv/bin/pip install -r req.txt   # if req.txt changed
sudo systemctl restart api_fastapi
cd frontend && npm ci && npm run build
sudo cp -r dist/* /var/www/api_fastapi/  # if Nginx points there
sudo systemctl reload nginx
```

Rollback: `git checkout <prev-tag> && sudo systemctl restart api_fastapi`.

---

## 7. Troubleshooting

| Symptom | Cause / Fix |
|---------|-------------|
| `FileNotFoundError: .env` or `SECRET_KEY is None` | Run from repo root; `WorkingDirectory=/opt/api_fastapi` in systemd; `load_dotenv(".env")` is cwd-relative |
| `sqlachemy.exc.OperationalError: Can't connect to MySQL` | DB host/port/firewall/VPN; test `mysql -h $IOT_DB_HOST -u $IOT_DB_USER -p` |
| `401 Invalid token / User not found` | `SECRET_KEY` changed after token issued (tokens are HS256, 8h expiry `app/core/security.py:20`); re-login |
| `401 Username atau password salah` on correct password | DB `user.password` is MD5 hex (`app/core/security.py:14`); insert with `SELECT MD5('pass')` |
| Frontend `CORS error` | Add `CORSMiddleware` in `app/main.py:7` or serve API+frontend same origin via Nginx |
| Frontend blank after Nginx | `root` must point to `frontend/dist` and `try_files $uri /index.html` for SPA routing (`/devices`, `/atk`) |
| `vite build` fails `tsc -b` | Check `frontend/tsconfig.json:1` path alias `@/*` matches `vite.config.ts:1` alias |

---

## 8. One-liner Fresh Server (copy-paste)

```bash
set -e
APP_DIR=/opt/api_fastapi
REPO_URL=https://github.com/<org>/api_fastapi.git
git clone $REPO_URL $APP_DIR
cd $APP_DIR
python3.14 -m venv venv && venv/bin/pip install -r req.txt
cat > .env <<'ENV'
SECRET_KEY=$(openssl rand -hex 32)
SESSION_SECRET=$(openssl rand -hex 32)
API_FASTAPI_DB_HOST=192.168.10.220
API_FASTAPI_DB_PORT=3306
API_FASTAPI_DB_USER=api_user
API_FASTAPI_DB_PASSWORD=change-me
API_FASTAPI_DB_NAME=api_fastapi
IOT_DB_HOST=192.168.10.223
IOT_DB_PORT=3306
IOT_DB_USER=iot_user
IOT_DB_PASSWORD=change-me
IOT_DB_NAME=iot
SISTEMIT_DB_HOST=192.168.10.223
SISTEMIT_DB_PORT=3306
SISTEMIT_DB_USER=sistemit_user
SISTEMIT_DB_PASSWORD=change-me
SISTEMIT_DB_NAME=sistemit
ENV
# edit passwords + hosts above before starting!
venv/bin/uvicorn app.main:app --host 127.0.0.1 --port 8000 --workers 2 &
cd frontend && npm ci && echo "VITE_API_BASE_URL=http://$(hostname -f):8000" > .env && npm run build
echo "Backend PID $! — now configure systemd+nginx per sections 2.5 and 4"
```

---

## 9. Repo Files Reference

- Backend entry: `app/main.py:1`
- Config: `app/core/config.py:5`, Security: `app/core/security.py:14`
- DB engines: `app/database/api_fastapi.py`, `iot.py`, `sistemit.py`
- Modules: `app/modules/{auth,device,atk}/{model,schema,service,router}.py`
- Frontend entry: `frontend/src/main.tsx:1`, routes: `frontend/src/routes/index.tsx:1`, api: `frontend/src/lib/api.ts:1`
