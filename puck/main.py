import os
from tornado import ioloop
from tornado.web import Application
from tornado.options import options, parse_config_file, parse_command_line
from handler import router

_dir = os.path.dirname(__file__)
parse_config_file(os.path.join(_dir, 'setting.py'))
parse_command_line()


class app(Application):

  def __init__(self):
    settings = dict(
      static_path=os.path.join(_dir, "static"),
      template_path=os.path.join(_dir, "tpl"),
      #cookie_secret=options.cookie_secret,
      debug=options.debug,
      gzip=True,
    )
    Application.__init__(self, router, **settings)


def main():
  app().listen(options.port)
  ioloop.IOLoop.instance().start()


if __name__ == "__main__":
  main()
