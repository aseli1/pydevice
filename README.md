# pydevice
Python interface for the Device Magic API

## Installation

PyPi:

```python
pip install pydevice
```

Git:

```python
git clone https://github.com/aseli1/pydevice.git
cd pydevice
python setup.py install
```
Tested on Python 3.6 -- works on Mac

## Usage
```python
>>> from pydevice import DeviceMagic
>>> args = {'org_id': 3000,'database_id': 580, 'form_id': 6000, 'resource_id': 103, 'file_path': 'path/to/file'}
>>> dm = DeviceMagic(args)
>>> dm.form.all() # destination, device, resource, group, and dispatch also have this method
{'forms': [{'id': 40015631, 'name': 'Daily Report'...}
```

## Authentication
Authentication is handled by the DeviceMagic class. The class can handle authentication automatically if the environment variable DEVICEMAGIC_API_KEY is set with your api key.
```python
>>> import os
>>> os.environ['DEVICEMAGIC_API_KEY'] = 'Basic c3ppZhh39fj3Wjk6eA=='
>>> dm = DeviceMagic(args)
```
In preference, you can pass the key explicitly:
```python
>>> dm = DeviceMagic({'api_key': 'Basic c3ppZhh39fj3Wjk6eA=='})
```

### Database
```python
>>> args = {'database_id': 500}
>>> dm = DeviceMagic(args)
>>>
>>> dm.database.json() # All submissions
{'per_page': 30, 'current_page': 1, 'total_pages': 1, 'current_count': 13, 'total_count': 13, 'submissions': [{'form'...
>>>
>>> dm.database.json("from_date=2018-5-1 00:00", "to_date=2018-5-31 00:00") # Filter submissions
{...'total_count': 1, 'submissions': [{'form': {'id': 6009105, 'name': 'Sales Report'...}
```

### Destination
```python
>>> args = {'form_id': 700}
>>> dm = DeviceMagic(args)
>>>
>>> from some_file import destination_json
>>> docx_to_email = 17443 # Destination id
>>> google_sheet = 17465
>>> old_destination = 17432
>>> new_form = 8475
>>>
>>> dm.destination.all() # All form destinations
{'destinations': [{'id': 17442, 'description': None, 'active': True...}]}
>>>
>>> dm.destination.details(docx_to_email)
{'destination': {'id': 17443, 'description': '', 'active': True, 'form_id': 7225921, 'format_type': 'word_format', 'format_id': 14990, 'transport_type': 'email_transport'...
>>>
>>> dm.destination.create(destination_json) # Create a destination
>>>
>>> dm.destination.update(google_sheet, destination_json)
>>>
>>> dm.destination.delete(old_destination)
>>>
>>> dm.destination.copy(docx_to_email) # Copy a destination
>>> dm.destination.copy(docx_to_email, form_id=new_form) # Copy to another form
```

### Device
```python
>>> args = {'org_id': 800}
>>> dm = DeviceMagic(args)
>>>
>>> omaha_tablet = 281 # Device id
>>> new_device = 543
>>> old_device = 93
>>>
>>> dm.device.all() # All devices in organization
{'devices': [{'id': 281, 'identifier': 'Android_d5c2a9d...
>>>
>>> dm.device.details(omaha_tablet) # Device details
{'id': 281, 'identifier': 'Android_d5c2a9d...
>>>
>>> dm.device.delete(old_device)
>>>
>>> dm.device.approve(new_device)
>>>
>>> device_json = {
        'device':{
            'owner':'Audrey',
            'description':'Abroad helping others',
            'groups':'Outreach'
        }
    }
>>>
>>> dm.device.update(new_device, device_json) # Change device name, description and group(s)
```

### Form
```python
>>> args = {'org_id': 800}
>>> dm = DeviceMagic(args)
>>>
>>> from some_file import group_json
>>> site_survey = 400 # Form id
>>> old_form = 235
>>>
>>> dm.form.all() # All forms in organization
{'forms': [{'id': 400, 'name': 'Site Survey'...
>>>
>>> dm.form.details(site_survey)
{'type': 'root', 'children': [{'identifier': 'Time_on_site'...
>>>
>>> with open('form.json') as json:
...     dm.form.create(json.read())
...
'Form created'
>>>
>>> dm.form.update(site_survey, form_json)
>>>
>>> dm.form.delete(old_form)
>>>
>>> dm.form.new_group(site_survey, group_json) # Change form group
```

### Resource
```python
>>> args = {'file_path': 'path/to/material_list.xlsx'}
>>> dm = DeviceMagic(args)
>>>
>>> cost_of_material = 7898 # Resource id
>>> customer_list = 9789
>>> old_resource = 6778
>>> file_as_string = 'eyJub3J0aCI6IjM4L...'
>>> mime = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
>>>
>>> dm.resource.all() # All organization resources
{'resources': [{'id': 6958, 'original_filename': 'Equipment List.xlsx...'}
>>>
>>> dm.resource.details(customer_list)
{'resource': {'id': 9789, 'identifier': '52945f50-408...'}
>>>
>>> dm.resource.download(customer_list) # Download file
>>>
>>> dm.resource.create('Copy of all materials', 'material_list.xlsx') # Create a resource
>>>
>>> dm.resource.create('Copy of all materials', 'material_list.xlsx', file_as_string, mime) # Pass a file directly
>>>
>>> dm.resource.update(cost_of_material, 'With updated pricing', 'cost_of_material.xlsx') # Optionally, pass a file
>>>
>>> dm.resource.clone(cost_of_material, mime) # Clone an existing resource
>>>
>>> dm.resource.delete(old_resource)
```

### Group
```python
>>> args = {'org_id': 400}
>>> dm = DeviceMagic(args)
>>>
>>> from some_file import group_json
>>> old_group = 879 # Group id
>>> technician = 900
>>>
>>> dm.group.all() # All organization groups
{'groups': [{'id': 3643, 'name': 'Engineer', 'form_ids': [...]}
>>>
>>> dm.group.create(group_json) # Create a group
>>>
>>> dm.group.update(technician, group_json)
>>>
>>> dm.group.delete(old_group)
```

### Dispatch
```python
>>> args = {'org_id': 600}
>>> dm = DeviceMagic(args)
>>>
>>> from some_file import dispatch_json
>>> new_brunswick_tab = 'Android_d5c2a9db-7c7e-465b'
>>> ontario_phone = 'iPhone_8775938_48795749'
>>> service_call = 13434 # Oneshot id
>>> old_dispatch = 11947
>>>
>>> dm.dispatch.all() # All outstanding dispatches
'[{"form": {"id": 72343, "name": "Daily Inspection","namespace"...'
>>>
>>> dm.dispatch.push(new_brunswick, dispatch_json) # Dispatch a form
>>>
>>> dm.dispatch.update(new_brunswick, service_call, dispatch_json)
>>>
>>> dm.dispatch.delete(ontario_phone, oneshot_id=old_dispatch) # Delete a single dispatch
>>>
>>> dm.dispatch.delete(ontario_phone) # Remove all
```

[Official Device Magic API docs](https://docs.devicemagic.com/create-custom-integrations-with-our-restapi)
