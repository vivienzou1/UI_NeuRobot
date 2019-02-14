import gevent.monkey
gevent.monkey.patch_all()
from flask import Flask, render_template
from flask_socketio import SocketIO

import os,sys
import numpy as np
import glob
import pickle
from datetime import datetime
from flask import Flask, request, render_template, redirect, url_for
from werkzeug import secure_filename
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

if __name__=="__main__":
    socketio.run(app,debug=True)
