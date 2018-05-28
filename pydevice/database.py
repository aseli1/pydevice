class Database():

    def __init__(self, session, database_id):
        self.r = session
        self.database_id = database_id
        self.base_url = 'https://www.devicemagic.com/api/forms/{0}/device_magic_database.json'.format(self.database_id)

    def json(self, *args):
        return self.__request_with_params(args) if args else self.__simple_request()
    
    def __simple_request(self):
        request = self.r.get(self.base_url) # For all submissions within the Device Magic Database
        return request.json()

    def __join_params(self, parameters):
        params = [ param.strip() for param in parameters ]
        params_for_url = "?" + "&".join(params)
        return params_for_url

    def __request_with_params(self, parameters):
        params = self.__join_params(parameters)
        request = self.r.get(self.base_url + params)
        return request.json()




