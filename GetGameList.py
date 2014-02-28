import os
from flask import Flask
from webhooks import app

@app.route('/GetGameList')
def GetGameList():
    return 'GetGameList!'
