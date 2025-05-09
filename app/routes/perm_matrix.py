from flask import Blueprint, jsonify, request
from app.services.risk_matrix import PERM_RISK_MAP
bp = Blueprint('perm', __name__, url_prefix='/perm')
@bp.get('/')
def get_matrix():
    return jsonify(PERM_RISK_MAP)
@bp.post('/')
def upd():
    PERM_RISK_MAP.update({k:int(v) for k,v in (request.json or {}).items()})
    return jsonify(status='ok')
