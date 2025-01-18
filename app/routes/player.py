from flask import Blueprint, jsonify, json
from app.utils.dbutil import DBUtil

bp = Blueprint('player', __name__, url_prefix='/api')

dbutil = DBUtil()

@bp.route('/players')
def get_all_players():
    from app.models.player import Player
    players = dbutil.execute_query(Player).all()

    response = []
    for player in players:
        response.append(player.to_dict())

    return response, 200

@bp.route('/players/<player_id>')
def get_player_with_id(player_id):
    from app.models.player import Player
    response = {}
    query_res = dbutil.execute_query(Player).filter_by(player_id=player_id).first()
    if query_res is not None:
        response = query_res.to_dict()
        return response, 200
    else:
        response['message'] = 'Player not found'
        return response, 404