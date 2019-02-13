from flask_restful import Resource
from app import cache


class Index(Resource):
    def __init__(self, api):
        self.api = api

    @cache.cached(timeout=3600)
    def get(self):
        return self.api.get_indexes()
