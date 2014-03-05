from app import app

from flask import request, json

import db

@app.route('/GameClose', methods=['POST'])
def GameClose():
	jsonRequest = request.get_json(force = True)
	app.logger.info("hook: GameClose: %s", jsonRequest)

	game_id = jsonRequest['GameId']
	if 'State' not in jsonRequest:
		
		if jsonRequest['ActorCount'] > 0:
			app.logger.error("hook: GameClose: Missing State.")
			return json.jsonify(Message = "Missing State.",
						ResultCode = 1)

		app.logger.info("hook: GameClose: all actors left, we delete the game: %s", game_id)
		db.delete_game_state(game_id)
		return json.jsonify(Message = "",
						ResultCode = 0)

	if 'State2' in jsonRequest:
		for v in jsonRequest['State2']['ActorList']:
			user_id = v['UserId']
			actor_nr = v['ActorNr']
			app.logger.info("hook: GameClose: saving user game: userid: %s, gameid: %s, actornr: %d", user_id, game_id, actor_nr)
			db.set_user_game(user_id, game_id, actor_nr)
	
	state = jsonRequest['State']
	app.logger.info("hook: GameClose: saving game: %s, state: %s", game_id, state)
	db.set_game_state(game_id, json.dumps(state))

	return json.jsonify(Message = "",
					ResultCode = 0)

