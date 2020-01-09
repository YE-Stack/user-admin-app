import sys
from os import environ

from flask import Blueprint

import firebase_admin
from firebase_admin import credentials

USERS = Blueprint(__name__, 'users', template_folder='templates')

PATH_TO_JSON = environ.get('PATH_TO_JSON')
if not PATH_TO_JSON:
	print('PATH_TO_JSON not set.')
	sys.exit(1)

API_KEY = environ.get('API_KEY')
if not API_KEY:
	print('API_KEY not set.')
	sys.exit(1)

CREDENTIALS = credentials.Certificate(PATH_TO_JSON)
firebase_admin.initialize_app(CREDENTIALS)

from users import routes
