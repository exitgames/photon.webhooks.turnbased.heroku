from webhooks import app

from flask import request, json

import db

@app.route('/GameJoin', methods=['POST'])
def GameJoin():
	jsonRequest = request.get_json(force = True)
	app.logger.info("hook: GameJoin: %s", jsonRequest)

	if 'GameId' not in jsonRequest:
		return json.jsonify(Message = "Missing GameId.",
					ResultCode = 1)
	if 'UserId' not in jsonRequest:
		return json.jsonify(Message = "Missing UserId.",
					ResultCode = 2)
					
	game_id = jsonRequest['GameId']
	user_id = jsonRequest['UserId']
					
	if 'IsInactive' not in jsonRequest or not jsonRequest['IsInactive']:
		db.delete_user_game(user_id, game_id)
	else:
		if 'ActorNr' in jsonRequest and jsonRequest['ActorNr'] > 0:
			db.set_user_game(user_id, game_id, jsonRequest['ActorNr'])

	return json.jsonify(Message = "",
					ResultCode = 0)
