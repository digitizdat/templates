#!/usr/bin/env python
#
# controller.py
#
# This is the main Flask body.
#
# TEMPLATE: Replace every occurrence of MYAPP with your application name (e.g.
# sensibility, imturk, etc.).
#
# Jan 21, 2015 - Martin McGreal
#

from __future__ import print_function
from flask import Flask, send_from_directory, Response, request
from flask_cors import CORS
import uuid
import os
from numpy import random
import logging
import json
import eventlet


# Flask configuration variables
SERVER_NAME = "MYAPP.cty.io"
app = Flask(__name__)
app.debug = True
cors = CORS(app, resources=r'/*', headers='Content-Type')


# IMTurk config vars
logfile = '/opt/MYAPP/log/MYAPP.log'

# Global logging object (setup happens in __main__)
logger = logging.getLogger('MYAPP')
logger.setLevel(logging.DEBUG)

# Create a file handler
fh = logging.FileHandler(logfile)
fh.setLevel(logging.DEBUG)

# Create a console handler
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# Create a formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s %(name)s[%(process)d] %(levelname)s: %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)


# Routes

@app.route('/hello', methods=['GET', 'POST'])
def checkme():
    """Test WS"""
    print("checkme: Received a request: "+str(request.data))
    if request.method == 'POST':
        return Response(json.dumps({'status': request.data}), mimetype='application/json')
    if request.method == 'GET':
        return Response(json.dumps({'status': 'Hello!'}))


@app.route('/favicon.ico')
def favicon():
    return send_from_directory('../img/', 'MYAPP.ico',
                                   mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

