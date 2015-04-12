import requests
import unittest


MEASURE_URL = 'http://localhost:5000/measure'
TEST_URL = 'http://localhost:5000/test'


class ScaleTest(unittest.TestCase):

    def test_get_measurement(self):
        r = requests.get(MEASURE_URL)
        self.assertEqual(r.status_code, 200)
        self.assertTrue(r.text.isdigit())

    def test_test_url_returns_someting(self):
        r = requests.get(TEST_URL)
        self.assertEqual(r.status_code, 200)
        self.assertGreater(len(r.text), 0)


if __name__ == '__main__':
    unittest.main()
