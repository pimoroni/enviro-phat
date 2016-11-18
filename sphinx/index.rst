.. role:: python(code)
   :language: python

.. toctree::
   :titlesonly:
   :maxdepth: 0

.. module:: envirophat

Welcome
-------

This documentation will guide you through the methods available in the Enviro pHAT python library.

Enviro pHAT is an environmental sensor add-on, packing 4 different sensors, letting you measure temperature, pressure, light level, colour, 3-axis motion, compass heading, and analog inputs.

* More information - https://shop.pimoroni.com/products/enviro-phat
* Getting started - https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-enviro-phat
* GPIO Pinout - http://pinout.xyz/pinout/enviro_phat
* Get the code - https://github.com/pimoroni/enviro-phat
* Get help - http://forums.pimoroni.com/c/support

At A Glance
-----------

.. automethodoutline:: light.rgb
.. automethodoutline:: light.light
.. automethodoutline:: light.raw
.. automethodoutline:: leds.on
.. automethodoutline:: leds.off
.. automethodoutline:: weather.temperature
.. automethodoutline:: weather.pressure
.. automethodoutline:: weather.altitude
.. automethodoutline:: weather.update
.. automethodoutline:: analog.read
.. automethodoutline:: analog.read_all
.. automethodoutline:: analog.available
.. automethodoutline:: motion.magnetometer
.. automethodoutline:: motion.accelerometer
.. automethodoutline:: motion.heading
.. automethodoutline:: motion.raw_heading
.. automethodoutline:: motion.update

Light
-----

Light sensing is provided by a TCS3472 colour sensor, with filtered channels for Red, Green and Blue. plus an unfiltered "Light" channel.

.. automethod:: light.rgb
.. automethod:: light.light
.. automethod:: light.raw

For colour sensing, two LEDs are placed either side of the TCS3472 to illuminate the subject.

.. automethod:: leds.on
.. automethod:: leds.off

Weather
-------

Weather sensing is provided by a BMP280. The altitude is approximated from atmospheric pressure.

.. automethod:: weather.temperature
.. automethod:: weather.pressure
.. automethod:: weather.altitude
.. automethod:: weather.update

Analog
------

The four channels of Analog input are provided by an ADS1015.

.. automethod:: analog.read
.. automethod:: analog.read_all
.. automethod:: analog.available

Motion
------

Motion sensing is provided by an LSM303D accelerometer and magnetometer. The compass heading is approximated.

.. automethod:: motion.magnetometer
.. automethod:: motion.accelerometer
.. automethod:: motion.heading
.. automethod:: motion.raw_heading
.. automethod:: motion.update
