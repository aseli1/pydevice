class Dispatch():

    def __init__(self, session, org_id):
        self.r = session
        self.org_id = org_id
        self.device_base_url = 'https://www.devicemagic.com/clients'
        self.org_base_url = 'https://www.devicemagic.com/organizations'

    def all(self, device_identifier=None):
        if device_identifier != None:
            url = self.device_base_url + "/" + device_identifier + "/oneshots"
        else:
            url = self.org_base_url + "/" + self.org_id + "/oneshots"
        request = self.r.get(url)
        return request.text

    def push(self, device_identifier, json):
        headers = {'Content-Type': 'application/json'}  
        request = self.r.post(self.device_base_url + "/" + device_identifier + "/oneshots", data=json, headers=headers)
        if request.status_code >= 200 and request.status_code < 300:
            return "Dispatch successful"
        else:
            return "Failed with status code: {0}".format(request.status_code)
    
    def update(self, device_identifier, oneshot_id, json):
        headers = {'Content-Type': 'application/json'}
        request = self.r.put(self.device_base_url + "/" + device_identifier + "/oneshots/" + str(oneshot_id), data=json, headers=headers)
        if request.status_code >= 200 and request.status_code < 300:
            return "Dispatch updated"
        else:
            return "Failed with status code: {0}".format(request.status_code)

    def delete(self, device_identifier, oneshot_id=None):
        if oneshot_id != None:
            url = self.device_base_url + "/" + device_identifier + "/oneshots/" + str(oneshot_id)
            request = self.r.delete(url)
        else:
            url = self.device_base_url + "/" + device_identifier + "/oneshots/destroy_all"
            request = self.r.post(url)
        if request.status_code >= 200 and request.status_code < 300:
            return "Dispatch deleted"
        else:
            return "Failed with status code: {0}".format(request.status_code)