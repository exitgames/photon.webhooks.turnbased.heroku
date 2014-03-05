from app import app

from flask import request, json

import db

@app.route('/GameJoin', methods=['POST'])
def GameJoin():
	jsonRequest = request.get_json(force = True)
	app.logger.info("hook: GameJoin: %s", jsonRequest)

	return json.jsonify(Message = "",
					ResultCode = 0)

