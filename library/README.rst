Enviro pHAT
===========

https://shop.pimoroni.com/products/enviro-phat

The Pimoroni Enviro pHAT boast a plethora of sensors and connectivity
for measuring your environment.

Enviro pHAT includes:

-  An LSM303D accelerometer/magnetometer for detecting orientation,
   motion and heading
-  A BMP280 temperature/pressure sensor
-  A TCS3472 colour sensor, for detecting the amount and colour of light
-  An ADS1015 analog sensor with four 3.3v tolerant channels for your
   external sensors
-  A 5v power supply pin for powering your sensors, which you can
   regulate or divide to 3v if needed
-  Two LEDs connected to GPIO #4 for illuminating objects over the
   colour sensor

Installing
----------

Full install (recommended):
~~~~~~~~~~~~~~~~~~~~~~~~~~~

We’ve created an easy installation script that will install all
pre-requisites and get your Enviro pHAT up and running with minimal
efforts. To run it, fire up Terminal which you’ll find in Menu ->
Accessories -> Terminal on your Raspberry Pi desktop, as illustrated
below:

.. figure:: http://get.pimoroni.com/resources/github-repo-terminal.png
   :alt: Finding the terminal

   Finding the terminal

In the new terminal window type the command exactly as it appears below
(check for typos) and follow the on-screen instructions:

.. code:: bash

   curl https://get.pimoroni.com/envirophat | bash

Alternatively, on Raspbian, you can download the ``pimoroni-dashboard``
and install your product by browsing to the relevant entry:

.. code:: bash

   sudo apt-get install pimoroni

(you will find the Dashboard under ‘Accessories’ too, in the Pi menu -
or just run ``pimoroni-dashboard`` at the command line)

If you choose to download examples you’ll find them in
``/home/pi/Pimoroni/envirophat/``.

Manual install:
~~~~~~~~~~~~~~~

Library install for Python 3:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

on Raspbian:

.. code:: bash

   sudo apt-get install python3-envirophat

other environments:

.. code:: bash

   sudo pip3 install envirophat

Library install for Python 2:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

on Raspbian:

.. code:: bash

   sudo apt-get install python-envirophat

other environments:

.. code:: bash

   sudo pip2 install envirophat

Development:
~~~~~~~~~~~~

If you want to contribute, or like living on the edge of your seat by
having the latest code, you should clone this repository, ``cd`` to the
library directory, and run:

.. code:: bash

   sudo python3 setup.py install

(or ``sudo python setup.py install`` whichever your primary Python
environment may be)

In all cases you will have to enable the i2c bus.

Documentation & Support
-----------------------

-  Guides and tutorials - https://learn.pimoroni.com/enviro-phat
-  Function reference - http://docs.pimoroni.com/envirophat/
-  GPIO Pinout - https://pinout.xyz/pinout/enviro_phat
-  Get help - http://forums.pimoroni.com/c/support

1.0.1
-----

* Fix: Corrected upper bounds check for tilt_heading

1.0.0
-----

* Fix: Defer setup to avoid import side-effects
* Fix: QNH changed to ISA standard
* Tweak: New Enviro pHAT I2C addr now default
* Added: unit argument to pressure to choose Pa or hPa

0.0.6
-----

* Added __version__ to module
* Added DocStrings

0.0.5
-----

* Bug fix to lsm303d raw_heading

0.0.4
-----

* Tidy up of read functions in bmp280
* Fixed incorrect call to pressure method

0.0.3
-----

* Python3 fix

0.0.2
-----

* Bug fixes

0.0.1
-----

* Initial release

