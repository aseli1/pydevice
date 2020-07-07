import json


class Destination():

    def __init__(self, connector, form_id):
        self.connector = connector
        self.form_id = form_id
        self.base_url = 'https://www.devicemagic.com/api/forms/' \
                        '{0}/destinations'.format(self.form_id)
        self.headers = {'Content-Type': 'application/json'}
        self.format = 'json'

    def all(self):
        path = self.base_url + '.' + self.format
        request = self.connector.execute_request(path, 'GET')
        return request

    def details(self, destination_id):
        path = self.base_url + '/' + str(destination_id) + '.' + self.format
        request = self.connector.execute_request(path, 'GET')
        return request

    def create(self, json, form_id=None):
        if form_id is not None:
            path = 'https://www.devicemagic.com/api/'\
                   'forms/{0}/destinations.json'.format(form_id)
        else:
            path = self.base_url + '.' + self.format

        request = self.connector.execute_request(
            path, 'POST', data=json, headers=self.headers)
        return request

    def update(self, destination_id, json):
        path = self.base_url + '/' + str(destination_id) + '.' + self.format
        request = self.connector.execute_request(
            path, 'PUT', data=json, headers=self.headers)
        return request

    def delete(self, destination_id):
        path = self.base_url + '/' + str(destination_id)
        print(path)
        request = self.connector.execute_request(path, 'DELETE')
        if request.status_code >= 200 and request.status_code < 300:
            return 'Destination deleted'
        else:
            return self.connector.failed_request_details(request)

    def copy(self, destination_id, form_id=None):
        destination_to_copy = self.details(destination_id)
        format = destination_to_copy['destination']['format_type']
        transport = destination_to_copy['destination']['transport_type']
        binary = destination_to_copy['destination']['binary_transport_type']
        destination_elements = [format, transport, binary]
        self._remove_keys(destination_elements, destination_to_copy)
        new_destination_json = self._format_destination_json(
            destination_to_copy, format,
            transport, binary)
        return self.create(new_destination_json, form_id=form_id)

    def _remove_keys(self, destination_elements, json):
        for element in destination_elements:
            if element is None:
                continue
            del json['destination'][element]['id']
            del json['destination'][element]['created_at']
            del json['destination'][element]['updated_at']

    def _format_destination_json(self, destination_to_copy,
                                 format, transport, binary):
        new_json = {}
        new_json['destination'] = {}
        new_json['destination']['description'] = \
            destination_to_copy['destination']['description']
        new_json['destination']['format_selection'] = format
        new_json['destination']['transport_selection'] = transport
        new_json['destination']['binary_transport_selection'] = binary
        new_json[format] = destination_to_copy['destination'][format]
        new_json[transport] = destination_to_copy['destination'][transport]
        if binary is not None:
            new_json[binary] = \
                destination_to_copy['destination'][binary]
        new_json = json.dumps(new_json)
        return new_json
