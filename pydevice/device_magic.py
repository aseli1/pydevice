from .auth import DeviceMagicAuth
import requests


class DeviceMagic():

    def __init__(self, args={}):
        self.api_key = args.get('api_key')
        self.session = requests.Session()
        self.session.auth = DeviceMagicAuth(self.api_key)
        self.form_id = str(args.get('form_id'))
        self.database_id = str(args.get('database_id'))
        self.org_id = str(args.get('org_id'))
        self.resource_id = str(args.get('resource_id'))
        self.file_path = args.get('file_path')
        self.device_identifier = args.get('device_identifier')

    @property
    def resource(self):
        from .resource import Resource
        return Resource(self.connector, self.file_path)

    @property
    def database(self):
        from .database import Database
        return Database(self.connector, self.database_id)

    @property
    def destination(self):
        from .destination import Destination
        return Destination(self.connector, self.form_id)

    @property
    def device(self):
        from .device import Device
        return Device(self.connector, self.org_id)

    @property
    def form(self):
        from .form import Form
        return Form(self.connector, self.org_id)

    @property
    def group(self):
        from .group import Group
        return Group(self.connector, self.org_id)

    @property
    def dispatch(self):
        from .dispatch import Dispatch
        return Dispatch(self.connector, self.org_id)

    @property
    def connector(self):
        from .connector import Connector
        return Connector(self.session)
