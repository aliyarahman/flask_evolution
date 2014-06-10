from app import db


class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	firstname = db.Column(db.String(64))
	lastname = db.Column(db.String(64))
	username = db.Column(db.String(120), unique = True)
	password = db.Column(db.String(120))
	posts = db.relationship('Post', backref = 'author')

	def is_authenticated(self): # Checks to see if the user is signed in
		return True

	def is_active(self): # Checks to see if the user is active - you can shut down accounts without deleting them
		return True

	def is_anonymous(self):
	        return False


	def get_id(self):  # Grabs the user's id number in unicode text format
		return unicode(self.id)	


class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(100))
	content = db.Column(db.Text)
	author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
