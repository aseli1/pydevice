class Device():

    def __init__(self, connector, org_id):
        self.connector = connector
        self.org_id = org_id
        self.base_url = 'https://www.devicemagic.com/organizations/' \
                        '{0}/devices'.format(self.org_id)
        self.headers = {'Content-Type': 'application/json'}
        self.format = 'json'

    def all(self):
        path = self.base_url + '.' + self.format
        request = self.connector.execute_request(path, 'GET')
        return request

    def details(self, device_id):
        path = self.base_url + '/' + str(device_id) + '.' + self.format
        request = self.connector.execute_request(path, 'GET')
        return request

    def approve(self, device_id):
        path = self.base_url + '/' + str(device_id) + '/approve'
        request = self.connector.execute_request(
            path, 'POST', return_json=False)
        if request.status_code >= 200 and request.status_code < 300:
            return 'Device approved'
        else:
            return self.connector.failed_request_details(request)

    def delete(self, device_id):
        path = self.base_url + '/' + str(device_id)
        request = self.connector.execute_request(path, 'DELETE')
        if request.status_code >= 200 and request.status_code < 300:
            return 'Device deleted'
        else:
            return self.connector.failed_request_details(request)

    def update(self, device_id, json):
        path = self.base_url + '/' + str(device_id)
        request = self.connector.execute_request(
            path, 'PUT', data=json, headers=self.headers, return_json=False)
        if request.status_code >= 200 and request.status_code < 300:
            return 'Device updated'
        else:
            return self.connector.failed_request_details(request)
