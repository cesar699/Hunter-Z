import zipfile, os
from pathlib import Path

def make_zip(src:Path, dest:Path):
    with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED) as z:
        for f in src.rglob('*'):
            z.write(f, arcname=f.relative_to(src))
