from webhooks import app

from flask import request, json

@app.route('/GameLeave', methods=['POST'])
def GameLeave():
	jsonRequest = request.get_json(force = True)
	app.logger.info("hook: GameLeave: %s", jsonRequest)
	
	return json.jsonify(Message = "",
					ResultCode = 0)

