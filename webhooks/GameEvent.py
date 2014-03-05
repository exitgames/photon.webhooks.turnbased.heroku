from app import app

from flask import request, json

@app.route('/GameEvent', methods=['POST'])
def GameEvent():
	jsonRequest = request.get_json(force = True)
	app.logger.info("hook: GameEvent: %s", jsonRequest)
	
	return json.jsonify(Message = "",
					ResultCode = 0)

