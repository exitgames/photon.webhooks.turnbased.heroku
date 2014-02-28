import os
from flask import Flask
from webhooks import app

@app.route('/GameProperties')
def GameProperties():
    return 'GameProperties!'
