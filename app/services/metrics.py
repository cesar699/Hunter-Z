import psutil, json, time, threading
from queue import SimpleQueue
from flask import Blueprint, Response

_q = SimpleQueue()

def _collector():
    while True:
        _q.put(json.dumps({
            "cpu": psutil.cpu_percent(),
            "mem": round(psutil.virtual_memory().percent,1),
            "net": round(psutil.net_io_counters().bytes_sent/1024/1024,2)
        }))
        time.sleep(2)

def start_collector(app):
    threading.Thread(target=_collector, daemon=True).start()

bp = Blueprint('metrics', __name__, url_prefix='/metrics')

@bp.route('/stream')
def stream():
    def gen():
        while True:
            yield f"data: {_q.get()}\n\n"
    return Response(gen(), mimetype='text/event-stream')
