#!/usr/bin/env python

import sys
import time

from envirophat import light, weather, motion, analog

unit = 'hPa' # Pressure unit, can be either hPa (hectopascals) or Pa (pascals)

def write(line):
    sys.stdout.write(line)
    sys.stdout.flush()

write("--- Enviro pHAT Monitoring ---")

try:
    while True:
        rgb = light.rgb()
        analog_values = analog.read_all()
        mag_values = motion.magnetometer()
        acc_values = [round(x,2) for x in motion.accelerometer()]

        output = """
Temp: {t:.2f}c
Pressure: {p:.2f}{unit}
Altitude: {a:.2f}m
Light: {c}
RGB: {r}, {g}, {b} 
Heading: {h}
Magnetometer: {mx} {my} {mz}
Accelerometer: {ax}g {ay}g {az}g
Analog: 0: {a0}, 1: {a1}, 2: {a2}, 3: {a3}

""".format(
        unit = unit,
        a = weather.altitude(), # Supply your local qnh for more accurate readings
        t = weather.temperature(),
        p = weather.pressure(unit=unit),
        c = light.light(),
        r = rgb[0],
        g = rgb[1],
        b = rgb[2],
        h = motion.heading(),
        a0 = analog_values[0],
        a1 = analog_values[1],
        a2 = analog_values[2],
        a3 = analog_values[3],
        mx = mag_values[0],
        my = mag_values[1],
        mz = mag_values[2],
        ax = acc_values[0],
        ay = acc_values[1],
        az = acc_values[2]
    )
        output = output.replace("\n","\n\033[K")
        write(output)
        lines = len(output.split("\n"))
        write("\033[{}A".format(lines - 1))

        time.sleep(1)
        
except KeyboardInterrupt:
    pass
