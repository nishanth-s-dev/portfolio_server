from . import db

class ConnectionType(db.Model):
    __tablename__ = 'connection_type'

    connection_type_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    connection_type = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"ConnectionType('{self.connection_type}')"

    def to_dict(self):
        return {
            "connection_type_id": self.connection_type_id,
            "connection_type": self.connection_type
        }