#!/usr/bin/env python

'''This example uses two enviro pHATs, one on the i2c1 bus and'''
'''another on the i2c0 bus for reference or delta calculations'''


import sys
import time

from envirophat import leds, light, weather, motion, analog
from envirophat import altleds, altlight, altweather, altmotion, altanalog

leds.on()
time.sleep(1)
leds.off()
altleds.on()
time.sleep(1)
altleds.off()


def write(line):
    sys.stdout.write(line)
    sys.stdout.flush()

write("\n--- Enviro pHAT Monitoring ---\n")

try:
    while True:
        rgb1 = light.rgb()
        rgb0 = altlight.rgb()
        analog1_values = analog.read_all()
        analog0_values = altanalog.read_all()

        output = """
Temp1: {t1}c
Temp0: {t0}c

Pressure1: {p1}Pa
Pressure0: {p0}Pa

Light1: {c1}
Light0: {c0}

RGB1: {r1}, {g1}, {b1}
RGB0: {r0}, {g0}, {b0}

Heading1: {h1}
Heading0: {h0}

Analog1: 0: {a0}, 1: {a1}, 2: {a2}, 3: {a3}
Analog0: 0: {v0}, 1: {v1}, 2: {v2}, 3: {v3}
""".format(
        t1 = round(weather.temperature(),2),
        t0 = round(altweather.temperature(),2),
        p1 = round(weather.pressure(),2),
        p0 = round(altweather.pressure(),2),
        c1 = light.light(),
        c0 = altlight.light(),
        r1 = rgb1[0],
        g1 = rgb1[1],
        b1 = rgb1[2],
        r0 = rgb0[0],
        g0 = rgb0[1],
        b0 = rgb0[2],
        h1 = motion.heading(),
        h0 = altmotion.heading(),
        a0 = analog1_values[0],
        a1 = analog1_values[1],
        a2 = analog1_values[2],
        a3 = analog1_values[3],
        v0 = analog0_values[0],
        v1 = analog0_values[1],
        v2 = analog0_values[2],
        v3 = analog0_values[3]
    )
        output = output.replace("\n","\n\033[K")
        write(output)
        lines = len(output.split("\n"))
        write("\033[{}A".format(lines - 1))

        time.sleep(1)

except KeyboardInterrupt:
    pass
