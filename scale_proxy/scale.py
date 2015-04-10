class Scale(object):

    def __init__(self, serial):
        self._serial = serial

    def _read_line(self, serial):
        line = ''
        while True:
            r = self._serial.read()
            if r == '\r':
                break
            line += r
        return line

    def measure(self):
        line = self._read_line(self._serial)
        return int(line[1:])
