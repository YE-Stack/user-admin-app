from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class LoginForm(FlaskForm):
	email = StringField('Email',validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=1)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	# phone
	admin = BooleanField('Are you Admin?')
	password = PasswordField('Password', [DataRequired(), EqualTo('confirm', message='Passwords do not match'), Length(min=6, message='Password must be at least 6 characters long.')])
	confirm = PasswordField('Confirm Password')
	submit = SubmitField('Sign Up')