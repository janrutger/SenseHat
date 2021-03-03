import web
import json
import datastore as ds

urls = (
    '/(.*)', 'root'
)



app = web.application(urls, globals())

#database = ds.Datastore("mem")

class root:
    def __init__(self):
        pass
        #database = ds.Datastore("lite")

    def GET(self, name):
        return("Hello Sensehat Station")

    def POST(self, x):
        data = str(web.data(), 'utf-8')
        data = json.loads(data)

        for row in data:
            print(row)

        return("oke")
        

if __name__ == "__main__":
    app.run()