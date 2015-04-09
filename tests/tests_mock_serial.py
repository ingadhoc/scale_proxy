import unittest
import mock_serial


ENTRY = 'F000000\rF000000\rD000000\r'


class MockSerialTest(unittest.TestCase):

    def test_read_consume_one_caracter(self):
        serial = mock_serial.Serial(ENTRY)
        self.assertEqual(serial.read(), 'F')
        for _ in range(6):
            self.assertEqual(serial.read(), '0')
        self.assertEqual(serial.read(), '\r')

    def test_read_consumes_mutiple_characters(self):
        serial = mock_serial.Serial(ENTRY)
        self.assertEqual(serial.read(8), 'F000000\r')
        self.assertEqual(serial.read(6), 'F00000')
        self.assertEqual(serial.read(8), '0\rD00000')


if __name__ == '__main__':
    unittest.main()
