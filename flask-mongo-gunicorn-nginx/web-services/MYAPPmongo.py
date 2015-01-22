#
# MYAPPmongo.py
#
# Here is the MongoDB-Flask interface.
#
# TEMPLATE: Replace every occurrence of MYAPP with your app's name.
#
# Jan 21, 2015 - Martin McGreal
#

from flask import Flask, request, Response
from flask.ext.mongoengine import MongoEngine
# Enable the next line for debugging only.  Requires Flask-DebugToolbar.
#from flask_debugtoolbar import DebugToolbarExtension
#from werkzeug.datastructures import ImmutableMultiDict
#from wtforms.validators import *
import json
from MYAPP.utils import getval
from MYAPP.MYAPPdoco import *
# You'll need to use this for complicated (compound) Mongo queries.
#from mongoengine import Q


# Some initialization variables
mongocf = "/opt/MYAPP/etc/mongo.cf"

# Initialize Flask and load the MongoDB interface.
app = Flask(__name__)
app.config.from_pyfile(mongocf)
db = MongoEngine(app)


# Enable the following lines for debugging only
#app.debug = True
#app.config['DEBUG_TB_PANELS'] = 'flask.ext.mongoengine.panels.MongoDebugPanel'


# Functions that interface with MongoDB

