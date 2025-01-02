# Event-Driven Architecture

folder structure

├── app/
│   ├── __init__.py
│   ├── main.py                # Main FastAPI application
│   ├── models.py              # Pydantic models
│   ├── config.py              # Configuration (Redis, environment variables, etc.)
│   ├── models/
│   │   ├── __init__.py
│   │   ├── datamodels.py      # models for data handling
│   │   ├── errors.py          # Error classes
│   ├── services/
│   │   ├── __init__.py
│   │   ├── fuel_price_service.py  # Logic for fetching fuel prices and interacting with Redis
│   │   ├── pubsub_service.py      # Redis pub/sub logic
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── scraper.py         # Web scraping logic with BeautifulSoup
│   │   ├── cache.py  
│   │   ├── exceptions.py	# Custom error handling
│   └──  auth/
│      ├── __init__.py
│      ├── jwt_handler.py  # JWT generation and verification
│      └── auth_service.py # token issuance logic
├── requirements.txt  
├── Dockerfile
└── .dockerignore
