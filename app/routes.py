from flask import request, render_template

from users.auth import verify
from users.routes import store_user_info, clear_user_info

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
