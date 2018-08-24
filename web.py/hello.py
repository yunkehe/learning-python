# 请求参数获取  web.input()
# 请求头获取    web.ctx.env
import web
        
urls = (
    '/index', 'index',
    '/blog/\d+', 'blog',
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class index():
    """docstring for index"""
    def GET(self):
        query = web.input()
        return query

class blog():
    def GET(self, id):
        return 'blog get ' + id

    def POST(self):
        query = web.input()
        return query

class hello:        
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'
        # return open(r'./html/1.html', 'r').read()

if __name__ == "__main__":
    app.run()