from app import db

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
