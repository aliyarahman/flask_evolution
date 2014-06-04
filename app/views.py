# -*- coding: utf-8 -*-

from flask import render_template
from app import app  # Go get stuff we need from the app folder
from models import Post, User

@app.route('/')   # This means that this is the view for the landing page.					# 
def index(): 
	angie = User("Angie", "Rollins", "arollins")
	jason = User("Jason", "Towns", "jtowns")
	users = [angie, jason]
	angies_post = Post("Woke up on the freedom side", "Which side are you on, my people?", 1)
	jasons_post = Post("CSTEM for all", "Educational equity around CSTEM is a significant factor impacting the demographic makeup of today's tech labor force", 2)
	posts = [angies_post, jasons_post]
	return render_template('index.html', users = users, posts = posts)	# Now we load a template instead of just returning some text
