from flask import render_template, request, redirect, url_for
from users import users_app
from users.forms import LoginForm, RegisterForm
from users.auth import login, register, user_info

@users_app.route('/register', methods=['GET', 'POST'])
@users_app.route('/login', methods=['GET', 'POST'])
def change_user():
	log_form = LoginForm()
	reg_form = RegisterForm()
	logged_in = False
	token = request.cookies.get('idToken')
	if token:
		user = user_info(token)
		if user:
			logged_in = True
	do = 'login'
	if request.method == 'POST':
		if 'signin' in request.form:
			do = 'login'
			if log_form.validate_on_submit():
				print('Login Form')
				status, res = login(log_form)
				print(status, res)
				if status != 200:
					return res['error']['message'], status
				user = user_info(res['idToken'])
				response = redirect(url_for('index'))
				response.set_cookie('idToken', res['idToken'])
				return response
		elif 'signup' in request.form:
			do = 'register'
			if reg_form.validate_on_submit():
				print('Register Form')
				status, res, user = register(reg_form)
				print(status, res)
				print(user.status_code, user.json())
				response = redirect(url_for('index'))
				response.set_cookie('idToken', res['idToken'])
				return response
		return render_template('changeuser.html', do=do, logged_in=logged_in, lform=log_form, rform=reg_form)
	return render_template('changeuser.html', do=do, logged_in=logged_in, lform=log_form, rform=reg_form)

@users_app.route('/logout')
def clear_user():
	response = redirect(url_for('users.change_user'))
	response.set_cookie('idToken', '', expires=0)
	return response