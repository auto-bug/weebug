import struct
from adafruit_bus_device.i2c_device import I2CDevice


class LIS3DH:
    _buffer = bytearray(6)

    def __init__(self, i2c, addr=0x18):
        self.device = I2CDevice(i2c, addr)
        with self.device:
            self._write(0x20, 0x37)  # enable, data rate 400Hz
            self._write(0x23, 0x88)  # HiRes & BDU
            self._write(0x1f, 0x80)  # ADCs

    def _write(self, register, value):
        self._buffer[0] = register
        self._buffer[1] = value
        self.device.write(self._buffer, end=2)

    def get(self):
        self._buffer[0] = 0xa8
        with self.device:
            self.device.write_then_readinto(self._buffer, self._buffer,
                out_end=1, in_end=6)
        return struct.unpack_from('<hhh', self._buffer)
