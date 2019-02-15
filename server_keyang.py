from flask import Flask, render_template
from flask_socketio import SocketIO
import json

import os,sys
import numpy as np
import glob
import pickle
from datetime import datetime
from flask import Flask, request, render_template, redirect, url_for
import uuid
from flask_socketio import SocketIO
from test import demo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index_keyang.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    # print("send to demo:", json.get('message'))
    results = demo(json.get('message'))
    if results:
        res = {'user_name': '', 'message': results[0], "recommend": results[1],
               "related": results[2] }
        res_0 = {'user_name': '', 'message': results[0]}
        res_1 = {'user_name': 'Visual Assistant:', 'message': results[1]}
        res_2 = {'user_name': 'Related Questions:', 'message': results[2]}
        print ("res-----", res)
        # socketio.emit('my response', res, callback=messageReceived)
        socketio.emit('my response', res_0, callback=messageReceived)
        socketio.emit('my response', res_1, callback=messageReceived)
        socketio.emit('my response', res_2, callback=messageReceived)

if __name__ == "__main__":
    socketio.run(app, debug=True)
