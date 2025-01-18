from app.models import player, connection_type, connection, project

class InitialDBData:
    def __init__(self):
        self.players = [
            player.Player(username='nishanth', display_name='Nishanth', description='I am a software engineer', occupation='Software Engineer', image_url='image_url_placeholder', location='Bangalore'),
        ]

        self.connection_types = [
            connection_type.ConnectionType(connection_type='Mail'),
            connection_type.ConnectionType(connection_type='LinkedIn'),
            connection_type.ConnectionType(connection_type='GitHub'),
        ]

        self.connections = [
            connection.Connection(url="mailto:nishanth.selvakumar.dev@gmail.com", connection_type_id=1, player_id=1),
            connection.Connection(url="https://www.linkedin.com/in/nishanth-s-dev/", connection_type_id=2, player_id=1),
            connection.Connection(url="https://github.com/nishanth-s-dev", connection_type_id=3, player_id=1),
        ]

        self.projects = [
            project.Project(player_id=1, title='Project 1', image_url='image_url_placeholder', description='Description 1', tech_stack='Tech Stack 1', project_url='https://project1.com', created_on='2021-01-01 00:00:00'),
            project.Project(player_id=1, title='Project 2', image_url='image_url_placeholder', description='Description 2', tech_stack='Tech Stack 2', project_url='https://project2.com', created_on='2021-01-02 00:00:00'),
            project.Project(player_id=1, title='Project 3', image_url='image_url_placeholder', description='Description 3', tech_stack='Tech Stack 3', project_url='https://project3.com', created_on='2021-01-03 00:00:00'),
        ]

    def get_initial_data(self):
        return {
            'players': self.players,
            'connection_types': self.connection_types,
            'connections': self.connections,
            'projects': self.projects,
        }