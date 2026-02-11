#import pytest
import requests
import api_framework.config as config
from urllib.parse import urljoin


def send_get_request(endpoint):
     endpoint = urljoin(config.API_BASEPOINT, endpoint)
     return requests.get(endpoint)

def send_post_request(endpoint, data):
     endpoint = urljoin(config.API_BASEPOINT, endpoint)
     return requests.post(endpoint, json=data)

def send_delete_request(endpoint):
     endpoint = urljoin(config.API_BASEPOINT, endpoint)
     return requests.delete(endpoint)




