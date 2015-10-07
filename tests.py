import unittest

from app import app


class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_save(self):
        result = self.app.post('/save', data={'content':'test'})
        self.assertEqual(result.data, b'test')
        self.assertEqual(result.status_code, 200)


    def tearDown(self):
        pass




if __name__ == '__main__':
    unittest.main()
