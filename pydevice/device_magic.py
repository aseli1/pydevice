from .database import Database
from .destination import Destination
from .device import Device
from .form import Form
from .resource import Resource
from .auth import DeviceMagicAuth
import requests

class DeviceMagic():

    def __init__(self, args={}):
        self.api_key = args.get('api_key')
        session = requests.Session()
        session.auth = DeviceMagicAuth(self.api_key)
        self.session = session
        self.form_id = str(args.get('form_id'))
        self.database_id = str(args.get('database_id'))
        self.org_id = str(args.get('org_id'))
        self.resource_id = str(args.get('resource_id'))
        self.file_path = args.get('file_path')
        self.database = Database(session, self.database_id)
        self.destination = Destination(session, self.form_id)
        self.device = Device(session, self.org_id)
        self.form = Form(session, self.org_id)
        self.resource = Resource(session, self.file_path)