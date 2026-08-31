# Frontend — IoT API (React + TypeScript + Vite + shadcn/ui)

Mirrors `api_fastapi` backend (`app/main.py`, `app/modules/{auth,device,atk}`).

## Quick start

```bash
cd frontend
npm install
cp .env.example .env   # set VITE_API_BASE_URL=http://localhost:8000
npm run dev            # http://localhost:5173
```

Backend must be running: `venv/bin/uvicorn app.main:app --reload` (repo root).

## Scripts

- `npm run dev` — Vite dev server (port 5173)
- `npm run build` — type-check + production build
- `npm run preview` — preview built bundle

## Env

- `VITE_API_BASE_URL` — FastAPI base URL (no trailing slash)

## Routes (mirror backend)

| Frontend | Backend | Auth |
|----------|---------|------|
| `/login` | `POST /auth/login` (public) | no |
| `/devices` | `GET /devices/list` | Bearer |
| `/devices/speedtest?server=&period=YYYY-MM` | `GET /devices/isp_speedtest` | Bearer |
| `/atk` | `GET /atk` | Bearer |

Auth: JWT HS256 8h, `Authorization: Bearer <token>` via `src/lib/api.ts` interceptor. Token + user cached in `localStorage` (`access_token`, `auth_user`), revalidated via `GET /auth/me`.

## shadcn/ui

Initialized via `npx shadcn@latest init` (config `components.json`). To add components:

```bash
npx shadcn@latest add button input label card table badge alert skeleton
npx shadcn@latest add select pagination calendar popover tabs
```

Utils: `src/lib/utils.ts` (`cn()` = `clsx` + `tailwind-merge`).

## Adding a new module (e.g. `ocr`)

Mirrors `notes.txt` backend steps:

```bash
mkdir -p src/modules/ocr/{hooks,components,pages}
touch src/modules/ocr/{api.ts,types.ts,schema.ts}
```

1. `types.ts` — interfaces (`| null` for nullable like `AtkResponse`)
2. `api.ts` — `api.get/post("/ocr"...)`
3. `hooks/useOcr.ts` — `useQuery`/`useMutation`
4. `pages/OcrListPage.tsx` + `routes/index.tsx` — add protected route if needed
