from scale_proxy import scale
import unittest
import mock_serial


MEASUREMENTS = 'F000000\rF000671\rD000000\r'


class ScaleTest(unittest.TestCase):

    def _get_mock_serial(self):
        return mock_serial.Serial(MEASUREMENTS)

    def test_get_measurement(self):
        serial = self._get_mock_serial()
        sc = scale.Scale(serial)
        self.assertEquals(sc.measure(), 0)
        self.assertEquals(sc.measure(), 671)
        self.assertEquals(sc.measure(), 0)


if __name__ == '__main__':
    unittest.main()
