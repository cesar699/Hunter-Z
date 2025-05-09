import requests
from flask import current_app

def get_session():
    s = requests.Session()
    if current_app.config.get('TOR_ENABLED'):
        proxy = 'socks5h://127.0.0.1:9050'
        s.proxies.update({'http':proxy,'https':proxy})
    return s
