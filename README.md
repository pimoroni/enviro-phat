# Enviro pHAT

https://shop.pimoroni.com/products/enviro-phat

The Pimoroni Enviro pHAT boast a plethora of sensors and connectivity for measuring your environment.

Enviro pHAT includes:

* An LSM303D accelerometer/magnetometer for detecting orientation, motion and heading
* A BMP280 temperature/pressure sensor
* A TCS3472 colour sensor, for detecting the amount and colour of light
* An ADS1015 analog sensor with four 3.3v tolerant channels for your external sensors
* A 5v power supply pin for powering your sensors, which you can regulate or divide to 3v if needed
* Two LEDs connected to GPIO #4 for illuminating objects over the colour sensor

### Note: for Enviro and Enviro Plus see: https://github.com/pimoroni/enviroplus-python/

## Installing

### Full install (recommended):

We've created an easy installation script that will install all pre-requisites and get your Enviro pHAT
up and running with minimal efforts. To run it, fire up Terminal which you'll find in Menu -> Accessories -> Terminal
on your Raspberry Pi desktop, as illustrated below:

![Finding the terminal](http://get.pimoroni.com/resources/github-repo-terminal.png)

In the new terminal window type the command exactly as it appears below (check for typos) and follow the on-screen instructions:

```bash
curl https://get.pimoroni.com/envirophat | bash
```

Alternatively, on Raspbian, you can download the `pimoroni-dashboard` and install your product by browsing to the relevant entry:

```bash
sudo apt-get install pimoroni
```
(you will find the Dashboard under 'Accessories' too, in the Pi menu - or just run `pimoroni-dashboard` at the command line)

If you choose to download examples you'll find them in `/home/pi/Pimoroni/envirophat/`.

### Manual install:

#### Library install for Python 3:

on Raspbian:

```bash
sudo apt-get install python3-envirophat
```

other environments:

```bash
sudo pip3 install envirophat
```

#### Library install for Python 2:

on Raspbian:

```bash
sudo apt-get install python-envirophat
```

other environments:

```bash
sudo pip2 install envirophat
```

### Development:

If you want to contribute, or like living on the edge of your seat by having the latest code, you should clone this repository, `cd` to the library directory, and run:

```bash
sudo python3 setup.py install
```
(or `sudo python setup.py install` whichever your primary Python environment may be)

In all cases you will have to enable the i2c bus.

## Documentation & Support

* Guides and tutorials - https://learn.pimoroni.com/enviro-phat
* Function reference - http://docs.pimoroni.com/envirophat/
* GPIO Pinout - https://pinout.xyz/pinout/enviro_phat
* Get help - http://forums.pimoroni.com/c/support
