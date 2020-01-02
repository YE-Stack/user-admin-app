from flask import render_template, request, redirect, url_for
from app import app
from users.auth import user_info

@app.route('/index')
@app.route('/')
def index():
	token = request.cookies.get('id_token')
	if token:
		user = user_info(token)
		if not user:
			return redirect(url_for('users.clear_user'))
		return render_template('index.html', title='Home', username=user[0], email=user[1], admin=user[2])
	return redirect(url_for('users.change_user'))

@app.errorhandler(404)
def page_not_found(e):
	return render_template('error.html', error=e), 404