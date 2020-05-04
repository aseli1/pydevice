class Form():

    def __init__(self, session, org_id):
        self.r = session
        self.org_id = org_id
        self.base_url = "https://www.devicemagic.com/organizations/"\
                        "{0}/forms".format(self.org_id)

    def all(self):
        request = self.r.get(self.base_url + ".json")
        return request.json()

    def details(self, form_id):
        request = self.r.get(self.base_url + "/" + str(form_id) + ".json")
        return request.json()

    def create(self, json):
        headers = {'Content-Type': 'application/json'}
        request = self.r.post(self.base_url, data=json, headers=headers)
        if request.status_code >= 200 and request.status_code < 300:
            return request.json()
        else:
            return "Failed with status code: {0}".format(request.status_code)

    def update(self, form_id, json):
        headers = {'Content-Type': 'application/json'}
        request = self.r.put(self.base_url + "/"
                             + str(form_id), data=json, headers=headers)
        if request.status_code >= 200 and request.status_code < 300:
            return request.json()
        else:
            return "Failed with status code: {0}".format(request.status_code)

    def delete(self, form_id):
        request = self.r.delete(self.base_url + "/" + str(form_id))
        if request.status_code >= 200 and request.status_code < 300:
            return "Form deleted"
        else:
            return "Failed with status code: {0}".format(request.status_code)

    def new_group(self, form_id, json):
        headers = {'Content-Type': 'application/json'}
        request = self.r.post(self.base_url + "/" + str(form_id)
                              + "/properties", data=json, headers=headers)
        if request.status_code >= 200 and request.status_code < 300:
            return "Form group updated"
        else:
            return "Failed with status code: {0}".format(request.status_code)
