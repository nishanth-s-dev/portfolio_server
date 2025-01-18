from flask import Blueprint

bp = Blueprint('index', __name__, url_prefix='/api')

@bp.route('/', methods=['GET'])
def index():
    response_json = {
        "message": "API is up and running.",
    }
    return response_json, 200
