from envirophat import light, motion, weather, analog, leds
import time

while True:
    print("LEDs on...")
    leds.on()
    time.sleep(1)
    print("LEDs off...")
    leds.off()
    print("Light...")
    print(light.rgb())
    print("Motion...")
    print(motion.heading())
    print(motion.magnetometer())
    print(motion.accelerometer())
    print("Weather...")
    print(weather.temperature())
    print(weather.pressure())
    print("Analog...")
    print(analog.values())
    time.sleep(1)
