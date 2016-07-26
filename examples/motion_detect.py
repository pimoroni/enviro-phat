#!/usr/bin/env python

import time

from envirophat import motion, leds


print("""This example will detect motion using the accelerometer.

Press Ctrl+C to exit.

""")

threshold = 0.2
readings = []
last_z = 0

try:
    while True:
        readings.append(motion.accelerometer().z)
        readings = readings[-4:]
        z = sum(readings) / len(readings)
        if last_z > 0 and abs(z-last_z) > threshold:
            print("Motion Detected!!!")
            leds.on()
        last_z = z
        time.sleep(0.01)
        leds.off()
except KeyboardInterrupt:
    pass
