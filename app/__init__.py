from flask import Flask
from config import DevConfig
<<<<<<< HEAD
# from flask_bootstrap import Bootstrap
from app.main import views
from   flask_sqlalchemy import SQLAlchemy




# bootstrap = Bootstrap()
db = SQLAlchemy()
from .import main
=======
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from app.main import views


bootstrap = Bootstrap()
db = SQLAlchemy()
>>>>>>> e093d9df398ee9518dc278a60a359257df126007


def create_app(config_name):
# Initializing application
    app = Flask(__name__)

 # Initializing flask extensions
<<<<<<< HEAD
    # bootstrap.init_app(app)
    db.init_app(app)
=======
    bootstrap.init_app(app)
    db.init_app(app)

>>>>>>> e093d9df398ee9518dc278a60a359257df126007
# Setting up configuration
    app.config.from_object(DevConfig)
    # app.config.from_object(config_options[config_name])



 # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
<<<<<<< HEAD
    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
=======
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
>>>>>>> e093d9df398ee9518dc278a60a359257df126007

    return app