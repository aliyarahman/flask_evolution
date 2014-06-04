========================
flask_evolution - Our Flask learning app
==========================


In this commit, we've given the app more purpose - it now has users, who can make short blog posts.

To handle the user and post data, we've added a models.py file, where we're declaring some classes - User and Post. At this point, we aren't
connecting to a database yet. Instead, we're manually typing a couple of pieces of sample data (two uses and two posts) directly into views.py
and passing them along to the index.html template to display on the page using two separate for loops.

We've also further styled this landing page to help us see the difference between different kinds of data.
