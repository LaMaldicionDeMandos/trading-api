import os
import requests
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

    @app.route('/indexes')
    def indexes():
        url = '%s/indexes' % app.config['API_BASE_URL']
        headers = {'x-api-key': app.config['API_KEY'], 'Accept': 'application/json'}
        response = app.make_response((requests.get(url, headers=headers).text, 200))
        response.mimetype = 'application/json'
        return response

    return app
