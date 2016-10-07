try:
    import RPi.GPIO as GPIO
except ImportError:
    exit("This library requires the RPi.GPIO module\nInstall with: sudo pip install RPi.GPIO")


pin = 4
altpin = 5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, 0)
GPIO.setup(altpin, GPIO.OUT)
GPIO.output(altpin, 0)

class leds:
    def __init__(self, status=0):
        self.status = status

    def on(self):
        """Turn LED on."""
        self.status = 1
        GPIO.output(pin, 1)
        return True

    def off(self):
        """Turn LED off."""
        self.status = 0
        GPIO.output(pin, 0)

    def is_on(self):
        """Return True if LED is on."""
        if self.status == 1:
            return True
        else:
            return False

    def is_off(self):
        """Return True if LED is off."""
        if self.status == 0:
            return True
        else:
            return False
