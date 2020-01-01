from flask import Blueprint

users_app = Blueprint(__name__, 'users', template_folder='templates')

from users import routes