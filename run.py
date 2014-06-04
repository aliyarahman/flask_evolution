# -*- coding: utf-8 -*-
#!flask/bin/python

from app import app    # Go get tools from the app folder
app.run(debug = True) # We set debug = True so that we can see our changes
						# as we make them while developing.
						# We'll set this to False when we deploy, to 
						# save us from hacking!
