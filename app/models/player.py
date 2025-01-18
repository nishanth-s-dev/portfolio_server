from . import db

class Player(db.Model):
    __tablename__ = 'player'

    player_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    display_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    occupation = db.Column(db.String(255), nullable=True)
    image_url = db.Column(db.String(255), nullable=True)
    location = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"Player('{self.username}', '{self.display_name}', '{self.description}', '{self.occupation}', '{self.image_url}', '{self.location}')"

    def to_dict(self):
        return {
            "player_id": self.player_id,
            "username": self.username,
            "display_name": self.display_name,
            "description": self.description,
            "occupation": self.occupation,
            "image_url": self.image_url,
            "location": self.location
        }
