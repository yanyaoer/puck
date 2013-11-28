from tornado.web import RequestHandler


class base(RequestHandler):
  pass


class home(base):
  def get(self, *args):
    self.write('home')


router = [
  (r"/(home/)?", home),
]
