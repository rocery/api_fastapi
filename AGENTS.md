# AGENTS.md

## Commands

| Action | Command |
|--------|---------|
| Install deps | `pip install -r req.txt` |
| Run dev server | `uvicorn main:app --reload` |
| Run tests | No test files exist in this repo |
| Lint | No lint config found |

## Environment

- `.env` is loaded via `python-dotenv` at startup (see `main.py:11`, `database.py:3`)
- `.env` is gitignored — do not commit secrets
- Required env vars: `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`, `DB_NAME`, `SESSION_SECRET`

## Project structure

- `main.py` — FastAPI app entrypoint; loads `.env`, adds session middleware, includes `auth` router
- `routers/auth.py` — auth router mounted at `/`
- `models.py` — SQLAlchemy 2.0 `Users` model (uses `DeclarativeBase`)
- `database.py` — creates engine/session via `create_engine`/`sessionmaker`; `get_db()` yields sessions
- `dependencies.py` — `get_current_user()` reads `request.session["user"]`, raises `HTTPException(401)` if missing

## Database

- MySQL via `mysql+pymysql` driver (from `req.txt`)
- SQLAlchemy 2.0 style: `DeclarativeBase`, `sessionmaker` with `autocommit=False, autoflush=False`
- `.env` holds DB connection details; ensure MySQL is running before running tests or dev server

## Auth

- Session-based: `request.session["user"]` set by auth router
- `dependencies.get_current_user()` is the dependency to use for protecting routes