# app/models/connection.py
from app import db

class Connection(db.Model):
    __tablename__ = 'connection'

    connection_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(255), nullable=False)
    connection_type_id = db.Column(db.Integer, db.ForeignKey('connection_type.connection_type_id'), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('player.player_id'), nullable=False)

    def __repr__(self):
        return f"Connection('{self.url}')"