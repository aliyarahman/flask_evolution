from flask import Flask   # Get some basic Flask tools from the Flask program

app = Flask(__name__)
app.config.from_object('config')  # Settings are in a separate file, and that
									# file is called config.py


from app import views			# When you (Flask) start up, the first place you should go
								# for directions is the views file!
