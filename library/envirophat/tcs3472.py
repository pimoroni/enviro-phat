ADDR = 0x29

REG_CMD = 0b10000000
REG_CMD_AUTO_INC = 0b00100000
REG_CLEAR_L = REG_CMD | REG_CMD_AUTO_INC | 0x14
REG_RED_L = REG_CMD | REG_CMD_AUTO_INC | 0x16
REG_GREEN_L = REG_CMD | REG_CMD_AUTO_INC | 0x18
REG_BLUE_L = REG_CMD | REG_CMD_AUTO_INC | 0x1A

REG_ENABLE = REG_CMD | 0
REG_ATIME = REG_CMD | 1
REG_CONTROL = REG_CMD | 0x0f
REG_STATUS = REG_CMD | 0x13

REG_CONTROL_GAIN_1X = 0b00000000
REG_CONTROL_GAIN_4X = 0b00000001
REG_CONTROL_GAIN_16X = 0b00000010
REG_CONTROL_GAIN_60X = 0b00000011

REG_ENABLE_INTERRUPT = 1 << 4
REG_ENABLE_WAIT = 1 << 3
REG_ENABLE_RGBC = 1 << 1
REG_ENABLE_POWER = 1

class tcs3472:
    def __init__(self, i2c_bus=None, addr=ADDR):
        self.addr = addr
        self.i2c_bus = i2c_bus
        if not hasattr(i2c_bus, "read_word_data") or not hasattr(i2c_bus, "write_byte_data"):
            raise TypeError("Object given for i2c_bus must implement read_word_data and write_byte_data")

        self.i2c_bus.write_byte_data(ADDR, REG_ENABLE, REG_ENABLE_RGBC | REG_ENABLE_POWER)
        self.set_integration_time_ms(511.2)

    def set_integration_time_ms(self, ms):
        if ms < 2.4 or ms > 612:
            raise TypeError("Integration time must be between 2.4 and 612ms")
        self._atime = int(round(ms / 2.4))
        self._max_count = min(65535, (256 - self._atime) * 1024)

        self.i2c_bus.write_byte_data(ADDR, REG_ATIME, 256 - self._atime)

    def max_count(self):
        return self._max_count

    def scaled(self):
        rgbc = self.raw()
        return tuple([float(x) / rgbc[3] for x in rgbc])

    def rgb(self):
        return tuple([int(x * 255) for x in self.scaled()][:3])

    def light(self):
        return self.raw()[3]

    def valid(self):
        return (self.i2c_bus.read_byte_data(ADDR, REG_STATUS) & 1) > 0

    def raw(self):
        #data = self.i2c_bus.read_i2c_block_data(ADDR, REG_CLEAR_L, 8)
        #c = data[0] | (data[1] << 8)
        #r = data[2] | (data[3] << 8)
        #g = data[4] | (data[5] << 8)
        #b = data[6] | (data[7] << 8)
        c = self.i2c_bus.read_word_data(ADDR, REG_CLEAR_L)
        r = self.i2c_bus.read_word_data(ADDR, REG_RED_L)
        g = self.i2c_bus.read_word_data(ADDR, REG_GREEN_L)
        b = self.i2c_bus.read_word_data(ADDR, REG_BLUE_L)
        return (r, g, b, c)
