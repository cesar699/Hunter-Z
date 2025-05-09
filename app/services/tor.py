import subprocess, time, os, signal
from pathlib import Path
from stem import Signal
from stem.control import Controller
from flask import current_app

PIDFILE = Path('/tmp/tor.pid')

def _running(): return PIDFILE.exists()

def start_tor():
    if _running(): return
    proc = subprocess.Popen(['tor','--RunAsDaemon','0','--ControlPort','9051','--SocksPort','9050','--PidFile',str(PIDFILE)])
    time.sleep(4)
    current_app.config['TOR_ENABLED'] = True

def stop_tor():
    if not _running(): return
    os.kill(int(PIDFILE.read_text()), signal.SIGTERM)
    PIDFILE.unlink(missing_ok=True)
    current_app.config['TOR_ENABLED'] = False

def newnym():
    with Controller.from_port(port=9051) as c:
        c.authenticate()
        c.signal(Signal.NEWNYM)
