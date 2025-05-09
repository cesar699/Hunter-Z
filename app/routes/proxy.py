from flask import Blueprint, jsonify, abort
from app.services.tor import start_tor, stop_tor
from app.services.proxy_session import get_session

bp = Blueprint('proxy', __name__, url_prefix='/proxy')

@bp.route('/tor/<action>', methods=['POST'])
def tor_toggle(action):
    if action=='on':
        start_tor(); return jsonify({'tor':'enabled'})
    if action=='off':
        stop_tor(); return jsonify({'tor':'disabled'})
    abort(400)

@bp.route('/ip')
def current_ip():
    sess = get_session()
    ip = sess.get('https://api.ipify.org').text.strip()
    return jsonify({'ip':ip,'via_tor':bool(sess.proxies)})
