class Dispatch():

    def __init__(self, session, device_identifier):
        self.r = session
        self.device_identifier = device_identifier
        self.base_url = 'https://www.devicemagic.com/clients'

    def all(self):
        request = self.r.get(self.base_url + "/" + self.device_identifier + "/oneshots")
        return request.text

    def push(self, json):
        headers = {'Content-Type': 'application/json'}  
        request = self.r.post(self.base_url + "/" + self.device_identifier + "/oneshots", data=json, headers=headers)
        if request.status_code >= 200 and request.status_code < 300:
            return "Dispatch successful"
        else:
            return "Failed with status code: {0}".format(request.status_code)
    
    def update(self, oneshot_id, json):
        headers = {'Content-Type': 'application/json'}
        request = self.r.put(self.base_url + "/" + self.device_identifier + "/oneshots/" + str(oneshot_id), data=json, headers=headers)
        if request.status_code >= 200 and request.status_code < 300:
            return "Dispatch updated"
        else:
            return "Failed with status code: {0}".format(request.status_code)

    def delete(self, oneshot_id):
        request = self.r.delete(self.base_url + "/" + self.device_identifier + "/oneshots/" + str(oneshot_id))
        if request.status_code >= 200 and request.status_code < 300:
            return "Dispatch deleted"
        else:
            return "Failed with status code: {0}".format(request.status_code)