from app import app

from flask import request, json

import db

@app.route('/GameClose', methods=['POST'])
def GameClose():
	jsonRequest = request.get_json(force = True)
	app.logger.info("hook: GameClose: %s", jsonRequest)

	if 'GameId' not in jsonRequest:
		return json.jsonify(Message = "Missing GameId.",
					ResultCode = 1)
	if 'Type' not in jsonRequest:
		return json.jsonify(Message = "Missing Type.",
					ResultCode = 4)
	if 'ActorCount' not in jsonRequest:
		return json.jsonify(Message = "Missing ActorCount.",
					ResultCode = 7)

	game_id = jsonRequest['GameId']
	if 'State' not in jsonRequest:
		if jsonRequest['ActorCount'] > 0:
			app.logger.error("hook: GameClose: Missing State.")
			return json.jsonify(Message = "Missing State.",
						ResultCode = 8)

		app.logger.info("hook: GameClose: all actors left, we delete the game: %s", game_id)
		db.delete_game_state(game_id)
		return json.jsonify(Message = "",
						ResultCode = 0)

	for v in jsonRequest['State']['ActorList']:
		user_id = v['UserId']
		actor_nr = v['ActorNr']
		app.logger.info("hook: GameClose: saving user game: userid: %s, gameid: %s, actornr: %d", user_id, game_id, actor_nr)
		db.set_user_game(user_id, game_id, actor_nr)

	state = jsonRequest['State']
	app.logger.info("hook: GameClose: saving game: %s, state: %s", game_id, state)
	db.set_game_state(game_id, json.dumps(state))

	return json.jsonify(Message = "",
					ResultCode = 0)

