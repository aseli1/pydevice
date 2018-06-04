from pydevice import DeviceMagic
import os
import json

current_path = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_path, "../tests/files/sample_resource.xlsx")

test_object = DeviceMagic({'database_id': 6009105, 'form_id': 7179243, 'org_id': 38298, 'file_path': file_path})

create_json = {
    "destination": {
      "description": "Some description",
      "format_selection": "text_format",
      "transport_selection": "email_transport"
    },
    "email_transport": {
      "to_addresses": "test@test.com;test2@test.com" 
    }
}

update_json = {
    "destination": {
      "description": "Brand new description",
    },
    "email_transport": {
      "to_addresses": "new@test.com" 
    },
    "text_format": {
      "location_in_coordinate_format": True
    }
}  
create_json = json.dumps(create_json)
update_json = json.dumps(update_json)

test_destination = {'details_id': 2698289, 'update_id': 2699888, 'delete_id': 2699909, 'copy_id': 2698289, 'create_json': create_json, 'update_json': update_json, 'device_identifier': 'Android_d5c2a9db-7c7e-465b-9e9c-f08ab19bdddc'}

device_xml = '''<device>
                    <owner>Galaxy S7</owner>
                    <description>sample description</description>
                    <groups>Default,Unpublished</groups>
                </device>'''

test_device = {'details_id': 281251, 'update_id': 282601, 'update_xml': device_xml}

sample_form = {
                "type": "root",
                "children": [{
                  "identifier": "Untitled_Question",
                  "title": "Untitled Question",
                  "autoIdentifier": True,
                  "type": "text"
                }],
                "title": "Untitled Form"
              }
sample_form = json.dumps(sample_form)

form_group_json = {
                    "group": "Unpublished"
                  }
form_group_json = json.dumps(form_group_json)

group_create_json = ["Hello", "Goodbye"]
group_create_json = json.dumps(group_create_json)

group_update_json = {
                      "group": {
                        "name": "An updated group name"
                      }
                    }
group_update_json = json.dumps(group_update_json)

dispatch_push_json = { "form_namespace" : "http://www.devicemagic.com/xforms/4c0a5530-ef41-0131-822e-22000a1ddaf9", 
                              "payload" : {
                                "Group" : []
                         }
                     }
dispatch_push_json = json.dumps(dispatch_push_json)

test_form = {'form_id': 7179243, 'sample_form': sample_form, 'delete_id': 7148940, 'group_json': form_group_json}
test_resource = {'download_id': 35670, 'update_id': 35670, 'delete_id': 18333}
test_group = {'create_json': group_create_json, 'update_json': group_update_json, 'update_id': 369051, 'delete_id': 367644}
test_dispatch = {'push_json': dispatch_push_json, 'update_oneshot_id': 7200993, 'delete_oneshot_id': 7200993, 'device_identifier': 'Android_d5c2a9db-7c7e-465b-9e9c-f08ab19bdddc'}