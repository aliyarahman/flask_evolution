from app import db
from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, IntegerField, PasswordField
from wtforms.validators import Required
from models import User, Post

class LoginForm(Form):
        username = TextField('username', validators = [Required(message="We need your username!")])
        password = PasswordField('password', validators = [Required(message="We need your password!")])

        def validate_email(self, field):
                user = self.get_user()
                if user is None:
                        raise ValidationError('Invalid User')
                if user.password != self.password.data:
                        raise ValidationError('Invalid Password')

        def get_user(self):
                return db.session.query(User).filter_by(username=self.username.data).first()

class NewUserForm(Form):
	firstname = TextField('firstname')
	lastname = TextField('lastname')
	username = TextField('username', validators = [Required()])
	password = PasswordField('password', validators = [Required()])

class NewPostForm(Form):
	title = TextField('title')
	content = TextAreaField('content')
	author_id = IntegerField('author_id')
