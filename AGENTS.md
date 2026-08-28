# AGENTS.md

## Stack & Entrypoint
- Python 3.14 + FastAPI 0.141 + SQLAlchemy 2.0 + PyMySQL — deps in `req.txt` (no `pyproject.toml`/`poetry`).
- Entrypoint: `app/main.py:1` (`app = FastAPI(...)`, routers registered via `app.include_router`).
- Run dev server: `venv/bin/uvicorn app.main:app --reload` (or `venv/bin/python -m uvicorn app.main:app --reload`).

## Setup
- Create venv + install: `python -m venv venv && venv/bin/pip install -r req.txt`
- Env file: `.env` at repo root (gitignored). Required vars — `API_FASTAPI_*`, `IOT_*`, `SISTEMIT_*` (HOST/PORT/USER/PASSWORD/NAME each), plus `SECRET_KEY` and `SESSION_SECRET`. `app/core/config.py:5` calls `load_dotenv(".env")` — cwd must be repo root, `os.getenv` only (no pydantic-settings).
- No `pytest`/`ruff`/`mypy`/CI config — no lint/test commands to run.

## Architecture — Read This First
- **Layout** follows `folder_sctructure.md` (now realized):
  ```
  app/main.py
  app/core/{config.py, security.py}
  app/database/{api_fastapi.py, iot.py, sistemit.py}
  app/modules/{auth,device,atk}/{model.py, schema.py, service.py, router.py}
  ```
- **3 MySQL databases**, each with its own engine/session/getter (`mysql+pymysql`, `pool_pre_ping=True`):
  - `api_fastapi` (`app/database/api_fastapi.py` `get_api_fastapi_db`) — `User` model in `app/modules/auth/model.py`
  - `iot` (`app/database/iot.py` `get_iot_db`) — `Device` model in `app/modules/device/model.py`
  - `sistemit` (`app/database/sistemit.py` `get_sistemit_db`) — `Atk` model in `app/modules/atk/model.py`
  Hosts are internal (`192.168.10.220/.223`) — not reachable off VPN; local dev needs tunnel or mock.
- **3 declarative bases** (one per DB) — `UserBase` in `app/modules/auth/model.py:4`, `IotBase` in `app/modules/device/model.py:4`, `SistemitBase` in `app/modules/atk/model.py:4` — do not merge.
- Routers: `app/modules/auth/router.py` (public `POST /auth/login`), `app/modules/device/router.py` (`GET /devices`), `app/modules/atk/router.py` (`GET /atk`). Last two require `Authorization: Bearer <JWT>` via `app/core/security.py:38` (`get_current_user`, `HTTPBearer`).
- `app/core/config.py` centralizes all env reads; `app/core/security.py` holds JWT/MD5/auth dependency; `app/modules/*/service.py` holds domain logic (`authenticate_user`, `list_devices`, `list_atk`); routers are thin HTTP wrappers calling services.

## Auth Quirks
- Passwords are **MD5 hex** (`app/core/security.py:14` `md5_password`) — legacy, not bcrypt. Comparisons are plain `hexdigest()` equality.
- JWT: `HS256`, `SECRET_KEY` from `.env`, 8h expiry (`app/core/security.py:20`). Payload `sub=user_id`, `username`, `level`.
- `get_current_user` always hits `api_fastapi` DB to re-fetch user — even `iot`/`sistemit` routes depend on that DB being up.

## Conventions
- Keep `model.py` / `schema.py` / `service.py` / `router.py` per module; do not re-consolidate into flat `app/model.py` etc.
- Router prefix/tags defined at `APIRouter(prefix=...)` level; `app/main.py:10-14` re-exports as `auth_router`/`device_router`/`atk_router` and includes without extra prefix.
- Responses use `list[DeviceResponse]` / `AtkResponse` with `| None` optional fields — match existing patterns.
