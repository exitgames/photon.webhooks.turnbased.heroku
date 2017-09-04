from app import app

from flask import request, json

@app.route('/GameEvent', methods=['POST'])
def GameEvent():
	jsonRequest = request.get_json(force = True)
	app.logger.info("hook: GameEvent: %s", jsonRequest)
	
	if 'State' in jsonRequest:
		state = jsonRequest['State']
		app.logger.info("hook: GameEvent: saving game: %s, state: %s", game_id, state)
		db.set_game_state(game_id, json.dumps(state))		
	
	return json.jsonify(Message = "",
					ResultCode = 0)

