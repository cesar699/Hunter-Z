class Config:
    CELERY_BROKER_URL = 'redis://redis:6379/0'
    RESULT_DIR = 'uploads/results'
    UPLOAD_DIR = 'uploads'
    TOR_ENABLED = False
    TOR_SOCKS   = 'socks5h://127.0.0.1:9050'
    TOR_CTRL    = ('127.0.0.1', 9051)
