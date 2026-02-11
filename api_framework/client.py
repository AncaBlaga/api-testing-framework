#import pytest
import requests
import apiframework.config as config
from urllib.parse import urljoin
"""
def set_up():
     if requests.get(config.API_BASEPOINT).ok:
          return True
     else: ""

"""

def send_get_request(endpoint):
     endpoint = urljoin(config.API_BASEPOINT, endpoint)
     return requests.get(endpoint)



