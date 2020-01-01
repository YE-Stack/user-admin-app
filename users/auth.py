from flask import flash
from requests import post
from firebase_admin import auth
from os import environ

api_key = environ.get('API_KEY')
signin_url         = 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=' + api_key
# signup_url         = 'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=' + api_key
# update_profile_url = 'https://identitytoolkit.googleapis.com/v1/accounts:update?key=' + api_key
# user_data_url      = 'https://identitytoolkit.googleapis.com/v1/accounts:lookup?key=' + api_key
headers = {'Content-Type': 'application/json'}

def register(form):
	try:
		auth.create_user (
			email=form.email.data,
			email_verified=False,
			password=form.password.data,
			display_name=form.username.data
		)
	except Exception as err:
		print(str(err))
		return 400, str(err)
	return login(form)

def login(form):
	email = form.email.data
	passw = form.password.data
	json_data = {
		'email'            : email,
		'password'         : passw,
		'returnSecureToken': 'true'
	}
	res = post(signin_url, headers=headers, json=json_data)
	status = res.status_code
	if status == 200:
		res = res.json()
	else:
		res = res.json()['error']['message']
	return status, res

def user_info(id_token):
	if id_token:
		try:
			user = auth.verify_id_token(id_token, check_revoked=True)
			return user
		except auth.RevokedIdTokenError:
			flash('Session Expired. Login Again')
		except auth.InvalidIdTokenError:
			flash('Session Invalid. Login Again')

	return None

def list_of_users():
	users = auth.list_users()
	return users