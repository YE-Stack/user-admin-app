from os import environ

class FlaskConfig(object):
	SECRET_KEY = environ.get('SECRET_KEY') or 'a-7jBACuoyB8qiUedVXvzoBYuuvlNgxPCR_WjH'
	# SESSION_COOKIE_SECURE = True
	# REMEMBER_COOKIE_SECURE = True
	SESSION_COOKIE_HTTPONLY = True
	REMEMBER_COOKIE_HTTPONLY = True