from flask import Flask
from users import users_app
from app.config import FlaskConfig

app = Flask(__name__, template_folder='templates')

app.config.from_object(FlaskConfig())

app.register_blueprint(users_app, url_prefix='/')

from app import routes