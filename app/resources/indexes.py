from flask_restful import Resource


class Index(Resource):
    def __init__(self, api):
        self.api = api

    def get(self):
        return self.api.get_indexes()
