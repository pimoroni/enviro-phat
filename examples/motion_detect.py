print("""This example will detect motion using the accelerometer.

Press Ctrl+C to exit.

""")

import time
from envirophat import motion, leds

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
            leds(1)
        last_z = z
        time.sleep(0.01)
        leds(0)
except KeyboardInterrupt:
    pass
