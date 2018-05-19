class Device():

    def __init__(self, session, org_id):
        self.r = session
        self.org_id = org_id
        self.base_url = 'https://www.devicemagic.com/organizations/{0}/devices'.format(self.org_id)

    def all(self):
        request = self.r.get(self.base_url + ".xml")
        return request.text

    def details(self, device_id):
        request = self.r.get(self.base_url + "/"+ str(device_id) + ".xml")
        return request.text

    def approve(self, device_id):
        request = self.r.post(self.base_url + "/"+ str(device_id) + "/approve")
        return request.text

    def delete(self, device_id):
        request = self.r.delete(self.base_url + "/" + str(device_id))
        return request.text

    def update(self, device_id, xml):
        headers = {'Content-Type': 'application/xml'}
        request = self.r.put(self.base_url + "/" + str(device_id), data=xml, headers=headers)
        return request.text