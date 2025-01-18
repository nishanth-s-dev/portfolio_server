from app.routes import index, player, project, connection


class RouteUtil:
    def __init__(self):
        self.routes = [index, player, project, connection]

    def register_blueprints(self, app):
        for route in self.routes:
            app.register_blueprint(route.bp)