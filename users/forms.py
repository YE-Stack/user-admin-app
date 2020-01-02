from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

password_length_error = 'Password must be at least 6 characters long.'
class LoginForm(FlaskForm):
	email = StringField('Email',validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[
		DataRequired(),
		Length(min=6, message=password_length_error)])
	submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=1)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	# phone
	password = PasswordField('Password', validators=[
		DataRequired(),
		EqualTo('confirm', message='Passwords do not match'),
		Length(min=6, message=password_length_error)])
	confirm = PasswordField('Confirm Password')
	submit = SubmitField('Sign Up')