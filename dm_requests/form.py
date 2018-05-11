import requests
import json

class Form():

    def __init__(self, args={}):
        self.api_key = args['api_key']
        self.org_id = str(args['org_id'])
        self.base_url = 'https://www.devicemagic.com/organizations/{0}/forms'.format(self.org_id)

    def all_forms(self):
        request = requests.get(self.base_url + ".json", auth=(self.api_key, 'pass'))
        return request.text

    def form_details(self, form_id):
        request = requests.get(self.base_url + "/"+ str(form_id) + ".json", auth=(self.api_key, 'pass'))
        return request.text

    def create_form(self, form_json):
        headers = {'Content-Type': 'application/json'}    
        request = requests.post(self.base_url, auth=(self.api_key, 'pass'), data=form_json, headers=headers)
        if request.status_code == 201:
            return "Form created"
        else:
            return "Failed with status code: {0}".format(request.status_code)

    def update_form(self, form_id, form_json):
        headers = {'Content-Type': 'application/json'}
        request = requests.put(self.base_url + "/" + str(form_id), auth=(self.api_key, 'pass'), data=form_json, headers=headers)
        if request.status_code == 202:
            return "Form updated"
        else:
            return "Failed with status code: {0}".format(request.status_code)

    def delete_form(self, form_id):
        request = requests.delete(self.base_url + "/" + str(form_id), auth=(self.api_key, 'pass'))
        if request.status_code == 200:
            return "Form deleted"
        else:
            return "Failed with status code: {0}".format(request.status_code)

    def update_form_group(self, form_id, json):
        headers = {'Content-Type': 'application/json'}
        request = requests.put(self.base_url + "/" + str(form_id) + "/properties", auth=(self.api_key, 'pass'), data=json, headers=headers)
        if request.status_code == 200:
            return "Form group updated"
        else:
            return "Failed with status code: {0} {1}".format(request.status_code)
