
from app import create_app
from celery import shared_task
from app.services import extractor, permission, report
from dynamic.analyzer import run_dynamic_analysis
from pathlib import Path

app = create_app()
celery = app.celery

@shared_task(queue='static')
def analyze_static(file_path):
    urls = extractor.extract_urls(file_path)
    perms = permission.analyze(file_path)
    meta = {'mode':'static'}
    out_dir = Path('uploads/results')/Path(file_path).stem
    return report.generate(urls, perms, meta, out_dir)

@shared_task(queue='dynamic')
def analyze_dynamic(file_path):
    return run_dynamic_analysis(file_path)
