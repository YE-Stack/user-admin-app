from os import environ

class FlaskConfig(object):
	SECRET_KEY = environ.get('SECRET_KEY') or 'WEAK_KEY'