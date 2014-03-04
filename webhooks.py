import os
from flask import Flask, request

app = Flask(__name__)
app.debug = True 
@app.route('/')
def hello():
    return 'Hello World!'

import GameClose
import GameCreate
import GameEvent
import GameJoin
import GameLeave
import GameLoad
import GameProperties
import GetGameList
