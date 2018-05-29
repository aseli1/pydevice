# pydevice
Device Magic API Wrapper

Currently supports:

* Device Magic Database 
* Destinations
* Devices
* Forms
* Resources
* Groups
* Dispatch

## Installation
```python
pip install pydevice
```

## Usage
```python
>>> from pydevice import DeviceMagic
>>> args = {'org_id': 3000,'database_id': 580, 'form_id': 6000, 'resource_id': 103, 'file_path': 'path/to/file', 'device_identifier': 'Android_d5c2a885'}
>>> dm = DeviceMagic(args)
>>> dm.form.all() # destination, device, resource, group, and dispatch also have this method
{'forms': [{'id': 40015631, 'name': 'Daily Report'...}
```

## Authentication
Authentication is handled by the DeviceMagic class. The class can handle authentication automatically if the environment variable DEVICEMAGIC_API_KEY is set with your api key.
```python
>>> dm = DeviceMagic(args)
```
In preference, you can pass the key explicitly:
```python
>>> dm = DeviceMagic({'api_key': 'HTTP_Auth_Header_Value'})
```
### Database
```python
>>> dm.database.json()
{'per_page': 30, 'current_page': 1, 'total_pages': 1, 'current_count': 13, 'total_count': 13, 'submissions': [{'form'...
>>> dm.database.json("from_date=2018-5-1 00:00", "to_date=2018-5-31 00:00")
{...'total_count': 1, 'submissions': [{'form': {'id': 6009105, 'name': 'Sales Report'...}
```

### Destination
```python
>>> dm.destination.copy(26754)
'Destination created'
```
Optionally you can pass the id of a different form in which you'd like to copy the destination to.
```
>>> dm.destination.copy(26754, form_id=4008185)
```

### Device
```python
>>> dm.device.approve(2801)
'Device approved'
```
### Form
```python
>>> dm.form.details(3005)
{'type': 'root', 'children': [{'identifier': 'Yes_No_Question', 'title': 'Yes/No Question', 'autoIdentifier': True, 'type': 'boolean'}, {'identifier': 'Date_Question', 'title': 'Date Question', 'autoIdentifier': True, 'type': 'date'}...}
```

### Resource
```python
>>> dm.resource.update(480,'client_list', 'client_list.xlsx')
'Resource updated'
```

### Group
```python
>>> dm.group.delete(615)
'Group deleted'
```

### Dispatch
```python
>>> import json
>>> dispatch_json = { "form_namespace" : "http://www.devicemagic.com/xforms/4c0a6400-ef90-8283-8586-22000a1ddaf9", 
                             "payload" : {
                               "Group" : []
                        }
                    }
>>> dispatch_json = json.dumps(dispatch_json)
>>> dm.dispatch.push(dispatch_json)
'Dispatch successful'
```

[Official Device Magic API docs](https://docs.devicemagic.com/create-custom-integrations-with-our-restapi)