import web
import json
import datastore as ds

urls = (
    '/(.*)', 'hello'
)



app = web.application(urls, globals())

#database = ds.Datastore("mem")

class hello:
    def __init__(self):
        pass
        #database = ds.Datastore("lite")

    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'

    def POST(self, x):
        data = str(web.data(), 'utf-8')
        data = json.loads(data)
        #print(type(data), data)

        for row in data:
            print(row)

        return("oke")
            #database.store_sample(row[1], row[2], (row[5],), row[6])
        
        #samples = database.read_all_samples()
        #print(samples)

        #value = data["name"]
        #return "Hello " + value + "!"

if __name__ == "__main__":
    app.run()