import requests
import json
import datetime


class Datasender:
    def __init__(self):
        self.url     = "http://192.168.2.15:8080"
        self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}


    def jsondefault(self, field):
        if isinstance(field, (datetime.date, datetime.datetime)):
            return field.isoformat()


    def send_samples(self, samples2send):
        json2send = json.dumps(samples2send, default=self.jsondefault)
        result = requests.post(self.url, data=(json2send), headers=self.headers)
        return(result)
