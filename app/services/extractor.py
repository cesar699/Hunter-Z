import re
from androguard.misc import AnalyzeAPK

URL_RE  = re.compile(r'https?://[\w\.-/:%#\$&\?~.=]+')
IP_RE   = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}(?::\d+)?\b')
API_RE  = re.compile(r'/(?:v\d+/)?[A-Za-z0-9._-]+/[^/\s"\']+')

def extract_urls(apk_path:str)->dict:
    _, _, dx = AnalyzeAPK(apk_path)
    urls, ips, apis = set(), set(), set()
    for _, m in dx.get_methods():
        for const in m.get_constants():
            if isinstance(const,str):
                if URL_RE.search(const): urls.add(const.strip())
                if IP_RE.search(const): ips.update(IP_RE.findall(const))
                if API_RE.search(const): apis.update(API_RE.findall(const))
    return {"urls":sorted(urls),"ips":sorted(ips),"apis":sorted(apis)}
