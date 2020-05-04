class Database():

    def __init__(self, session, id):
        self.r = session
        self.id = id
        self.base_url = "https://www.devicemagic.com/api/forms"\
                        "/{0}/device_magic_database.json".format(self.id)

    def json(self, *args):
        return self.__filtered_query(args) if args else self.__basic_query()

    def __basic_query(self):
        request = self.r.get(self.base_url)  # For all submissions within the
        return request.json()                # Device Magic Database

    def __join_params(self, parameters):
        params = [param.strip() for param in parameters]
        params_for_url = "?" + "&".join(params)
        return params_for_url

    def __filtered_query(self, parameters):
        params = self.__join_params(parameters)
        request = self.r.get(self.base_url + params)
        return request.json()
