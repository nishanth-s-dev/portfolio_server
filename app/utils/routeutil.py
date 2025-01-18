from app.routes import index


class RouteUtil:
    def __init__(self):
        self.routes = [index]

    def register_blueprints(self, app):
        for route in self.routes:
            app.register_blueprint(route.bp)