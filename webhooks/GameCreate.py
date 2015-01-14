from app import app

from flask import request, json

import db

@app.route('/GameCreate', methods=['POST'])
def GameCreate():
	jsonRequest = request.get_json(force = True)
	app.logger.info("hook: GameCreate: %s", jsonRequest)
	if 'Type' not in jsonRequest:
		return json.jsonify(Message = "Missing Type.",
					ResultCode = 4)
	if 'GameId' not in jsonRequest:
		return json.jsonify(Message = "Missing GameId.",
					ResultCode = 1)
	if 'UserId' not in jsonRequest:
		return json.jsonify(Message = "Missing UserId.",
					ResultCode = 2)
					
	game_id = jsonRequest['GameId']
	user_id = jsonRequest['UserId']

	if jsonRequest['Type'] == "Load":
		state = db.get_game_state(game_id)

		if state == None:	
			if 'CreateIfNotExists' in jsonRequest and jsonRequest['CreateIfNotExists']:
				app.logger.info("GameId not Found, but this is a join with CreateIfNotExists => returning OK.")
				return json.jsonify(Message = "",
								ResultCode = 0)
			else:
				return json.jsonify(Message = "GameId not Found.",
								ResultCode = 3)
	
		if state != "":
			stateObj = json.loads(state)
			app.logger.info("hook: GameLoad: stateObj: %s", stateObj)
			return json.jsonify(Message = "",
						ResultCode = 0,
						State = stateObj)
		else:
			return json.jsonify(Message = "",
						ResultCode = 0)

	else:
		if db.game_state_exists(game_id):
			return json.jsonify(Message = "Game already exists.",
						ResultCode = 5)
		
		db.set_game_state(jsonRequest['GameId'], "")
		
		return json.jsonify(Message = "",
						ResultCode = 0)
	