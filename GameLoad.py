from webhooks import app

from flask import request, json

import db

@app.route('/GameLoad', methods=['POST'])
def GameLoad():
	jsonRequest = request.get_json(force = True)
	app.logger.info("hook: GameLoad: %s", jsonRequest)

	if 'GameId' not in jsonRequest:
		return json.jsonify(Message = "Missing GameId.",
					ResultCode = 1)
	if 'UserId' not in jsonRequest:
		return json.jsonify(Message = "Missing UserId.",
					ResultCode = 2)

	game_id = jsonRequest['GameId']
					
	state = db.get_game_state(game_id)

	if state == None:	
		if 'ActorNr' in jsonRequest and jsonRequest['ActorNr'] == 0:
			log("GameId not Found, but this is a join with CreateIfNotExists => returning OK.")
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
