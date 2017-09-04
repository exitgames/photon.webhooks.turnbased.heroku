from app import app

from flask import request, json

import db

@app.route('/GameLeave', methods=['POST'])
def GameLeave():
	jsonRequest = request.get_json(force = True)
	app.logger.info("hook: GameLeave: %s", jsonRequest)

	if 'GameId' not in jsonRequest:
		return json.jsonify(Message = "Missing GameId.",
					ResultCode = 1)
	if 'UserId' not in jsonRequest:
		return json.jsonify(Message = "Missing UserId.",
					ResultCode = 2)
	if 'ActorNr' not in jsonRequest:
		return json.jsonify(Message = "Missing ActorNr.",
					ResultCode = 6)
					
	game_id = jsonRequest['GameId']
	user_id = jsonRequest['UserId']
	actor_nr = jsonRequest['ActorNr']
					
	if 'IsInactive' in jsonRequest and jsonRequest['IsInactive']:
		if actor_nr > 0:
			db.set_user_game(user_id, game_id, jsonRequest['ActorNr'])
	else:
		db.delete_user_game(user_id, game_id)

	return json.jsonify(Message = "",
					ResultCode = 0)
	
