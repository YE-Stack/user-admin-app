from flask import render_template, request, redirect, url_for, flash
from users import users_app
from users.forms import LoginForm, RegisterForm
from users.auth import login, register, user_info, list_of_users

@users_app.route('/register', methods=['GET', 'POST'])
@users_app.route('/login', methods=['GET', 'POST'])
def change_user():
	log_form = LoginForm()
	reg_form = RegisterForm()
	token = request.cookies.get('idToken')
	if token:
		user = user_info(token)
		if user:
			flash('You are already logged in.')
	do = 'login'
	if request.method == 'POST':
		status = res = None
		if 'signin' in request.form:
			do = 'login'
			if log_form.validate_on_submit():
				print('Login Form')
				status, res = login(log_form)
		elif 'signup' in request.form:
			do = 'register'
			if reg_form.validate_on_submit():
				print('Register Form')
				status, res = register(reg_form)

		if status == None:
			return render_template('changeuser.html', do=do, lform=log_form, rform=reg_form)

		print(status, res)
		if status != 200:
			return render_template('error.html', error=res), status
		response = redirect(url_for('index'))
		response.set_cookie('idToken', res['idToken'])
		return response

	return render_template('changeuser.html', do=do, lform=log_form, rform=reg_form)

@users_app.route('/logout')
def clear_user():
	response = redirect(url_for('users.change_user'))
	response.set_cookie('idToken', '', expires=0)
	return response

@users_app.route('/users')
def manage_users():
	token = request.cookies.get('idToken')
	if token:
		user = user_info(token)
		if user and user.get('admin'):
			users = list_of_users()
			return render_template('manageusers.html', title='Users', users=users)
	flash('You are not authorized to view that!')
	return redirect(url_for('index'))