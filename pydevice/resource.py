import base64
import mimetypes


class Resource():

    def __init__(self, connector, file_path):
        self.connector = connector
        self.file_path = file_path
        self.base_url = 'https://www.devicemagic.com/api/resources'
        self.FORMAT = 'json'
        if self.file_path is not None:
            self.content_type = mimetypes.guess_type(self.file_path)
        else:
            self.content_type = None

    def all(self):
        path = self.base_url + '.' + self.FORMAT
        request = self.connector.execute_request(path, 'GET')
        return request

    def download(self, resource_id):
        path = self.base_url + '/' + str(resource_id) + '.' + self.FORMAT
        request = self.connector.execute_request(
            path, 'GET', return_json=False)
        return request

    def details(self, resource_id):
        path = self.base_url + '/' + str(resource_id) \
            + '/describe' + '.' + self.FORMAT
        request = self.connector.execute_request(path, 'GET')
        return request

    def _encode_file(self, file):
        return base64.b64encode(file).decode('utf-8')

    def _encode_local_file(self):
        with open(self.file_path, 'rb') as resource_file:
            self.encoded_file = self._encode_file(resource_file.read())

    def create(self, description, file_name,
               file_data=None, content_type=None):
        if file_data is None:
            self._encode_local_file()
        data = file_data or self.encoded_file
        content_type = content_type or self.content_type
        json = {'resource': {'description': description,
                             'file': {'file_name': file_name,
                                      'file_data': data,
                                      'content_type': content_type}}}
        path = self.base_url + '.' + self.FORMAT
        request = self.connector.execute_request(path, 'POST', data=json)
        return request

    def update(self, resource_id, description,
               file_name, file_data=None, content_type=None):
        if file_data is None:
            self._encode_local_file()
        data = file_data or self.encoded_file
        content_type = content_type or self.content_type
        json = {'resource': {'description': description,
                             'file': {'file_name': file_name,
                                      'file_data': data,
                                      'content_type': content_type}}}
        path = self.base_url + '/' + str(resource_id) + '.' + self.FORMAT
        request = self.connector.execute_request(path, 'PUT', data=json)
        return request

    def clone(self, resource_id, mimetype, description=None, file_name=None):
        file = self.download(resource_id)
        file_data = self._encode_file(file)
        description = description or 'CLONE - {0}'.format(
            self.details(resource_id)['resource']['description'])
        file_name = file_name or 'CLONE - {0}'.format(
            self.details(resource_id)['resource']['original_filename'])
        return self.create(description, file_name, file_data, mimetype)

    def delete(self, resource_id):
        path = self.base_url + '/' + str(resource_id)
        request = self.connector.execute_request(
            path, 'DELETE', return_json=False)
        if request.status_code >= 200 and request.status_code < 300:
            return 'Resource deleted'
        else:
            return self.connector.failed_request_details(request)
