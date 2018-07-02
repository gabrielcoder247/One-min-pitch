from flask import Flask
from config import DevConfig
# from flask_bootstrap import Bootstrap
from app.main import views
from   flask_sqlalchemy import SQLAlchemy




# bootstrap = Bootstrap()
db = SQLAlchemy()
from .import main


def create_app(config_name):
# Initializing application
    app = Flask(__name__)

 # Initializing flask extensions
    # bootstrap.init_app(app)
    db.init_app(app)
# Setting up configuration
    app.config.from_object(DevConfig)
    # app.config.from_object(config_options[config_name])



 # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    return app