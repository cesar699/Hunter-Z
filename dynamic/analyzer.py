
import subprocess, time, json, tempfile
from pathlib import Path
from datetime import datetime
from app.services.report import generate as gen_report

RUNTIME = 60  # seconds

def run_dynamic_analysis(apk_path:str):
    task_id = Path(apk_path).stem + '-' + datetime.utcnow().strftime('%H%M%S')
    workdir = Path('uploads/dyn')/task_id
    workdir.mkdir(parents=True, exist_ok=True)
    pcap = workdir/'traffic.pcap'

    # placeholder for real docker-android + tcpdump + frida control
    # here we just create dummy data
    summary = {"dst":[{"dst":"1.1.1.1","count":10}], "points":[0]*60}
    hooks = [{"type":"http","url":"https://example.com"}]

    # save dummy files
    (workdir/'tcp_summary.json').write_text(json.dumps(summary))
    (workdir/'frida.json').write_text(json.dumps(hooks))

    meta = {"mode":"dynamic","task_id":task_id}
    gen_report({}, {}, meta, workdir)
    return {"pcap":str(pcap),"summary":summary,"hooks":hooks}
