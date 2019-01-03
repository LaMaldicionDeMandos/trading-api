import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

API_KEY = os.environ.get('API_KEY', default="API_DEFAULT")

del os