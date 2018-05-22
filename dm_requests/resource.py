import base64

class Resource():

    def __init__(self, session, file_path):
        self.r = session
        self.file_path = file_path
        self.base_url = 'https://www.devicemagic.com/api/resources'
        self.content_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

    def all(self):
        request = self.r.get(self.base_url + ".json") # To get an overview of all the resources
        return request.json()

    def download(self, resource_id):
        request = self.r.get(self.base_url + "/" + str(resource_id))
        return request.text

    def details(self, resource_id):
        request = self.r.get(self.base_url + "/"+ str(resource_id) + "/describe.json")
        return request.json()

    def __encode_file(self):
        with open(self.file_path, "rb") as resource_file:
            encoded_file = base64.b64encode(resource_file.read())
            self.encoded_file = encoded_file

    def create(self, description, file_name, content_type=None):
        if content_type == None:
          content_type = self.content_type

        self.__encode_file()
        json = {"resource": {"description": description,
                             "file": {"file_name": file_name,
                                      "file_data": self.encoded_file,
                                      "content_type": content_type}}}
        request = self.r.post(self.base_url + ".json", json=json)
        if request.status_code >= 200 and request.status_code < 300:
            return "Resource created"
        else:
            return "Failed with status code: {0}".format(request.status_code)

    def update(self, resource_id, description, file_name, content_type=None):
        if content_type == None:
          content_type = self.content_type

        self.__encode_file()
        json = {"resource": {"description": description,
                             "file": {"file_name": file_name,
                                      "file_data": self.encoded_file,
                                      "content_type": content_type}}}
        request = self.r.put(self.base_url + "/" + str(resource_id), json=json)
        if request.status_code >= 200 and request.status_code < 300:
            return "Resource updated"
        else:
            return "Failed with status code: {0}".format(request.status_code)

    def delete(self, resource_id):
        request = self.r.delete(self.base_url + "/" + str(resource_id))
        if request.status_code >= 200 and request.status_code < 300:
            return "Resource deleted"
        else:
            return "Failed with status code: {0}".format(request.status_code)