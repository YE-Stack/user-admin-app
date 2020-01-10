from flask import request, render_template, redirect, url_for, flash

from users import USERS
from users.forms import LoginForm, RegisterForm
from users.auth import login, register, verify, list_of_users
from users.session import store_id_token, clear_user_info

@USERS.route('/signin', methods=['GET', 'POST'])
def signin():
	form = LoginForm()
	auth_errors = None
	id_token = request.cookies.get('id_token')
	if id_token:
		flash('There is an active session.')
	if request.method == 'POST':
		if form.validate_on_submit():
			status, response = login(form)
			if status == 200:
				success = redirect(url_for('index'))
				success = store_id_token(success, response)
				return success
			auth_errors = [response]
	return render_template('signin.html', auth_errors=auth_errors, title='Sign In', form=form)

@USERS.route('/signup', methods=['GET', 'POST'])
def signup():
	form = RegisterForm()
	auth_errors = None
	id_token = request.cookies.get('id_token')
	if id_token:
		flash('There is an active session.')
	if request.method == 'POST':
		if form.validate_on_submit():
			status, response = register(form)
			if status == 200:
				success = redirect(url_for('index'))
				success = store_id_token(success, response)
				return success
			auth_errors = [response]
	return render_template('signup.html', auth_errors=auth_errors, title='Sign Up', form=form)

@USERS.route('/signout')
def signout():
	id_token = request.cookies.get('id_token')
	response = redirect(url_for('users.signin'))
	if not id_token:
		flash('You are not signed in!')
		return response
	response = clear_user_info(response)
	flash('You have been signed out.')
	return response

@USERS.route('/manage', methods=['GET'])
def manage():
	id_token = request.cookies.get('id_token')
	status, user = verify(id_token)
	if status == 200:
		if user.get('admin'):
			return render_template('manage.html', title='Manage Users', users=list_of_users())
		flash('You are not authorized to view that!')
		return redirect(url_for('index'))
	flash('You are not signed in!')
	return redirect(url_for('users.signin'))
