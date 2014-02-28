import os
from flask import Flask

app = Flask(__name__)

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
