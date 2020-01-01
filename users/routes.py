from flask import render_template, request, redirect, url_for, flash
from users import users_app
from users.forms import LoginForm, RegisterForm
from users.auth import login, register, user_info, list_of_users

import datetime

@users_app.route('/register', methods=['GET', 'POST'])
@users_app.route('/login', methods=['GET', 'POST'])
def change_user():
	log_form = LoginForm()
	reg_form = RegisterForm()
	user = user_info()
	if user:
		flash('You are already logged in.')
	do = 'login'
	if request.method == 'POST':
		status = res = None
		if 'signin' in request.form:
			do = 'login'
			if log_form.validate_on_submit():
				status, res = login(log_form)
		elif 'signup' in request.form:
			do = 'register'
			if reg_form.validate_on_submit():
				status, res = register(reg_form)
		if status == None:
			return render_template('changeuser.html', do=do, lform=log_form, rform=reg_form)
		if status != 200:
			return render_template('error.html', error=res), status
		id_token = res['idToken']
		response = redirect(url_for('index'))
		expire_cookie = datetime.datetime.now() + datetime.timedelta(seconds=int(res['expiresIn']))
		response.set_cookie('id_token', id_token, expires=expire_cookie)
		user_info(id_token)
		return response
	return render_template('changeuser.html', do=do, lform=log_form, rform=reg_form)

@users_app.route('/logout')
def clear_user():
	response = redirect(url_for('users.change_user'))
	response.set_cookie('id_token', expires=0)
	return response

@users_app.route('/users')
def manage_users():
	user = user_info()
	if not user:
		return redirect(url_for('users.clear_user'))
	if user[2]:
		users = list_of_users()
		return render_template('manageusers.html', title='Users', users=users)
	flash('You are not authorized to view that!')
	return redirect(url_for('index'))