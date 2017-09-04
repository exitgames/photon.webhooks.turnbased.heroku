from app import app

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
    if 'Type' not in jsonRequest:
		return json.jsonify(Message = "Missing Type.",
					ResultCode = 4)
    if 'ActorNr' not in jsonRequest:
		return json.jsonify(Message = "Missing ActorNr.",
					ResultCode = 6)
					
	game_id = jsonRequest['GameId']
	user_id = jsonRequest['UserId']
	actor_nr = jsonRequest['ActorNr']
    
	if jsonRequest['Type'] == "Load":
		state = db.get_game_state(game_id)

		if state == None:	
			if 'CreateIfNotExists' in jsonRequest and jsonRequest['CreateIfNotExists']:
				app.logger.info("GameId not Found, but this is a join with CreateIfNotExists => returning OK.")
                
                db.set_game_state(jsonRequest['GameId'], json.dumps({'CustomProperties': jsonRequest.CreateOptions.CustomProperties}))
		
		        app.logger.info("hook: GameCreate: saving user game: userid: %s, gameid: %s, actornr: %d", user_id, game_id, actor_nr)
	            db.set_user_game(user_id, game_id, actor_nr)
                
				return json.jsonify(Message = "",
								ResultCode = 0)
			else:
				return json.jsonify(Message = "GameId not Found.",
								ResultCode = 3)
	
		if state != "":
			stateObj = json.loads(state)
			app.logger.info("hook: GameCreate: loaded stateObj: %s", stateObj)
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
                        
		db.set_game_state(jsonRequest['GameId'], json.dumps({'CustomProperties': jsonRequest.CreateOptions.CustomProperties}))
		
		app.logger.info("hook: GameCreate: saving user game: userid: %s, gameid: %s, actornr: %d", user_id, game_id, actor_nr)
	    db.set_user_game(user_id, game_id, actor_nr)
        
		return json.jsonify(Message = "",
						ResultCode = 0)
	