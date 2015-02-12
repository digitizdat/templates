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
from flask_cors import cross_origin  # Requires Flask-CORS >= 1.10.3
import re
import logging
import json


# Flask configuration variables
SERVER_NAME = "MYAPP.cty.io"
app = Flask('MYAPP')
app.debug = True

# Create our CORS origins regexp
re_origins = re.compile(u"http://.*\.cty\.io")

# MYAPP log file
logfile = '/opt/MYAPP/log/MYAPP.log'

# Configure the Flask app logger object
app.logger.setLevel(logging.DEBUG)

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
app.logger.addHandler(fh)
app.logger.addHandler(ch)


# Routes

@app.route('/hello', methods=['GET', 'POST'])
@cross_origin(origins=[re_origins])
def checkme():
    """Test WS"""
    app.logger.debug("checkme: Received a request: "+str(request.data))
    if request.method == 'POST':
        return Response(json.dumps({'status': request.data}), mimetype='application/json')
    if request.method == 'GET':
        return Response(json.dumps({'status': 'Hello!'}))


@app.route('/favicon.ico')
@cross_origin(origins=[re_origins])
def favicon():
    return send_from_directory('../img/', 'MYAPP.ico',
                                   mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

