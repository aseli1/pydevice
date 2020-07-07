class Connector(object):

    def __init__(self, session):
        self.r = session

    def execute_request(self, path, method,
                        data=None, headers={}, return_json=True):
        if method == 'GET':
            return self._get(path, return_json)
        elif method == 'POST':
            return self._post(path, data, headers, return_json)
        elif method == 'PUT':
            return self._put(path, data, headers, return_json)
        elif method == 'PATCH':
            return self._patch(path, data, headers)
        elif method == 'DELETE':
            return self._delete(path)
        else:
            raise ValueError('Invalid method provided: {}'.format(method))

    def _get(self, path, return_json=True):
        request = self.r.get(path)
        return request.json() if return_json else request.content

    def _post(self, path, data, headers, return_json=True):
        self.r.headers.update(headers)
        request = self.r.post(path, data=data, headers=self.r.headers)
        return request.json() if return_json else request

    def _put(self, path, data, headers, return_json=True):
        self.r.headers.update(headers)
        request = self.r.put(path, data=data, headers=self.r.headers)
        return request.json() if return_json else request

    def _patch(self, path, data, headers):
        self.r.headers.update(headers)
        request = self.r.patch(path, data=data, headers=self.r.headers)
        return request.json()

    def _delete(self, path):
        request = self.r.delete(path)
        return request

    def failed_request_details(self, request):
        return 'Failed with status code: {0} {1}, headers: {2}'.format(
            request.status_code, request.reason, request.headers)
