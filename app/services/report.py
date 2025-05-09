from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path
from weasyprint import HTML
from datetime import datetime, timezone

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html','xml'])
)
def generate(urls_obj, perm_obj, meta, out_dir):
    tpl = env.get_template('report.html.j2')
    html = tpl.render(**urls_obj, **perm_obj, meta=meta)
    out_dir = Path(out_dir); out_dir.mkdir(parents=True, exist_ok=True)
    html_path = out_dir/'report.html'
    html_path.write_text(html, encoding='utf-8')
    pdf_path = out_dir/'report.pdf'
    HTML(string=html, base_url='.').write_pdf(pdf_path)
    return {"html":str(html_path),"pdf":str(pdf_path)}
