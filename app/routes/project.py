from flask import Blueprint
from app.utils.dbutil import DBUtil

dbutil = DBUtil()
bp = Blueprint('project', __name__, url_prefix='/api')


@bp.route('/projects')
def get_all_projects():
    from app.models.project import Project
    projects = dbutil.execute_query(Project).all()
    response = []
    for project in projects:
        response.append(project.to_dict())
    return response, 200

@bp.route('/projects/<project_id>')
def get_project_with_id(project_id):
    from app.models.project import Project
    response = {}
    query_res = dbutil.execute_query(Project).filter_by(project_id=project_id).first()
    if query_res is not None:
        response = query_res.to_dict()
        return response, 200
    else:
        response['message'] = 'Project not found'
        return response, 404