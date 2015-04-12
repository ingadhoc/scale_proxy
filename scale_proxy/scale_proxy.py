import scale
import serial
from flask import Flask
from flask.ext.cors import CORS


app = Flask(__name__)
app.config.update(PROPAGATE_EXCEPTIONS=True)
cors = CORS(app)


@app.route('/measure')
def measure():
    return str(_scale.measure())


@app.route('/test')
def ping():
    return 'test'


def _get_serial():
    return serial.Serial(0, timeout=2, baudrate=1200)


def _get_scale(serial):
    return scale.Scale(serial)


def config_and_get_scale():
    return _get_scale(_get_serial())


_scale = config_and_get_scale()


if __name__ == "__main__":
    app.run()
