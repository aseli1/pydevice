class Dispatch():

    def __init__(self, session, org_id):
        self.r = session
        self.org_id = org_id
        self.device_base_url = 'https://www.devicemagic.com/api/v2/devices'
        self.org_base_url = 'https://www.devicemagic.com/api/v2/organizations'

    def all(self, device_identifier=None):
        if device_identifier is not None:
            url = self.device_base_url + "/" + device_identifier \
                  + "/dispatches.json"
        else:
            url = self.org_base_url + "/" + self.org_id + "/dispatches.json"
        request = self.r.get(url)
        return request.json()

    def push(self, device_identifier, json):
        headers = {'Content-Type': 'application/json'}
        request = self.r.post(self.device_base_url + "/" + device_identifier
                              + "/dispatches.json", data=json, headers=headers)
        if request.status_code >= 200 and request.status_code < 300:
            return request.json()
        else:
            return "Failed with status code: {0}".format(request.status_code)

    def update(self, device_identifier, dispatch_id, json):
        headers = {'Content-Type': 'application/json'}
        request = self.r.patch(self.device_base_url + "/" + device_identifier
                               + "/dispatches/" + str(dispatch_id)
                               + ".json", data=json, headers=headers)
        if request.status_code >= 200 and request.status_code < 300:
            return request.json()
        else:
            return "Failed with status code: {0}".format(request.status_code)

    def delete(self, device_identifier, dispatch_id=None):
        if dispatch_id is not None:
            url = self.device_base_url + "/" + device_identifier \
                  + "/dispatches/" + str(dispatch_id)
            request = self.r.delete(url)
        else:
            url = self.device_base_url + "/" + device_identifier \
                  + "/dispatches/destroy_all"
            request = self.r.post(url)
        if request.status_code >= 200 and request.status_code < 300:
            return "Dispatch deleted"
        else:
            return "Failed with status code: {0}".format(request.status_code)
