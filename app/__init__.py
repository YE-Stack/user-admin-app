from flask import Flask
from users import USERS
from app.config import AppConfig

APP = Flask(__name__, template_folder='templates')

APP.config.from_object(AppConfig())

APP.register_blueprint(USERS, url_prefix='/u')

from app import routes
