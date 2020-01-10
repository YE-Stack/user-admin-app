import datetime

from flask import session

def store_id_token(res, user):
	expire_cookie = datetime.datetime.now() + datetime.timedelta(seconds=int(user.get('expiresIn')))
	res.set_cookie('id_token', user.get('idToken'), expires=expire_cookie)
	store_user_info(user)
	return res

def store_user_info(user):
	session['username'] = user.get('displayName')
	session['email'] = user.get('email')

def clear_user_info(res):
	res.set_cookie('id_token', expires=0)
	session['username'] = None
	session['email'] = None
	return res
