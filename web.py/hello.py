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
        query = web.input()
        print(query)
        # print(web.ctx.env)
        return open(r'D:\\CODING\\python-on-the-way\\web.py\\html\\form.html', 'r').read().encode('utf-8').decode('utf-8')

if __name__ == "__main__":
    app.run()
