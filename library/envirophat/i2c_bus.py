from sys import exit, version_info

try:
    from smbus import SMBus
except ImportError:
    if version_info[0] < 3:
        exit("This library requires python-smbus\nInstall with: sudo apt-get install python-smbus")
    elif version_info[0] == 3:
        exit("This library requires python3-smbus\nInstall with: sudo apt-get install python3-smbus")

try:
    import RPi.GPIO as GPIO
except ImportError:
    exit("This library requires the RPi.GPIO module\nInstall with: sudo pip install RPi.GPIO")


bus = None
altbus = None

if GPIO.RPI_REVISION == 2 or GPIO.RPI_REVISION == 3:
    try:
        bus = SMBus(1)
    except IOError:
        exit("Creating instance of class SMBus failed\nCheck that the I2C interface is enabled!")
    try:
        altbus = SMBus(0)
    except IOError:
        pass
else:
    try:
        bus = SMBus(0)
    except IOError:
        exit("Creating instance of class SMBus failed\nCheck that the I2C interface is enabled!")
