from app import app

from flask import request, json

import db

@app.route('/GetGameList', methods=['POST'])
def GetGameList():
	jsonRequest = request.get_json(force = True)
	app.logger.info("hook: GetGameList: %s", jsonRequest)

	if 'UserId' not in jsonRequest:
		return json.jsonify(Message = "Missing UserId.",
					ResultCode = 2)

	user_id = jsonRequest['UserId']
	game_list = db.get_user_game_list(user_id)
	list = {}
	for game_id, actor_nr in game_list:
		app.logger.info("%s -> %d", game_id, actor_nr)
		if db.game_state_exists(game_id):
			state = db.get_game_state(game_id)
			list[game_id] = {
				'ActorNr': actor_nr, 
			}
			if state != "":
				stateObj = json.loads(state)
				list[game_id]['Properties'] = stateObj['CustomProperties']

		else:
			db.delete_user_game(user_id, game_id)


	return json.jsonify(ResultCode = 0, Message = "", Data = list)
