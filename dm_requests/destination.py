import requests
import json

class Destination():

    def __init__(self, args={}):
        self.api_key = args['api_key']
        self.form_id = str(args['form_id'])
        self.base_url = 'https://www.devicemagic.com/api/forms/{0}/destinations'.format(self.form_id)

    def all_destinations(self):
        request = requests.get(self.base_url + ".json", auth=(self.api_key, 'pass'))
        return request.json()

    def destination_details(self, destination_id):
        request = requests.get(self.base_url + "/" + str(destination_id) + ".json", auth=(self.api_key, 'pass'))
        return request.json()

    def create_destination(self, json, form_id=None):
        if form_id != None:
            url = "https://www.devicemagic.com/api/forms/{0}/destinations".format(form_id)
        else:
            url = self.base_url
        headers = {'Content-Type': 'application/json'}    
        request = requests.post(url, auth=(self.api_key, 'pass'), data=json, headers=headers)
        if request.status_code >= 200 and request.status_code < 300:
            return "Destination created"
        else:
            return "Failed with status code: {0}{1}".format(request.status_code, request.headers)

    def update_destination(self, destination_id, json):
        headers = {'Content-Type': 'application/json'}
        request = requests.put(self.base_url + "/" + str(destination_id), auth=(self.api_key, 'pass'), data=json, headers=headers)
        if request.status_code >= 200 and request.status_code < 300:
            return "Destination updated"
        else:
            return "Failed with status code: {0}".format(request.status_code)

    def delete_destination(self, destination_id):
        request = requests.delete(self.base_url + "/" + str(destination_id), auth=(self.api_key, 'pass'))
        if request.status_code >= 200 and request.status_code < 300:
            return "Destination deleted"
        else:
            return "Failed with status code: {0}".format(request.status_code)

    def copy_destination(self, destination_id, form_id=None):
        destination_to_copy = self.destination_details(destination_id)
        format = destination_to_copy["destination"]["format_type"]
        transport = destination_to_copy["destination"]["transport_type"]
        binary = destination_to_copy["destination"]["binary_transport_type"]
        destination_elements = [format, transport, binary]
        self.remove_keys(destination_elements, destination_to_copy)
        new_destination_json = self.format_destination_json(destination_to_copy, format, transport, binary)
        return self.create_destination(new_destination_json, form_id=form_id)

    def remove_keys(self, destination_elements, json):
        for element in destination_elements:
            if element == None:
                continue
            del json["destination"][element]["id"]
            del json["destination"][element]["created_at"]
            del json["destination"][element]["updated_at"]

    def format_destination_json(self, destination_to_copy, format, transport, binary):
        new_destination_json = {}
        new_destination_json["destination"] = {}
        new_destination_json["destination"]["description"] = destination_to_copy["destination"]["description"]
        new_destination_json["destination"]["format_selection"] = format
        new_destination_json["destination"]["transport_selection"] = transport
        new_destination_json["destination"]["binary_transport_selection"] = binary
        new_destination_json[format] = destination_to_copy["destination"][format]
        new_destination_json[transport] = destination_to_copy["destination"][transport]
        if binary != None:
            new_destination_json[binary] = destination_to_copy["destination"][binary]
        new_destination_json = json.dumps(new_destination_json)
        return new_destination_json