from app import app

from flask import request, json

import db

@app.route('/GetGameList', methods=['POST'])
def GetGameList():
	jsonRequest = request.get_json(force = True)
	app.logger.info("hook: GetGameList: %s", jsonRequest)

	if 'UserId' not in jsonRequest:
		return json.jsonify(Message = "Missing UserId.",
					ResultCode = 1)

	user_id = jsonRequest['UserId']
	game_list = db.get_user_game_list(user_id)
	list = {}
	for game_id, actor_nr in game_list:
		app.logger.info("%s -> %d", game_id, actor_nr)
		if db.game_state_exists(game_id):
			list[game_id] = actor_nr
		else:
			db.delete_user_game(user_id, game_id)			


	return json.jsonify(ResultCode = 0, Mesage = "", Data = list)
