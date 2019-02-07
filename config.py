import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

API_KEY = os.environ.get('API_KEY')
API_BASE_URL = os.environ.get('API_BASE_URL')
del os