import sys
import os

from flask import Blueprint

import firebase_admin
from firebase_admin import credentials

USERS = Blueprint(__name__, 'users', template_folder='templates')

PATH_TO_JSON = os.environ.get('PATH_TO_JSON')
if not PATH_TO_JSON:
	print('PATH_TO_JSON not set.')
	sys.exit(1)

CREDENTIALS = credentials.Certificate(PATH_TO_JSON)
firebase_admin.initialize_app(CREDENTIALS)

from users import routes
