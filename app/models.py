from app import db

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

class Project(db.Model):
    __tablename__ = 'project'

    project_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.player_id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=False)
    tech_stack = db.Column(db.Text, nullable=False)
    project_url = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"Project('{self.title}', '{self.description}', '{self.image_url}', '{self.project_url}')"

class ConnectionType(db.Model):
    __tablename__ = 'connection_type'

    connection_type_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    connection_type = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"ConnectionType('{self.connection_type}')"

class Connection(db.Model):
    __tablename__ = 'connection'

    connection_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(255), nullable=False)
    connection_type_id = db.Column(db.Integer, db.ForeignKey('connection_type.connection_type_id'), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('player.player_id'), nullable=False)

    def __repr__(self):
        return f"Connection('{self.url}')"
