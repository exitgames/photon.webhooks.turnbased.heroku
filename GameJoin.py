import os
from flask import Flask
from webhooks import app

@app.route('/GameJoin')
def GameJoin():
    return 'GameJoin!'
