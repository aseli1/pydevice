class Connector(object):

    def __init__(self, session):
        self.r = session
        self.FORMAT = 'json'

    def execute_request(self, path, method,
                        data=None, headers={}, return_json=True):
        if method == 'GET':
            return self._get(path)
        elif method == 'POST':
            return self._post(path, data, headers, return_json)
        elif method == 'PUT':
            return self._put(path, data, headers)
        elif method == 'PATCH':
            return self._patch(path, data, headers)
        elif method == 'DELETE':
            return self._delete(path)
        else:
            return "pizza"

    def _get(self, path):
        request = self.r.get(path + ".{}".format(self.FORMAT))
        return request.json()

    def _post(self, path, data, headers, return_json=True):
        self.r.headers.update(headers)
        request = self.r.post(path + ".{}".format(self.FORMAT),
                              data=data, headers=self.r.headers)
        return request.json() if return_json else request

    def _put(self, path, data, headers):
        self.r.headers.update(headers)
        request = self.r.put(path + ".{}".format(self.FORMAT),
                             data=data, headers=self.r.headers)
        return request.json()

    def _patch(self, path, data, headers):
        self.r.headers.update(headers)
        request = self.r.patch(path + ".{}".format(self.FORMAT),
                               data=data, headers=self.headers)
        return request.json()

    def _delete(self, path):
        request = self.r.delete(path)
        return request
