from app import app

from flask import request, json

@app.route('/GameProperties', methods=['POST'])
def GameProperties():
	jsonRequest = request.get_json(force = True)
	app.logger.info("hook: GameProperties: %s", jsonRequest)
	
	return json.jsonify(Message = "",
					ResultCode = 0)

