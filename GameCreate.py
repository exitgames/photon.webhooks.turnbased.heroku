from webhooks import app

from flask import request, json

import db

@app.route('/GameCreate', methods=['POST'])
def GameCreate():
	jsonRequest = request.get_json(force = True)
	app.logger.info("hook: GameCreate: %s", jsonRequest)

	if 'GameId' not in jsonRequest:
		return json.jsonify(Message = "Missing GameId.",
					ResultCode = 1)
	if 'UserId' not in jsonRequest:
		return json.jsonify(Message = "Missing UserId.",
					ResultCode = 2)
					
	game_id = jsonRequest['GameId']
	user_id = jsonRequest['UserId']

	if db.game_state_exists(game_id):
		return json.jsonify(Message = "Game already exists.",
					ResultCode = 3)
	
	db.set_game_state(jsonRequest['GameId'], "")
	
	return json.jsonify(Message = "",
					ResultCode = 0)
	