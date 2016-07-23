#!/usr/bin/env python

from envirophat import weather, leds
import time

print("""This example will detect motion using the accelerometer.

Press Ctrl+C to exit.

""")

threshold = None

try:
    while True:
        temperature = weather.temperature()

        if threshold is None:
            threshold = temperature + 2

        print("{} degrees celcius".format(temperature))
        if temperature > threshold:
            leds.on()
        else:
            leds.off()

        time.sleep(0.1)

except KeyboardInterrupt:
    pass
