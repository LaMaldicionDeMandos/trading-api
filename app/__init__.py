import os
from flask import Flask
from flask_restful import Api
from flask_caching import Cache
cache = Cache(config={'CACHE_TYPE': 'simple'})

from app.resources.indexes import Index
from app.services.api import ApiService


def create_app(conf=None):
    app = Flask(__name__, instance_relative_config=True)
    cache.init_app(app)
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

    api = Api(app)

    api_service = ApiService(app.config)

    api.add_resource(Index, '/indexes', resource_class_args=[api_service])

    return app
