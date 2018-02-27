#!/usr/bin/env python

# Use the Enviro pHAT to check how much light is in a room, then trigger a webhook to control
# Philips Hue lights via IFTTT. By Wesley Archer (@raspberrycoulis).

# Import the relevant modules

import requests
import time
import datetime
import os
from envirophat import light

# Get the current time for displaying in the terminal.
def whats_the_time():
    now = datetime.datetime.now()
    return (now.strftime("%H:%M:%S"))

# The function to turn off the lights. Sends a webhook to IFTTT which
# triggers Hue. Replace the trigger word and tokens from your account.

def turn_off():
    requests.post("https://maker.ifttt.com/trigger/{TRIGGER_WORD}/with/key/{TOKEN_GOES_HERE}")
    print("Lights off!")

# The function to turn on the lights. Sends a webhook to IFTTT which                   
# triggers Hue. Replace the trigger word and tokens from your account.

def turn_on():
    requests.post("https://maker.ifttt.com/trigger/{TRIGGER_WORD}/with/key/{TOKEN_GOES_HERE}")
    print("Lights on!")

# Check the light level and determine whether the lights need to 
# be turned on or off.

def average_lux():
    # Variables for calculating the average lux levels
    start_time = time.time()
    curr_time = time.time()
    collect_light_time = 60
    collect_light_data = []

    # Calculate the average lux level over 60 seconds
    print("Calculating average light level...")
    while curr_time - start_time < collect_light_time:
	      curr_time = time.time()
	      avg = light.light()
	      collect_light_data.append(avg)
	  time.sleep(1)
    average_light = sum(collect_light_data[-10:]) / 10.0
    now = whats_the_time()
    print("{} {} {} {} {} {} {} {}.".format("Average over", collect_light_time, "seconds", "is:", average_light, "lux.", "Last checked at", now))
    print("{} {} {} {}.".format("Waiting", "90", "seconds", "before trying again"))
    return average_light

try:
    # Local variables.
    state = 0	# Sets the state for the lights.
    low = 260	# Low value for light level (lux).
    high = 300	# High value for light level (lux).
    period = 90	# Delay, in seconds, between calls.
    while True:
	# Get the average lux level first,
	room_light = average_lux()
	# Now check if the room is dark enough then turn on the lights.
	if room_light < low and state != 1:
	    turn_on()
	    state = 1
	# Or if it is bright enough, turn off the lights.
	elif room_light > high and state == 1:
	    turn_off()
	    state = 0
	time.sleep(period)
except KeyboardInterrupt:
    pass
