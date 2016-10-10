import tornado.web
import tornado.ioloop

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = ['qeq', 'da', 'deb']
        self.render('qeq.html', title='Hello world', items=items, error=tornado.web.HTTPError(302))
    def post(self):
        print(self.get_arguments(name='age'))
        self.write('Nice arguments, bitch.')

app = tornado.web.Application([
    (r'/', MainHandler),
])

class ContactHandler(tornado.web.RequestHandler):
    def post(self):
        print(self.get_arguments())
        self.write('Nice arguments, bitch.')

app.listen(8888)
tornado.ioloop.IOLoop.instance().start()

