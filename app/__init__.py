import os
from flask import Flask
from .main_routes import main_routes_bp

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(main_routes_bp)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flask.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app

    