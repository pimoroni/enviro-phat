from sys import exit

from .i2c_bus import bus
try:
    from .i2c_bus import altbus
except ImportError:
    pass

from .ads1015 import ads1015
from .bmp280 import bmp280
from .lsm303d import lsm303d
from .tcs3472 import tcs3472
from .leds import leds

leds = leds()
mainbus = bus

try:
    light = tcs3472(bus)
    weather = bmp280(bus)
    analog = ads1015(bus)
    motion = lsm303d(bus)
except IOError:
    mainbus = None

if mainbus == None:
    try:
        light = tcs3472(altbus)
        weather = bmp280(altbus)
        analog = ads1015(altbus)
        motion = lsm303d(altbus) 
    except (NameError, IOError):
        exit("Enviro pHAT can't be detected!")
else:
    try:
        altlight = tcs3472(altbus)
        altweather = bmp280(altbus)
        altanalog = ads1015(altbus)
        altmotion = lsm303d(altbus) 
    except (NameError, IOError):
        pass
