import web
import json

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'

    def POST(self, x):
        data = str(web.data(), 'utf-8')
        #data = (web.data())
        #print(type(data), data)

        data = json.loads(data)
        print(type(data), data)

        #value = data["name"]
        #return "Hello " + value + "!"

if __name__ == "__main__":
    app.run()