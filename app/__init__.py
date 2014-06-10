from flask import Flask   # Get some basic Flask tools from the Flask program
from flask.ext.login import LoginManager  #Get the tools we need to do logins
from flask.ext.sqlalchemy import SQLAlchemy	# We installed SQLAlchemy on our virtual environment, so we want to import the tools to use


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)			# This tells Flask to start up the connection to the database when we start up the app

lm = LoginManager()			# Turn on the login manager
lm.init_app(app)
lm.login_view = "login"			# Let it know that our 'login' view is where the user should be redirected if they try to access a protected page but aren't logged in



from app import views, models		# Now that we have models, we want to make them easily importable when we start up the app
