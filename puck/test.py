import unittest
from tornado.ioloop import IOLoop
from tornado.options import options
from tornado.testing import AsyncHTTPTestCase
import main


class testBase(AsyncHTTPTestCase):
  def setUp(self):
    super(testBase, self).setUp()

  def get_app(self):
    return main.app()

  def get_http_port(self):
    return options.port

  def get_new_ioloop(self):
    return IOLoop.instance()


class testHandler(testBase):
  def test_home(self):
    res = self.fetch('/')
    self.assertIn("home", res.body)

  def test_not_found(self):
    res = self.fetch('/not_found')
    self.assertIn("Not Found", res.body)


if __name__ == "__main__":
  unittest.main()
