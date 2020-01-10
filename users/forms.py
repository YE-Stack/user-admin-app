from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
	submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=1)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired(),
	                                                 EqualTo('confirm',
	                                                         message='Passwords do not match.'),
	                                                 Length(min=6)])
	confirm = PasswordField('Confirm Password')
	submit = SubmitField('Sign Up')
