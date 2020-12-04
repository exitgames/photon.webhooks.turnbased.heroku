import os
import db

from flask import Flask, request

app = Flask(__name__)
app.debug = True 
db.set_game_state(1, 2);

@app.route('/')
def hello():
    return 'Hello World!'

from webhooks import GameClose
from webhooks import GameCreate
from webhooks import GameEvent
from webhooks import GameJoin
from webhooks import GameLeave
from webhooks import GameProperties
from webhooks import GetGameList
