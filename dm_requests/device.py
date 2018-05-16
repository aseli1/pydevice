import requests

class Device():

    def __init__(self, args={}):
        self.api_key = args['api_key']
        self.org_id = str(args['org_id'])
        self.base_url = 'https://www.devicemagic.com/organizations/{0}/devices'.format(self.org_id)

    def all_devices(self):
        request = requests.get(self.base_url + ".xml", auth=(self.api_key, 'pass'))
        return request.text

    def device_details(self, device_id):
        request = requests.get(self.base_url + "/"+ str(device_id) + ".xml", auth=(self.api_key, 'pass'))
        return request.text

    def approve_device(self, device_id):
        request = requests.post(self.base_url + "/"+ str(device_id) + "/approve", auth=(self.api_key, 'pass'))
        return request.text

    def delete_device(self, device_id):
        request = requests.delete(self.base_url + "/" + str(device_id), auth=(self.api_key, 'pass'))
        return request.text

    def update_device(self, device_id, xml):
        headers = {'Content-Type': 'application/xml'}
        request = requests.put(self.base_url + "/" + str(device_id), auth=(self.api_key, 'pass'), data=xml, headers=headers)
        return request.text