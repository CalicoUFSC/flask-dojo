import unittest

from app import app


class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello_world(self):
        result = self.app.get('/')
        self.assertEqual(b'Hello World!', result.data)
        self.assertEqual(200, result.status_code)

    def test_hello_name(self):
        result = self.app.get('/test')
        self.assertEqual(b'Hello, test!', result.data)
        self.assertEqual(200, result.status_code)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
