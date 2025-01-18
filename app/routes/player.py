from flask import Blueprint

bp = Blueprint('player', __name__, url_prefix='/api')


@bp.route('/players')
def get_all_players():
    response_json = {
        "message": "Players endpoint.",
    }
    return response_json, 200

@bp.route('/players/<player_id>')
def get_player_with_id(player_id):
    response_json = {
        "message": f"Player endpoint with id: {player_id}.",
    }
    return response_json, 200