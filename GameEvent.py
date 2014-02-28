import os
from flask import Flask
from webhooks import app

@app.route('/GameEvent')
def GameEvent():
    return 'GameEvent!'
