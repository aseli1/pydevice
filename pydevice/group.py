class Group():

    def __init__(self, connector, org_id):
        self.connector = connector
        self.org_id = org_id
        self.base_url = 'https://www.devicemagic.com/organizations/' \
                        '{0}/groups'.format(self.org_id)
        self.headers = {'Content-Type': 'application/json'}
        self.format = 'json'

    def all(self):
        path = self.base_url + '.' + self.format
        request = self.connector.execute_request(path, 'GET')
        return request

    def create(self, json):
        path = self.base_url
        request = self.connector.execute_request(
            path, 'POST', data=json, headers=self.headers, return_json=False)
        if request.status_code >= 200 and request.status_code < 300:
            return 'Group created'
        else:
            return self.connector.failed_request_details(request)

    def update(self, group_id, json):
        path = self.base_url + '/' + str(group_id)
        request = self.connector.execute_request(
            path, 'PUT', data=json, headers=self.headers, return_json=False)
        if request.status_code >= 200 and request.status_code < 300:
            return 'Group updated'
        else:
            return self.connector.failed_request_details(request)

    def delete(self, group_id):
        path = self.base_url + '/' + str(group_id)
        request = self.connector.execute_request(
            path, 'DELETE', return_json=False)
        if request.status_code >= 200 and request.status_code < 300:
            return 'Group deleted'
        else:
            return self.connector.failed_request_details(request)
