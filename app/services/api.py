import requests


class ApiService:
    def __init__(self, config):
        self.config = config

    def get_indexes(self):
        url = '%s/indexes' % self.config['API_BASE_URL']
        headers = {'x-api-key': self.config['API_KEY'], 'Accept': 'application/json'}
        return requests.get(url, headers=headers).json()
