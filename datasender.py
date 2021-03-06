import requests
import json
import datetime


class Datasender:
    def __init__(self):
        #self.url     = "http://192.168.2.18:5000"
        self.url     = "http://rest:5000"
        self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}


    def jsondefaults(self, field):
        if isinstance(field, (datetime.date, datetime.datetime)):
            return field.isoformat()


    def send_samples(self, samples2send):
        json2send = json.dumps(samples2send, default=self.jsondefaults)
        try:
            result = requests.post(self.url, data=(json2send), headers=self.headers, timeout=5)
            #return(result)
        except requests.ConnectionError:
            return("error")
