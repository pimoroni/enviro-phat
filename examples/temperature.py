#!/usr/bin/env python

import time

from envirophat import weather, leds


print("""Light the LEDs upon temperature increase.

Press Ctrl+C to exit.

""")

threshold = None

try:
    while True:
        temperature = weather.temperature()

        if threshold is None:
            threshold = temperature + 2

        print("{} degrees Celsius".format(temperature))
        if temperature > threshold:
            leds.on()
        else:
            leds.off()

        time.sleep(0.1)

except KeyboardInterrupt:
    pass
