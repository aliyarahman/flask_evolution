# -*- coding: utf-8 -*-

from flask import render_template
from app import app  # Go get stuff we need from the app folder


@app.route('/')   # This means that this is the view for the landing page.					# 
def index():  
	return render_template('index.html')	# Now we load a template instead of just returning some text
