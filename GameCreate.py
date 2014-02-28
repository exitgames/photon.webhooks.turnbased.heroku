import os
from flask import Flask
from webhooks import app

@app.route('/GameCreate')
def GameCreate():
    return 'GameCreate!'
