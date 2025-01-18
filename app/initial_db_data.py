from app.models import player, connection_type, connection, project

Player = player.Player
ConnectionType = connection_type.ConnectionType
Connection = connection.Connection
Project = project.Project

class InitialDBData:
    def __init__(self):
        self.players = [
            self.create_player('nishanth', 'Nishanth', 'I am a software engineer', 'Software Engineer', 'image_url_placeholder', 'Bangalore'),
        ]

        self.connection_types = [
            self.create_connection_type('Mail'),
            self.create_connection_type('LinkedIn'),
            self.create_connection_type('GitHub'),
        ]

        self.connections = [
            self.create_connection("mailto:nishanth.selvakumar.dev@gmail.com", 1, 1),
            self.create_connection("https://www.linkedin.com/in/nishanth-s-dev/", 2, 1),
            self.create_connection("https://github.com/nishanth-s-dev", 3, 1),
        ]

        self.projects = [
            self.create_project(1, 'Project 1', 'image_url_placeholder', 'Description 1', 'Tech Stack 1', 'https://project1.com', '2021-01-01 00:00:00'),
            self.create_project(1, 'Project 2', 'image_url_placeholder', 'Description 2', 'Tech Stack 2', 'https://project2.com', '2021-01-02 00:00:00'),
            self.create_project(1, 'Project 3', 'image_url_placeholder', 'Description 3', 'Tech Stack 3', 'https://project3.com', '2021-01-03 00:00:00'),
        ]

    def create_player(self, username: str, display_name: str, description: str, occupation: str, image_url: str, location: str) -> Player:
        return Player(username=username, display_name=display_name, description=description, occupation=occupation, image_url=image_url, location=location)

    def create_connection_type(self, connection_type: str) -> ConnectionType:
        return ConnectionType(connection_type=connection_type)

    def create_connection(self, url: str, connection_type_id: int, player_id: int) -> Connection:
        return Connection(url=url, connection_type_id=connection_type_id, player_id=player_id)

    def create_project(self, player_id: int, title: str, image_url: str, description: str, tech_stack: str, project_url: str, created_on: str) -> Project:
        return Project(player_id=player_id, title=title, image_url=image_url, description=description, tech_stack=tech_stack, project_url=project_url, created_on=created_on)

    def get_initial_data(self) -> dict:
        return {
            Player: self.players,
            ConnectionType: self.connection_types,
            Connection: self.connections,
            Project: self.projects,
        }