from .i2c_bus import bus, altbus
from .ads1015 import ads1015
from .bmp280 import bmp280
from .leds import leds
from .lsm303d import lsm303d
from .tcs3472 import tcs3472

leds = leds()

try:
    light = tcs3472(bus)
    weather = bmp280(bus)
    analog = ads1015(bus)
    motion = lsm303d(bus)
except IOError:
    print "can't find Enviro pHAT on the i2c1 bus"

try:
    altlight = tcs3472(altbus)
    altweather = bmp280(altbus)
    altanalog = ads1015(altbus)
    altmotion = lsm303d(altbus)
except IOError:
    pass
