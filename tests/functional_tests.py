import requests
import unittest


MEASURE_URL = 'http://localhost:5000'


class ScaleTest(unittest.TestCase):

    def test_get_measurement(self):
        r = requests.get(MEASURE_URL)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.text), 8)


if __name__ == '__main__':
    unittest.main()
