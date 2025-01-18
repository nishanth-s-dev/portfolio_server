from flask import Flask
from . import routes
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import getenv
from urllib.parse import quote_plus
import pymysql

db = SQLAlchemy()
load_dotenv()

def create_app():
    username = quote_plus(getenv('DB_USERNAME'))
    password = quote_plus(getenv('DB_PASSWORD'))
    host = getenv('DB_HOST', 'localhost')
    port = getenv('DB_PORT', '3306')
    database = getenv('DB_NAME')
    db_url = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'

    connection = pymysql.connect(host=host, user=username, password=getenv("DB_PASSWORD"), port=int(port))
    with connection.cursor() as cursor:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
    connection.close()

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    from .models import Player, Project, ConnectionType, Connection

    with app.app_context():
        try:
            db.create_all()
            print("Database connected successfully")
            print("Creating tables...")
        except Exception as e:
            print("Database connection failed", e)

    app.register_blueprint(routes.bp)

    return app