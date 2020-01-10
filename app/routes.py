from flask import request, render_template

from users.auth import verify
from users.session import store_user_info, clear_user_info

from app import APP

@APP.route('/index')
@APP.route('/')
def index():
	response = render_template('index.html', title='Welcome')
	id_token = request.cookies.get('id_token')
	if id_token:
		status, user = verify(id_token)
		if status == 200:
			store_user_info(user)
			response = render_template('index.html', title='Welcome', username=user.get('name'),
			                           email=user.get('email'), admin=user.get('admin'))
		else:
			response = clear_user_info(response)
	return response

@APP.errorhandler(404)
def not_found(error):
	return render_template('error.html', title='404', status='404 Not Found',
	                       error=error.description)
