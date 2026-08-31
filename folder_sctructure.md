app/
├── main.py
│
├── core/
│   ├── config.py
│   └── security.py
│
├── database/
│   ├── api_fastapi.py
│   ├── iot.py
│   └── sistemit.py
│
└── modules/
    ├── auth/
    │   ├── model.py
    │   ├── schema.py
    │   ├── service.py
    │   └── router.py
    │
    ├── device/
    │   ├── model.py
    │   ├── schema.py
    │   ├── service.py
    │   └── router.py
    │
    └── atk/
        ├── model.py
        ├── schema.py
        ├── service.py
        └── router.py

uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload