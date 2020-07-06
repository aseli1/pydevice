class Database():

    def __init__(self, connector, id):
        self.connector = connector
        self.id = id
        self.base_url = 'https://www.devicemagic.com/api/forms' \
                        '/{0}/device_magic_database.json'.format(self.id)

    def json(self, *args):
        return self._filtered_query(args) if args else self._basic_query()

    def _basic_query(self):
        path = self.base_url
        request = self.connector.execute_request(path, 'GET')
        return request

    def _join_params(self, parameters):
        params = [param.strip() for param in parameters]
        params_for_url = '?' + '&'.join(params)
        return params_for_url

    def _filtered_query(self, parameters):
        params = self._join_params(parameters)
        path = self.base_url + params
        request = self.connector.execute_request(path, 'GET')
        return request
