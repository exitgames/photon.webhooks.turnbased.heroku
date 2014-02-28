import os
from flask import Flask
from webhooks import app

@app.route('/GameLoad')
def GameLoad():
    return 'GameLoad!'
