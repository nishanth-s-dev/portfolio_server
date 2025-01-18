import logging
from pymysql import connect, MySQLError
from os import getenv
from urllib.parse import quote_plus
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from .constants import DBConstants
import importlib

load_dotenv()

# DB Util is a singleton class
class DBUtil:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DBUtil, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.db = SQLAlchemy()
            self.database_connectivity_details = {
                'username': getenv(DBConstants.DB_USERNAME),
                'password': getenv(DBConstants.DB_PASSWORD),
                'host': getenv(DBConstants.DB_HOST, DBConstants.DEFAULT_HOST),
                'port': int(getenv(DBConstants.DB_PORT, DBConstants.DEFAULT_PORT)),
                'database': getenv(DBConstants.DB_NAME)
            }
            self.logger = logging.getLogger(__name__)
            logging.basicConfig(level=logging.INFO)
            self.initialized = True

    def initialize(self, app):
        try:
            self.__create_db_if_not_exist()
            app.config[DBConstants.SQLALCHEMY_DATABASE_URI] = self.__get_db_url_with_url_encoding()
            app.config[DBConstants.SQLALCHEMY_TRACK_MODIFICATIONS] = False

            # Triggering every model | without this, models/tables won't be created
            importlib.import_module('app.models')

            self.db.init_app(app)
            self.db.create_all()
            # self.load_initial_data()
            self.logger.info("Database connected successfully and tables created.")

        except MySQLError as e:
            self.logger.error("Database initialization failed", exc_info=True)
        except Exception as e:
            self.logger.error("An unexpected error occurred", exc_info=True)

    def load_initial_data(self, initial_data=None):
        if initial_data is None:
            initial_data = dict()
        try:
            for model, model_data in initial_data.items():
                if self.execute_query(model).count() == 0:
                    for data in model_data:
                        self.db.session.add(data)
                    self.db.session.commit()
            self.logger.info("Initial data loaded successfully.")
        except Exception as e:
            self.logger.error("Failed to load initial data", exc_info=True)

    def execute_query(self, model):
        return self.db.session.query(model)

    def __get_db_url_with_url_encoding(self):
        details = self.database_connectivity_details
        return f"mysql+pymysql://{details['username']}:{quote_plus(details['password'])}@{details['host']}:{details['port']}/{details['database']}"

    def __create_db_if_not_exist(self):
        details = self.database_connectivity_details
        try:
            connection = connect(host=details['host'], user=details['username'], password=details['password'], port=details['port'])
            with connection.cursor() as cursor:
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {details['database']}")
            connection.close()
            self.logger.info(f"Database '{details['database']}' checked/created successfully.")
        except MySQLError as e:
            self.logger.error("Failed to create database", exc_info=True)
        except Exception as e:
            self.logger.error("An unexpected error occurred", exc_info=True)


