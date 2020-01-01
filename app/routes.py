from flask import render_template, request, redirect, url_for
from firebase_admin import auth
from app import app
from users.auth import user_info

@app.route('/index')
@app.route('/')
def index():
	id_token = request.cookies.get('idToken')
	user = user_info(id_token)
	if not user:
		return redirect(url_for('users.clear_user'))
	print(user)
	username = user.get('name')
	email    = user.get('email')
	admin    = user.get('admin')
	return render_template('index.html', title='Home', username=username, email=email, admin=admin)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('error.html', error=e), 404