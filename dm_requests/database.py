import requests

class Database():

    def __init__(self, args={}):
        self.api_key = args['api_key']
        self.database_id = str(args['database_id'])
        self.base_url = 'https://www.devicemagic.com/api/forms/{0}/device_magic_database.json'.format(self.database_id)

    def simple_request(self):
        request = requests.get(self.base_url, auth=(self.api_key, 'pass')) # For all submissions within the Device Magic Database
        return request

    def join_params(self, parameters):
        params = [ param.strip() for param in parameters ]
        params_for_url = "?" + "&".join(params)
        return params_for_url

    def request_with_params(self, parameters):
        params = self.join_params(parameters)
        request = requests.get(self.base_url + params, auth=(self.api_key, 'pass'))
        return request

    def db_request(self, *args):
        return self.request_with_params(args) if args else self.simple_request()



