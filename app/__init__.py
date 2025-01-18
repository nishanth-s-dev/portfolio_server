from flask import Flask
from .utils.dbutil import DBUtil
from .utils.routeutil import RouteUtil
from .routes import index
from .initial_db_data import InitialDBData
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)

    dbutil = DBUtil()
    with app.app_context():
        dbutil.initialize(app)
        dbutil.load_initial_data(InitialDBData().get_initial_data())

    routeutil = RouteUtil()
    routeutil.register_blueprints(app)

    return app