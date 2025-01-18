from flask import Blueprint
from app.utils.dbutil import DBUtil


dbutil = DBUtil()
bp = Blueprint('connection', __name__, url_prefix='/api')

@bp.route('/connections')
def get_all_connections():
    from app.models.connection import Connection
    connections = dbutil.execute_query(Connection).all()
    response = []
    for connection in connections:
        response.append(connection.to_dict())
    return response, 200

@bp.route('/connections/<connection_id>')
def get_connection_with_id(connection_id):
    from app.models.connection import Connection
    response = {}
    query_res = dbutil.execute_query(Connection).filter_by(connection_id=connection_id).first()
    if query_res is not None:
        response = query_res.to_dict()
        return response, 200
    else:
        response['message'] = 'Connection not found'
        return response, 404
