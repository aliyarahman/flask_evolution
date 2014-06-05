from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, IntegerField
from wtforms.validators import Required

class NewUserForm(Form):
	firstname = TextField('firstname')
	lastname = TextField('lastname')
	username = TextField('username', validators = [Required()])

class NewPostForm(Form):
	title = TextField('title')
	content = TextAreaField('content')
	author_id = IntegerField('author_id')
