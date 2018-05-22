from __future__ import absolute_import
import os
import requests

class DeviceMagicAuth(requests.auth.AuthBase):

    def __init__(self, api_key=None):
        """
        Args:
            api_key (``str``): DeviceMagic API Key. Optional.
                If not set, it will look for
                enviroment variable ``DEVICEMAGIC_API_KEY``
        """
        try:
            self.api_key = api_key or os.environ['DEVICEMAGIC_API_KEY']
        except KeyError:
            raise KeyError('Api Key not found. Pass api_key as a kwarg \
                            or set an env var DEVICEMAGIC_API_KEY with your key')

    def __call__(self, request):
        auth_token = {'Authorization': '{0}'.format(self.api_key)}
        request.headers.update(auth_token)
        return request
