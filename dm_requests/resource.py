import requests
import base64

class Resource():

    def __init__(self, args={}):
        self.api_key = args['api_key']
        self.resource_id = str(args.get('resource_id'))
        self.file_path = args.get('file_path')
        self.base_url = 'https://www.devicemagic.com/api/resources'
        self.content_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

    def all_resources(self):
        request = requests.get(self.base_url + ".json", auth=(self.api_key, 'pass')) # To get an overview of all the resources
        return request.json()

    def resource_download(self):
        resource_file = requests.get(self.base_url + "/" + self.resource_id, auth=(self.api_key, 'pass'))
        return resource_file

    def resource_details(self):
        request = requests.get(self.base_url + "/"+ self.resource_id + "/describe.json", auth=(self.api_key, 'pass'))
        return request.json()

    def encode_file(self):
        with open(self.file_path, "rb") as resource_file:
            encoded_file = base64.b64encode(resource_file.read())
            self.encoded_file = encoded_file

    def create_resource(self, description, file_name, content_type=None):
        if content_type == None:
          content_type = self.content_type

        self.encode_file()
        json = {"resource": {"description": description,
                             "file": {"file_name": file_name,
                                      "file_data": self.encoded_file,
                                      "content_type": content_type}}}
        request = requests.post(self.base_url + ".json", auth=(self.api_key, 'pass'), json=json)

    def update_resource(self, description, file_name, content_type=None):
        if content_type == None:
          content_type = self.content_type

        self.encode_file()
        json = {"resource": {"description": description,
                             "file": {"file_name": file_name,
                                      "file_data": self.encoded_file,
                                      "content_type": content_type}}}
        request = requests.put(self.base_url + "/" + self.resource_id, auth=(self.api_key, 'pass'), json=json)

    def delete_resource(self):
        request = requests.delete(self.base_url + "/" + self.resource_id, auth=(self.api_key, 'pass'))