import smbus
import RPi.GPIO as GPIO

bus = None

if GPIO.RPI_REVISION == 2 or GPIO.RPI_REVISION == 3:
    bus = smbus.SMBus(1)
else:
    bus = smbus.SMBus(0)
