import requests
import base64

class Resource():

    def __init__(self, args={}):
      self.api_key = args['api_key']
      self.resource_id = str(args['resource_id'])
      self.encoded_file = args['encoded_file']
      self.base_url = 'https://www.devicemagic.com/api/resources'

    def all_resources(self):
        request = requests.get(self.base_url + ".json", auth=(self.api_key, 'pass')) # To get an overview of all the resources
        return request

    def resource_download(self):
        resource_file = requests.get(self.base_url + "/" + self.resource_id, auth=(self.api_key, 'pass'))
        return resource_file

    def resource_details(self):
        request = requests.get(self.base_url + "/"+ self.resource_id + "/describe.json", auth=(self.api_key, 'pass'))
        return request

    def create_resource(self):
        json = {"resource": {"description": "Services Agreement",
                             "file": {"file_name": "Services.pdf",
                                      "file_data": self.encoded_file,
                                      "content_type": "application/pdf"}}}
        request = requests.post(self.base_url + ".json", auth=(self.api_key, 'pass'), json=json)

    def update_resource(self):
        json = {"resource": {"description": "Updated Agreement",
                             "file": {"file_name": "Update_Services.pdf",
                                      "file_data": self.encoded_file,
                                      "content_type": "application/pdf"}}}
        request = requests.put(self.base_url + "/" + self.resource_id, auth=(self.api_key, 'pass'), json=json)

    def delete_resource(self):
        request = requests.delete(self.base_url + "/" + self.resource_id, auth=(self.api_key, 'pass'))