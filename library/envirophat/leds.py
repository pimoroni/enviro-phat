import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.output(4, 0)

class leds:
    def __init__(self, status=0):
        self.status = status

    def on(self):
        self.status = 1
        GPIO.output(4, 1)
        return True

    def off(self):
        self.status = 0
        GPIO.output(4, 0)

    def is_on(self):
        if self.status == 1:
            return True
        else:
            return False

    def is_off(self):
        if self.status == 0:
            return True
        else:
            return False
