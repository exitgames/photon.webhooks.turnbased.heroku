import os
from flask import Flask, request

app = Flask(__name__)
app.debug = True 
@app.route('/')
def hello():
    return 'Hello World!'

from webhooks import GameClose
from webhooks import GameCreate
from webhooks import GameEvent
from webhooks import GameJoin
from webhooks import GameLeave
from webhooks import GameLoad
from webhooks import GameProperties
from webhooks import GetGameList
