# Event-Driven Architecture

folder structure
```bash
├── src/
│   ├── __init__.py
│   ├── main.py                     [x] # Main FastAPI application
│   ├── models.py                   [x] # Pydantic models
│   ├── config.py                   [.] # Configuration (Redis, environment variables, etc.)
│   ├── models/
│   │   ├── __init__.py
│   │   ├── datamodels.py           [x] # models for data handling
│   │   ├── errors.py               [x] # Error classes
│   ├── services/
│   │   ├── __init__.py
│   │   ├── fuel_price_service.py   [.] # Logic for fetching fuel prices and interacting with Redis
│   │   ├── pubsub_service.py       [.] # Redis pub/sub logic
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── scraper.py              [x] # Web scraping logic with BeautifulSoup
│   │   ├── cache.py                [.]
│   │   ├── metas.py                [x] # metaclass/factory for class creation
│   │   ├── exceptions.py	        [.] # Custom error handling
│   └──  auth/
│      ├── __init__.py
│      ├── jwt_handler.py           [.] # JWT generation and verification
│      └── auth_service.py          [.] # token issuance logic
├── requirements.txt  
├── Dockerfile
└── .dockerignore
```

created custom error classes using an abstract BaseError class, separated the scraping logic

