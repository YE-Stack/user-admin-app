from requests import post
from os import environ

api_key = environ.get('API_KEY')
signin_url         = 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=' + api_key
signup_url         = 'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=' + api_key
update_profile_url = 'https://identitytoolkit.googleapis.com/v1/accounts:update?key=' + api_key
user_data_url      = 'https://identitytoolkit.googleapis.com/v1/accounts:lookup?key=' + api_key
headers = {'Content-Type': 'application/json'}

def register(form):
	email = form.email.data
	passw = form.password.data
	json_data = {
		'email'            : email,
		'password'         : passw,
		'returnSecureToken': 'true'
	}
	res = post(signup_url, headers=headers, json=json_data)
	res_user = None
	if res.status_code == 200:
		json_data = {
			'idToken': res.json().get('idToken'),
			'displayName': form.username.data,
			'returnSecureToken': 'true'
		}
		res_user = post(update_profile_url, headers=headers, json=json_data)
	return res.status_code, res.json(), res_user

def login(form):
	email = form.email.data
	passw = form.password.data
	json_data = {
		'email'            : email,
		'password'         : passw,
		'returnSecureToken': 'true'
	}
	res = post(signin_url, headers=headers, json=json_data)
	return res.status_code, res.json()

def user_info(idToken):
	json_data = {'idToken' : idToken}
	res = post(user_data_url, headers=headers, json=json_data)
	if res.status_code == 200:
		return res.json()
	return None