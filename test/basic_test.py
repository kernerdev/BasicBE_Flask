import unittest
from src.main import app


class BasicTestCase(unittest.TestCase):

    def test_basic(self):
        tester = app.test_client(self)
        response = tester.get('/hello', content_type='application/json')
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"message":"Hello, World!"}')


if __name__ == '__main__':
    unittest.main()
