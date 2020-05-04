class Device():

    def __init__(self, session, org_id):
        self.r = session
        self.org_id = org_id
        self.base_url = "https://www.devicemagic.com/organizations/"\
                        "{0}/devices".format(self.org_id)

    def all(self):
        request = self.r.get(self.base_url + ".json")
        return request.json()

    def details(self, device_id):
        request = self.r.get(self.base_url + "/" + str(device_id) + ".json")
        return request.json()

    def approve(self, device_id):
        request = self.r.post(self.base_url + "/"
                              + str(device_id) + "/approve")
        if request.status_code >= 200 and request.status_code < 300:
            return "Device approved"
        else:
            return "Failed with status code: {0}".format(request.status_code)

    def delete(self, device_id):
        request = self.r.delete(self.base_url + "/" + str(device_id))
        if request.status_code >= 200 and request.status_code < 300:
            return "Device deleted"
        else:
            return "Failed with status code: {0}".format(request.status_code)

    def update(self, device_id, json):
        headers = {'Content-Type': 'application/json'}
        request = self.r.put(self.base_url + "/"
                             + str(device_id), data=json, headers=headers)
        if request.status_code >= 200 and request.status_code < 300:
            return "Device updated"
        else:
            return "Failed with status code: {0}".format(request.status_code)
