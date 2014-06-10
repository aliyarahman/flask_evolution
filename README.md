========================
flask_evolution - Our Flask learning app
==========================


In this commit, we: 
- Add the ability for users to sign up for accounts and then sign in and out using a password.
- Password protect the add_posts page so that only logged in users can post
- Add code to make any post added during a user's session automatically place that user's id in its author_id field.
- Add a logout button


To do this, we have to:
- Install flask-login on the virtual environment
- Configure the app to use and load LoginManager when it launches
- Create a template for the login page
- Add the login form to forms.py
- Modify views to take into account our new login and logout functionality.
- Add authentication methods to our User in models.py
- Remove the field for manually adding author_id to the add_post template (now we just add that automatically in the add_post view)



At this point the application is capable of:
- Launching and returning HTML through the browser screen
- Rendering an HTML template to the browser screen
- Using template inheritance to build every template off of a base.html so that we don't have to repeat the header on every template that holds content
- Connecting to a database, querying data from it, and displaying it by rendering a template in the browser
- Allowing users to enter data (new users and posts) through a form, which is committed to the database (so that it will show up when the view uploads)
