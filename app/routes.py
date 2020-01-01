from flask import render_template, request, redirect, url_for
from firebase_admin import auth
from app import app
from users.auth import user_info

@app.route('/index')
@app.route('/')
def index():
	id_token = request.cookies.get('idToken')
	user = user_info(id_token)
	if user == None:
		return redirect(url_for('users.change_user'))
	print(user)
	username = user.get('name')
	email    = user.get('email')
	admin    = user.get('admin')
	return render_template('index.html', title='Home', username=username, email=email, admin=admin)