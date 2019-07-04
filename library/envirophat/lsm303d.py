import math
import struct
import time


### LSM303 Address ###
ADDR    = 0x1D # Assuming SA0 grounded

### LSM303 Register definitions ###
TEMP_OUT_L      = 0x05
TEMP_OUT_H      = 0x06
STATUS_REG_M    = 0x07
OUT_X_L_M       = 0x08
OUT_X_H_M       = 0x09
OUT_Y_L_M       = 0x0A
OUT_Y_H_M       = 0x0B
OUT_Z_L_M       = 0x0C
OUT_Z_H_M       = 0x0D
WHO_AM_I        = 0x0F
INT_CTRL_M      = 0x12
INT_SRC_M       = 0x13
INT_THS_L_M     = 0x14
INT_THS_H_M     = 0x15
OFFSET_X_L_M    = 0x16
OFFSET_X_H_M    = 0x17
OFFSET_Y_L_M    = 0x18
OFFSET_Y_H_M    = 0x19
OFFSET_Z_L_M    = 0x1A
OFFSET_Z_H_M    = 0x1B
REFERENCE_X     = 0x1C
REFERENCE_Y     = 0x1D
REFERENCE_Z     = 0x1E
CTRL_REG0       = 0x1F
CTRL_REG1       = 0x20
CTRL_REG2       = 0x21
CTRL_REG3       = 0x22
CTRL_REG4       = 0x23
CTRL_REG5       = 0x24
CTRL_REG6       = 0x25
CTRL_REG7       = 0x26
STATUS_REG_A    = 0x27
OUT_X_L_A       = 0x28
OUT_X_H_A       = 0x29
OUT_Y_L_A       = 0x2A
OUT_Y_H_A       = 0x2B
OUT_Z_L_A       = 0x2C
OUT_Z_H_A       = 0x2D
FIFO_CTRL       = 0x2E
FIFO_SRC        = 0x2F
IG_CFG1         = 0x30
IG_SRC1         = 0x31
IG_THS1         = 0x32
IG_DUR1         = 0x33
IG_CFG2         = 0x34
IG_SRC2         = 0x35
IG_THS2         = 0x36
IG_DUR2         = 0x37
CLICK_CFG       = 0x38
CLICK_SRC       = 0x39
CLICK_THS       = 0x3A
TIME_LIMIT      = 0x3B
TIME_LATENCY    = 0x3C
TIME_WINDOW     = 0x3D
ACT_THS         = 0x3E
ACT_DUR         = 0x3F

### Mag scales ###
MAG_SCALE_2     = 0x00 # full-scale is +/- 2 Gauss
MAG_SCALE_4     = 0x20 # +/- 4 Guass
MAG_SCALE_8     = 0x40 # +/- 8 Guass
MAG_SCALE_12    = 0x60 # +/- 12 Guass

ACCEL_SCALE     = 2 # +/- 2g

X = 0
Y = 1
Z = 2

def twos_comp(val, bits):
    # Calculate the 2s complement of int:val #
    if val&(1<<(bits-1)) != 0:
        val = (val&((1<<bits)-1)) - (1<<bits)
    return val

class vector:
    def __init__(self, x, y=None, z=None):
        if type(x) == list and len(x) == 3:
            y = x[1]
            z = x[2]
            x = x[0]

        self.x = x
        self.y = y
        self.z = z

    def __getitem__(self, index):
        return (self.x, self.y, self.z)[index]

    def __str__(self):
        return str((self.x, self.y, self.z))

class lsm303d:
    _mag = [0,0,0]
    _accel = [0,0,0]
    _tiltcomp = [0,0,0]
    _heading=0
    _heading_degrees=0
    _tilt_heading=0
    _tilt_heading_degrees=0

    def __init__(self, i2c_bus=None, addr=ADDR):
        self.i2c_bus = i2c_bus

        if not hasattr(i2c_bus, "write_byte_data") or not hasattr(i2c_bus, "read_byte_data"):
            raise TypeError("Object given for i2c_bus must implement write_byte_data and read_byte_data methods")

        self.addr = addr

        self._is_setup = False

    def setup(self):
        if self._is_setup:
            return

        self._is_setup = True

        whoami = self.i2c_bus.read_byte_data(self.addr, WHO_AM_I)

        if whoami == 0x49:
            self.i2c_bus.write_byte_data(self.addr, CTRL_REG1, 0x57) # 0x57 = ODR=50hz, all accel axes on ## maybe 0x27 is Low Res?
            self.i2c_bus.write_byte_data(self.addr, CTRL_REG2, (3<<6)|(0<<3)) # set full scale +/- 2g
            self.i2c_bus.write_byte_data(self.addr, CTRL_REG3, 0x00) # no interrupt
            self.i2c_bus.write_byte_data(self.addr, CTRL_REG4, 0x00) # no interrupt
            self.i2c_bus.write_byte_data(self.addr, CTRL_REG5, 0x80|(4<<2)) # 0x10 = mag 50Hz output rate. 0x80 = enable temperature sensor
            self.i2c_bus.write_byte_data(self.addr, CTRL_REG6, MAG_SCALE_2) # Magnetic Scale +/1 1.3 Guass
            self.i2c_bus.write_byte_data(self.addr, CTRL_REG7, 0x00) # 0x00 continuous conversion mode
        else:
            raise IOError("No lsm303d detected")

    def temperature(self):
        """Read the temperature sensor and return the raw value in units of 1/8th degrees C.

        This is an uncalibrated relative temperature.
        """
        self.setup()

        # in order to read multiple bytes the high bit of the sub address must be asserted
        return twos_comp(self.i2c_bus.read_word_data(self.addr, TEMP_OUT_L|0x80), 12)

    def magnetometer(self):
        """Read the magnetomter and return the raw x, y and z magnetic readings as a vector.

        The returned vector will have properties x, y and z.
        """
        self.setup()

        # in order to read multiple bytes the high bit of the sub address must be asserted
        raw = self.i2c_bus.read_i2c_block_data(self.addr, OUT_X_L_M|0x80, 6)
        self._mag = list(struct.unpack("<hhh", bytearray(raw)))

        return vector(self._mag)

    def accelerometer(self):
        """Read the accelerometer and return the x, y and z acceleration as a vector in Gs.

        The returned vector will have properties x, y and z.
        """
        self.setup()

        # in order to read multiple bytes the high bit of the sub address must be asserted
        # so we |0x80 to enable register auto-increment
        raw = self.i2c_bus.read_i2c_block_data(self.addr, OUT_X_L_A|0x80, 6)
        accel = list(struct.unpack("<hhh", bytearray(raw)))

        for i in range(X, Z+1):
            self._accel[i] = accel[i] / math.pow(2, 15) * ACCEL_SCALE

        return vector(self._accel)

    def raw_heading(self):
        """Return a raw compas heading calculated from the magnetometer data."""

        self._heading = math.atan2(self._mag[X], self._mag[Y])

        if self._heading < 0:
            self._heading += 2*math.pi
        if self._heading > 2*math.pi:
            self._heading -= 2*math.pi

        self._heading_degrees = round(math.degrees(self._heading),2)

        return self._heading_degrees

    def heading(self):
        """Return a tilt compensated heading calculated from the magnetometer data.

        Returns None in the case of a calculation error.

        """

        self.update()

        truncate = [0,0,0]
        for i in range(X, Z+1):
            truncate[i] = math.copysign(min(math.fabs(self._accel[i]), 1.0), self._accel[i])
        try:
            pitch = math.asin(-1*truncate[X])
            roll = math.asin(truncate[Y]/math.cos(pitch)) if abs(math.cos(pitch)) >= abs(truncate[Y]) else 0
            # set roll to zero if pitch approaches -1 or 1

            self._tiltcomp[X] = self._mag[X] * math.cos(pitch) + self._mag[Z] * math.sin(pitch)
            self._tiltcomp[Y] = self._mag[X] * math.sin(roll) * math.sin(pitch) + \
                               self._mag[Y] * math.cos(roll) - self._mag[Z] * math.sin(roll) * math.cos(pitch)
            self._tiltcomp[Z] = self._mag[X] * math.cos(roll) * math.sin(pitch) + \
                               self._mag[Y] * math.sin(roll) + \
                               self._mag[Z] * math.cos(roll) * math.cos(pitch)
            self._tilt_heading = math.atan2(self._tiltcomp[Y], self._tiltcomp[X])

            if self._tilt_heading < 0:
                self._tilt_heading += 2*math.pi
            if self._tilt_heading > 2*math.pi:
                self._tilt_heading -= 2*math.pi

            self._tilt_heading_degrees = round(math.degrees(self._tilt_heading),2)
            return self._tilt_heading_degrees

        except Exception:
            return None

    def is_mag_ready(self):
        return (self.i2c_bus.read_byte_data(self.addr, STATUS_REG_M) & 0x03) > 0

    def update(self):
        """Update both the accelerometer and magnetometer data."""

        self.accelerometer()
        self.magnetometer()

