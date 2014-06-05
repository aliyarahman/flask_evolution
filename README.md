========================
flask_evolution - Our Flask learning app
==========================


In this commit, we've made the big jump to storing our data in a Postgres database instead of manually typing in sample posts and users
into our views.py file.

This means we've had to modify config.py and __init__.py to tailor our app to find the database on this local computer. Once we did that, we were able to create tables in the Postgres database that correspond to our blueprint that we wrote in models.py. Then, we add sample data using the Python shell (which is not viewable in the code on this repo).

It also means we've installed SQLAlcehmy and Flask-SQLAlchemy onto the virtual environment. You can see these changes in the requirements.txt file.

And - this also means we are modifying our models.py file to now use SQLAlchemy's awesome tools that allow us to talk to a SQL 
database without having to actually type any SQL (we can speak Python to it and SQLAlchemy does the translating).

And finally, we are now calling on the database to get our data in the views.py file and passing the results it gives us into the templates. But, notice that
we haven't changed anything in our html or css files - these are all backend changes. The data still displays exactly the same way as far as the front end is concerned.

