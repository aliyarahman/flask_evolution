# -*- coding: utf-8 -*-

from flask import render_template
from app import app  # Go get stuff we need from the app folder
from models import Post, User

@app.route('/')   # This means that this is the view for the landing page.					# 
def index(): 
	users = User.query.all()
	posts = Post.query.all()
	return render_template('index.html', users = users, posts = posts)	# Now we load a template instead of just returning some text
