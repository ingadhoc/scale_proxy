class Serial(object):

    def __init__(self, data):
        self._data = data

    def read(self, qty=1):
        read, data = self._data[0:qty], self._data[qty:]
        self._data = data
        return read
