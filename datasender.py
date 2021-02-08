import requests
import json


class Datasender:
    def __init__(self):
        self.url     = "http://192.168.2.15:8080"
        self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}


def send_samples(self, samples2send):
    result = requests.post(url, data=json.dumps(data), headers=headers)
    return(result)
