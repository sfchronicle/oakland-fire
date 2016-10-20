from flask import Flask
from flask.ext.frozen import Freezer
from flask.ext.assets import Environment

# Create application
app = Flask(__name__)

# asset management
assets =  Environment(app)
# building
freezer = Freezer(app)