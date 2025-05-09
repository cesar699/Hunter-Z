from flask import Blueprint, send_file, abort, current_app
from pathlib import Path
from app.utils.packager import make_zip

bp = Blueprint('download', __name__, url_prefix='/download')

@bp.route('/<task_id>.zip')
def dl(task_id):
    rez = Path(current_app.config['RESULT_DIR'])/task_id
    if not rez.exists(): abort(404)
    zp = rez.with_suffix('.zip')
    if not zp.exists(): make_zip(rez,zp)
    return send_file(zp, as_attachment=True, download_name=f'HunterZ-{task_id}.zip')
