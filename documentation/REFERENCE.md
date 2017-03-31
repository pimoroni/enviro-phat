# Enviro pHAT Function Reference
for full API documentation, see http://docs.pimoroni.com/envirophat/

You can import one or more devices from the Enviro pHAT library, which has:

* light
* motion
* weather
* analog
* leds

For example:

```python
from envirophat import motion, light
```

## Weather

Weather is monitored by the BMP280 temperature/pressure sensor.

Get the temperature in degrees C:

```
weather.temperature()
```

Get the pressure in hPA:

```
weather.pressure()
```

## Light

Light sensing is provided by a TCS3472 colour sensor, which has 4 light sensors inside with different filters in front of them. 3 of these are red, blue and green, and the 4th is unfiltered to provide a light level for comparison. It's usually referred to as "clear".

Get the colour of the light, adjusted against clear and scaled to 0-255:

```
r, g, b = light.rgb()
```

Get the amount of light detected:

```
light.light()
```

## Motion

The LSM303D can detect the motion, orientation and magnetic heading of your Pi.

Get the raw accelerometer data:

```
x, y, z = motion.accelerometer()
```

Get your Pi's offset, in degrees, from magnetic north:

```
motion.heading()
```

You can also get the raw magnetometer data, but you'll have to get creative
to do something useful with it!

```
x,y,z = motion.magnetometer()
```

## Analog

Enviro pHAT uses an ADS1015 to provide four 3.3v tolerant analog inputs and a 5v power supply pin for your external sensors.

You can read all of the analog readings at once like so:

```
analog.read_all()
```

This will return 4 floating point values between 0.0 and 3.3v, directly mapping to the detected voltage.
