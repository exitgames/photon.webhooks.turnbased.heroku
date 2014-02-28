import os
from flask import Flask
from webhooks import app

@app.route('/GameClose')
def GameClose():
    return 'GameClose!'
