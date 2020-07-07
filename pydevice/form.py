class Form():

    def __init__(self, connector, org_id):
        self.connector = connector
        self.org_id = org_id
        self.base_url = 'https://www.devicemagic.com/organizations/'\
                        '{0}/forms'.format(self.org_id)
        self.headers = {'Content-Type': 'application/json'}
        self.format = 'json'

    def all(self):
        path = self.base_url + '.' + self.format
        return self.connector.execute_request(path, 'GET')

    def details(self, form_id):
        path = self.base_url + '/' + str(form_id) + '.' + self.format
        return self.connector.execute_request(path, 'GET')

    def create(self, json):
        path = self.base_url + '.' + self.format
        return self.connector.execute_request(
            path, 'POST', data=json, headers=self.headers)

    def update(self, form_id, json):
        path = self.base_url + '/' + str(form_id) + '.' + self.format
        return self.connector.execute_request(
            path, 'PUT', data=json, headers=self.headers)

    def delete(self, form_id):
        path = self.base_url + '/' + str(form_id) + '.' + self.format
        request = self.connector.execute_request(path, 'DELETE')
        if request.status_code >= 200 and request.status_code < 300:
            return 'Form deleted'
        else:
            return self.connector.failed_request_details(request)

    def new_group(self, form_id, json):
        path = self.base_url + '/' + str(form_id) \
            + '/properties' + '.' + self.format
        request = self.connector.execute_request(
            path, 'POST', data=json, headers=self.headers, return_json=False)
        if request.status_code >= 200 and request.status_code < 300:
            return 'Form group updated'
        else:
            return self.connector.failed_request_details(request)
