import base64
import mimetypes


class Resource():

    def __init__(self, session, file_path):
        self.r = session
        self.file_path = file_path
        self.base_url = "https://www.devicemagic.com/api/resources"
        if self.file_path is not None:
            self.content_type = mimetypes.guess_type(self.file_path)
        else:
            self.content_type = None

    def all(self):
        request = self.r.get(self.base_url + ".json")  # To get an overview
        return request.json()                          # of all the resources

    def download(self, resource_id):
        request = self.r.get(self.base_url + "/" + str(resource_id))
        return request.content

    def details(self, resource_id):
        request = self.r.get(self.base_url + "/"
                             + str(resource_id) + "/describe.json")
        return request.json()

    def __encode_file(self, file):
        return base64.b64encode(file).decode("utf-8")

    def __encode_local_file(self):
        with open(self.file_path, "rb") as resource_file:
            self.encoded_file = self.__encode_file(resource_file.read())

    def create(self, description, file_name,
               file_data=None, content_type=None):
        if file_data is None:
            self.__encode_local_file()
        data = file_data or self.encoded_file
        content_type = content_type or self.content_type
        json = {"resource": {"description": description,
                             "file": {"file_name": file_name,
                                      "file_data": data,
                                      "content_type": content_type}}}
        request = self.r.post(self.base_url + ".json", json=json)
        if request.status_code >= 200 and request.status_code < 300:
            return request.json()
        else:
            return "Failed with status code: {0}".format(request.status_code)

    def update(self, resource_id, description,
               file_name, file_data=None, content_type=None):
        if file_data is None:
            self.__encode_local_file()
        data = file_data or self.encoded_file
        content_type = content_type or self.content_type
        json = {"resource": {"description": description,
                             "file": {"file_name": file_name,
                                      "file_data": data,
                                      "content_type": content_type}}}
        request = self.r.put(
            self.base_url + "/" + str(resource_id) + ".json", json=json)
        if request.status_code >= 200 and request.status_code < 300:
            return request.json()
        else:
            return "Failed with status code: {0}".format(request.status_code)

    def clone(self, resource_id, mimetype, description=None, file_name=None):
        file = self.download(resource_id)
        file_data = self.__encode_file(file)
        description = description or "CLONE - {0}".format(
            self.details(resource_id)["resource"]["description"])
        file_name = file_name or "CLONE - {0}".format(
            self.details(resource_id)["resource"]["original_filename"])
        return self.create(description, file_name, file_data, mimetype)

    def delete(self, resource_id):
        request = self.r.delete(self.base_url + "/" + str(resource_id))
        if request.status_code >= 200 and request.status_code < 300:
            return "Resource deleted"
        else:
            return "Failed with status code: {0}".format(request.status_code)
