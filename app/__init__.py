from flask import Flask   # Get some basic Flask tools from the Flask program

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy	# We installed SQLAlchemy on our virtual environment, so we want to import the tools to use


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)			# This tells Flask to start up the connection to the database when we start up the app

from app import views, models		# Now that we have models, we want to make them easily importable when we start up the app
