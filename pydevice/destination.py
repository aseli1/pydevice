import json


class Destination():

    def __init__(self, session, form_id):
        self.r = session
        self.form_id = form_id
        self.base_url = "https://www.devicemagic.com/api/forms/"\
                        "{0}/destinations".format(self.form_id)

    def all(self):
        request = self.r.get(self.base_url + ".json")
        return request.json()

    def details(self, destination_id):
        request = self.r.get(
            self.base_url + "/" + str(destination_id) + ".json")
        return request.json()

    def create(self, json, form_id=None):
        if form_id is not None:
            url = "https://www.devicemagic.com/api/"\
                  "forms/{0}/destinations.json".format(form_id)
        else:
            url = self.base_url + ".json"
        headers = {'Content-Type': 'application/json'}
        request = self.r.post(url, data=json, headers=headers)
        if request.status_code >= 200 and request.status_code < 300:
            return request.json()
        else:
            return "Failed with status code: {0}".format(request.status_code)

    def update(self, destination_id, json):
        headers = {'Content-Type': 'application/json'}
        request = self.r.put(self.base_url + "/" + str(destination_id)
                             + ".json", data=json, headers=headers)
        if request.status_code >= 200 and request.status_code < 300:
            return request.json()
        else:
            return "Failed with status code: {0}".format(request.status_code)

    def delete(self, destination_id):
        request = self.r.delete(self.base_url + "/" + str(destination_id))
        if request.status_code >= 200 and request.status_code < 300:
            return "Destination deleted"
        else:
            return "Failed with status code: {0}".format(request.status_code)

    def copy(self, destination_id, form_id=None):
        destination_to_copy = self.details(destination_id)
        format = destination_to_copy["destination"]["format_type"]
        transport = destination_to_copy["destination"]["transport_type"]
        binary = destination_to_copy["destination"]["binary_transport_type"]
        destination_elements = [format, transport, binary]
        self.__remove_keys(destination_elements, destination_to_copy)
        new_destination_json = self.__format_destination_json(
            destination_to_copy, format,
            transport, binary)
        return self.create(new_destination_json, form_id=form_id)

    def __remove_keys(self, destination_elements, json):
        for element in destination_elements:
            if element is None:
                continue
            del json["destination"][element]["id"]
            del json["destination"][element]["created_at"]
            del json["destination"][element]["updated_at"]

    def __format_destination_json(self, destination_to_copy,
                                  format, transport, binary):
        new_json = {}
        new_json["destination"] = {}
        new_json["destination"]["description"] = \
            destination_to_copy["destination"]["description"]
        new_json["destination"]["format_selection"] = format
        new_json["destination"]["transport_selection"] = transport
        new_json["destination"]["binary_transport_selection"] = binary
        new_json[format] = destination_to_copy["destination"][format]
        new_json[transport] = destination_to_copy["destination"][transport]
        if binary is not None:
            new_json[binary] = \
                destination_to_copy["destination"][binary]
        new_json = json.dumps(new_json)
        return new_json
