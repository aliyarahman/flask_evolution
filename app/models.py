class User:
	def __init__(self, firstname, lastname, username):
		self.firstname = firstname
		self.lastname = lastname
		self.username = username

class Post:
	def __init__(self, title, content, author_id):
		self.title = title
		self.content = content
		self.author_id = author_id
