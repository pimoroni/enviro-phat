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

CH_RED = 0
CH_GREEN = 1
CH_BLUE = 2
CH_CLEAR = 3

class tcs3472:
    def __init__(self, i2c_bus=None, addr=ADDR):
        self._is_setup = False
        self.addr = addr
        self.i2c_bus = i2c_bus
        if not hasattr(i2c_bus, "read_word_data") or not hasattr(i2c_bus, "write_byte_data"):
            raise TypeError("Object given for i2c_bus must implement read_word_data and write_byte_data")

    def setup(self):
        if self._is_setup:
            return

        self._is_setup = True

        self.i2c_bus.write_byte_data(ADDR, REG_ENABLE, REG_ENABLE_RGBC | REG_ENABLE_POWER)
        self.set_integration_time_ms(511.2)

    def set_integration_time_ms(self, ms):
        """Set the sensor integration time in milliseconds.

        :param ms: The integration time in milliseconds from 2.4 to 612, in increments of 2.4.

        """
        if ms < 2.4 or ms > 612:
            raise TypeError("Integration time must be between 2.4 and 612ms")
        self._atime = int(round(ms / 2.4))
        self._max_count = min(65535, (256 - self._atime) * 1024)

        self.setup()

        self.i2c_bus.write_byte_data(ADDR, REG_ATIME, 256 - self._atime)

    def max_count(self):
        """Return the maximum value which can be counted by a channel with the chosen integration time."""
        return self._max_count

    def scaled(self):
        """Return a tuple containing the red, green and blue colour values ranging from 0 to 1.0 scaled against the clear value."""
        rgbc = self.raw()
        if rgbc[CH_CLEAR] > 0:
            return tuple([float(x) / rgbc[CH_CLEAR] for x in rgbc])

        return (0,0,0)

    def rgb(self):
        """Return a tuple containing the red, green and blue colour values ranging 0 to 255 scaled against the clear value."""
        return tuple([int(x * 255) for x in self.scaled()][:CH_CLEAR])

    def light(self):
        """Return the clear/unfiltered light level as an integer."""
        return self.raw()[CH_CLEAR]

    def valid(self):
        self.setup()
        return (self.i2c_bus.read_byte_data(ADDR, REG_STATUS) & 1) > 0

    def raw(self):
        """Return the raw red, green, blue and clear channels"""
        self.setup()

        c = self.i2c_bus.read_word_data(ADDR, REG_CLEAR_L)
        r = self.i2c_bus.read_word_data(ADDR, REG_RED_L)
        g = self.i2c_bus.read_word_data(ADDR, REG_GREEN_L)
        b = self.i2c_bus.read_word_data(ADDR, REG_BLUE_L)

        return (r, g, b, c)
