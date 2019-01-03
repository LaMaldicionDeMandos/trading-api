import os
from flask import Flask


def create_app(conf=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        API_KEY='API!!!'
    )
    if conf is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object('config')
    else:
        # load the test config if passed in
        app.config.from_mapping(conf)

    try:
        # ensure the instance folder exists
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def hello():
        return 'Hello, World! Api key: %s.' % app.config['API_KEY']

    return app
