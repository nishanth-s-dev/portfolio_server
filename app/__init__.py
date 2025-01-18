from flask import Flask
from .utils.dbutil import DBUtil
from . import routes

def create_app():
    app = Flask(__name__)

    dbutil = DBUtil()
    dbutil.initialize(app)

    app.register_blueprint(routes.bp)
    return app