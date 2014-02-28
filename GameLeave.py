import os
from flask import Flask
from webhooks import app

@app.route('/GameLeave')
def GameLeave():
    return 'GameLeave!'
