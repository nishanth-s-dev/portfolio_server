from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    response_json = {
        "message": "API is up and running.",
    }
    return response_json, 200