from app import app

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
    if 'ActorNr' not in jsonRequest:
		return json.jsonify(Message = "Missing ActorNr.",
					ResultCode = 6)
    
    user_id = jsonRequest['UserId']
	actor_nr = jsonRequest['ActorNr']
    game_id = jsonRequest['GameId']
    
    app.logger.info("hook: GameJoin: saving user game: userid: %s, gameid: %s, actornr: %d", user_id, game_id, actor_nr)
	db.set_user_game(user_id, game_id, actor_nr)
    
	return json.jsonify(Message = "",
					ResultCode = 0)

