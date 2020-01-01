from flask import Blueprint
from firebase_admin import credentials
from os import environ

import firebase_admin

users_app = Blueprint(__name__, 'users', template_folder='templates')

path_to_json = environ.get('PATH_TO_JSON')

cred = credentials.Certificate(path_to_json)
firebase_app = firebase_admin.initialize_app(cred) # Not used

from users import routes