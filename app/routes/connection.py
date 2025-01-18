from flask import Blueprint

bp = Blueprint('connection', __name__, url_prefix='/api')

@bp.route('/connections')
def get_all_connections():
    response_json = {
        "message": f"Connections endpoint.",
    }
    return response_json, 200

@bp.route('/connections/<connection_id>')
def get_connection_with_id(connection_id):
    response_json = {
        "message": f"Connections endpoint with player id: {connection_id}.",
    }
    return response_json, 200
