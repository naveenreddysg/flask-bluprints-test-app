import os
from flask import Flask
from config import app_config
from flask_cors import CORS
import datetime

from main import test

def register_blueprints(app):
    app.register_blueprint(test.blueprint)

def create_app():
    config_name = os.getenv('WEB_ENV', 'dev')
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(app_config[config_name])
    register_blueprints(app)
    CORS(app)
    return app

app = create_app()

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])