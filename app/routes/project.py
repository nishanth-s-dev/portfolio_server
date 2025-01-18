from flask import Blueprint

bp = Blueprint('project', __name__, url_prefix='/api')


@bp.route('/projects')
def get_all_projects():
    response_json = {
        "message": f"Projects endpoint..",
    }
    return response_json, 200

@bp.route('/projects/<project_id>')
def get_project_with_id(project_id):
    response_json = {
        "message": f"Projects endpoint with player id: {project_id}.",
    }
    return response_json, 200
