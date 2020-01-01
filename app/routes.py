from flask import render_template, request, redirect, url_for
from app import app
from users.auth import user_info

@app.route('/index')
@app.route('/')
def index():
	user = user_info(request.cookies.get('idToken'))
	if user == None:
		return redirect(url_for('users.change_user'))
	user = user['users'][0]
	username = user['displayName']
	email    = user['email']
	return render_template('index.html', title='Home', username=username, email=email)