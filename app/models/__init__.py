from app.utils.dbutil import DBUtil

db = DBUtil().db

from .player import Player
from .project import Project
from .connection_type import ConnectionType
from .connection import Connection