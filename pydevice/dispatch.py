class Dispatch():

    def __init__(self, connector, org_id):
        self.connector = connector
        self.org_id = org_id
        self.device_base_url = 'https://www.devicemagic.com/api/v2/devices'
        self.org_base_url = 'https://www.devicemagic.com/api/v2/organizations'
        self.headers = {'Content-Type': 'application/json'}
        self.format = 'json'

    def all(self, device_identifier=None):
        if device_identifier is not None:
            path = self.device_base_url + '/' + device_identifier \
                  + '/dispatches' + '.' + self.format
        else:
            path = self.org_base_url + '/' + self.org_id + '/dispatches' \
                + '.' + self.format
        request = self.connector.execute_request(path, 'GET')
        return request

    def push(self, device_identifier, json):
        path = self.device_base_url + '/' + device_identifier + '/dispatches' \
            + '.' + self.format
        request = self.connector.execute_request(
            path, 'POST', data=json, headers=self.headers)
        return request

    def update(self, device_identifier, dispatch_id, json):
        path = self.device_base_url + '/' + device_identifier + '/dispatches/'\
               + str(dispatch_id) + '.' + self.format
        request = self.connector.execute_request(
            path, 'PATCH', data=json, headers=self.headers)
        return request

    def delete(self, device_identifier, dispatch_id=None):
        if dispatch_id is not None:
            path = self.device_base_url + '/' + device_identifier \
                   + '/dispatches/' + str(dispatch_id) + '.' + self.format
            request = self.connector.execute_request(path, 'DELETE')
        else:
            path = self.device_base_url + '/' + device_identifier \
                   + '/dispatches/destroy_all' + '.' + self.format
            request = self.connector.execute_request(
                path, 'POST', headers=self.headers, return_json=False)
        if request.status_code >= 200 and request.status_code < 300:
            return 'Dispatch deleted'
        else:
            return self.connector.failed_request_details(request)
