import unittest

from app import app


class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_prime(self):
        result = self.app.get('/1')
        self.assertEqual(result.data, b"Yes!!")

    def tearDown(self):
        pass




if __name__ == '__main__':
    unittest.main()
