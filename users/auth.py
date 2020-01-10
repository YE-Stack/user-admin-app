import os
import sys
import requests

from firebase_admin import auth
from firebase_admin._auth_utils import EmailAlreadyExistsError, UserNotFoundError

API_KEY = os.environ.get('API_KEY')
if not API_KEY:
	print('API_KEY not set.')
	sys.exit(1)

SIGNIN_URL = f'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}'
HEADERS = {'Content-Type': 'application/json'}

def register(form):
	try:
		auth.create_user(email=form.email.data, email_verified=False,
		                 password=form.password.data, display_name=form.username.data)
	except EmailAlreadyExistsError:
		return 400, 'The user with the provided email already exists.'
	return login(form)

def login(form):
	json_form = {'email': form.email.data,
	             'password': form.password.data,
	             'returnSecureToken': True}
	response = requests.post(SIGNIN_URL, headers=HEADERS, json=json_form)
	status = response.status_code
	json_response = response.json()
	if status == 200:
		print(json_response)
		return 200, json_response
	return status, json_response['error']['message']

def verify(id_token):
	error = None
	if id_token is None:
		return 400, error
	try:
		user = auth.verify_id_token(id_token, check_revoked=True)
		return 200, user
	except auth.RevokedIdTokenError:
		error = 'Session Expired. Login Again.'
	except auth.InvalidIdTokenError:
		error = 'Session Invalid. Login Again.'
	return 400, error

def list_of_users():
	users = auth.list_users()
	return users

def set_admin(uid, admin):
	try:
		user = auth.get_user(uid)
		claims = user.custom_claims
		if not claims:
			claims = {}
		claims['admin'] = (admin == 1)
		auth.set_custom_user_claims(user.uid, claims)
		auth.revoke_refresh_tokens(uid)
	except UserNotFoundError:
		return 'User Not Found.'
	return None
