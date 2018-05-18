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
    # Set your trigger word - e.g. "light" - and the IFTTT Webhook token below.
    TRIGGER_WORD = "YOUR CHOSEN TRIGGER WORD GOES HERE"
    TOKEN = "YOUR IFTTT TOKEN GOES HERE"

    requests.post("https://maker.ifttt.com/trigger/{trigger_word}/with/key/{token}".format(trigger_word=TRIGGER_WORD, token=TOKEN))
    print("Lights off!")

# The function to turn on the lights. Sends a webhook to IFTTT which                   
# triggers Hue. Replace the trigger word and tokens from your account.

def turn_on():
    # Set your trigger word - e.g. "dark" - and the IFTTT Webhook token below.
    TRIGGER_WORD = "YOUR CHOSEN TRIGGER WORD GOES HERE"
    TOKEN = "YOUR IFTTT TOKEN GOES HERE"

    requests.post("https://maker.ifttt.com/trigger/{trigger_word}/with/key/{token}".format(trigger_word=TRIGGER_WORD, token=TOKEN))
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
    # Take the last 45 data points taken over 60 seconds to calculate the average
    average_light = sum(collect_light_data[-45:]) / 45.0
    now = whats_the_time()
    print("Average over {collect_time} seconds is: {average} lux. Last checked at {time}".format(
        collect_time=collect_light_time,
        average=average_light,
        time=now
    ))
    return average_light

try:
    # Local variables.
    low = 260	# Low value for light level (lux).
    high = 300	# High value for light level (lux).
    period = 90	# Delay, in seconds, between calls.
    lights_on = False # Set the state of the lights to off.
    while True:
	# Get the average lux level first,
	room_light = average_lux()
	# Now check if the room is dark enough then turn on the lights.
	if room_light < low and not lights_on:
	    turn_on()
	    lights_on = True
	elif room_light > high and lights_on:
	    turn_off()
	    lights_on = False
	print("Waiting {} seconds before trying again".format(period))
	time.sleep(period)
except KeyboardInterrupt:
    pass
