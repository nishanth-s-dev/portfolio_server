from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return "<h1>Hello, World!</h1>"