#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import inkyphat
import os
import pyowm
import math
from PIL import ImageFont, ImageDraw, ImageOps
from PIL import Image
import schedule

inkyphat.set_rotation(180)

bulb_width = 50
bulb_space = 3
bulb_fill = bulb_width - (bulb_space * 2)
margin_bottom = 5
margin_top = 5
margin_left = (inkyphat.HEIGHT - bulb_width) / 2
margin_right = (inkyphat.HEIGHT - bulb_width) / 2
fill_max = inkyphat.WIDTH - margin_top
tube_width = math.ceil((bulb_width / 3) / 2.) * 2
tube_x = margin_bottom + bulb_width
tube_y = margin_left + (bulb_width - (tube_width * 2))
tube_end = fill_max
tubeline_top_x = tube_x - 2
tubeline_top_y = tube_y - 1
tubeline_bottom_x = tubeline_top_x
tubeline_bottom_y = tube_y + tube_width + 1
fmax = fill_max - (tube_width / 2)

# Data for Openweathermap Query
owm_key = os.environ["OWM_KEY"]
owm = pyowm.OWM(owm_key)
observation = owm.weather_at_zip_code("61449","de")
w = observation.get_weather()
currtemp = w.get_temperature('celsius')['temp']

hi_temp_c = 50
low_temp_c = -20

# hi_temp_f = 122
# lo_temp_f = -4

def draw_therm():
    inkyphat.arc((margin_bottom,margin_left,margin_bottom+bulb_width,margin_right+bulb_width), 0, 360, 1)
    inkyphat.arc((margin_bottom-1,margin_left-1,margin_bottom+bulb_width+1,margin_right+bulb_width+1), 0, 360, 1)

    inkyphat.rectangle((tube_x - (bulb_width/2), tube_y, (fill_max - tube_width), (tube_y + tube_width)), 0, 0)

    inkyphat.line((tubeline_top_x, tubeline_top_y, fill_max - tube_width / 2, tubeline_top_y), 1, 1)
    inkyphat.line((tubeline_top_x, (tubeline_top_y - 1), fill_max - tube_width / 2, (tubeline_top_y - 1)), 1, 1)

    inkyphat.line((tubeline_top_x, tubeline_bottom_y, (fill_max - tube_width / 2), tubeline_bottom_y), 1, 1)
    inkyphat.line((tubeline_top_x, (tubeline_bottom_y + 1), fill_max - tube_width / 2, (tubeline_bottom_y + 1)), 1, 1)

    inkyphat.arc(((fill_max - tube_width), tubeline_top_y, fill_max, tubeline_bottom_y), 270, 90, 1)
    inkyphat.arc(((fill_max - tube_width + 1), tubeline_top_y - 1, fill_max + 1, tubeline_bottom_y + 1), 270, 90, 1)

def fill_up():
    global currtemp
    # inkyphat.pieslice((), 0, 360, 2, 2)

    # Filled bulb
    inkyphat.pieslice((margin_bottom + bulb_space, margin_left + bulb_space, margin_bottom + bulb_space + bulb_fill, margin_left + bulb_space + bulb_fill), 0, 360, 2, 2)

    # Filled tube
    #inkyphat.rectangle((tubeline_top_x - (bulb_width / 2), tubeline_top_y + bulb_space, (fill_max - tube_width + tube_width / 2), (tubeline_bottom_y - bulb_space)), 2, 2)
    if currtemp <= 0:
        inv = currtemp * -1
        inkyphat.rectangle((tubeline_top_x - (bulb_width / 2), tubeline_top_y + bulb_space, (fmax - 100 - (inv * 2)), (tubeline_bottom_y - bulb_space)), 2, 2)
    else:
        inkyphat.rectangle((tubeline_top_x - (bulb_width / 2), tubeline_top_y + bulb_space, (fmax - 140 + 40 + (currtemp * 2)), (tubeline_bottom_y - bulb_space)), 2, 2)

    # inkyphat.pieslice((tubeline_top_x - (bulb_width / 2), 42, (fill_max - tube_width + tube_width / 2), 62), 270, 90, 2, 2)

def decorate():
    # Reflection
    inkyphat.pieslice(((tubeline_bottom_x - (bulb_width / 5)), (tubeline_bottom_y - (bulb_width / 5)), (tubeline_bottom_x - (bulb_width / 5)) - 20, (tubeline_bottom_y - (bulb_width / 5)) + 10), 0, 360, 0, 0)

    # Tube reflection, broken
    #inkyphat.arc((tubeline_top_x,tubeline_top_y,tubeline_bottom_x+tube_width,tubeline_bottom_y), 90, 270, 0)

    #draw_fahrenheit_scale()
    draw_celsius_scale()

    # Draw current temperature in the bulb area
    font = ImageFont.truetype(inkyphat.fonts.PressStart2P, 9)
    text = round(currtemp) + "C"
    pr = inkyphat.text((margin_bottom + 2 + bulb_space + (bulb_width / 4),margin_left + 2 + bulb_space + (bulb_width / 4)), text, inkyphat.WHITE, font)

def draw_fahrenheit_scale():
    """Does not work"""
    inkyphat.line((fill_max - 140, 0, fill_max, 0), 1, 1)
    inkyphat.line((fill_max - 140, 1, fill_max, 1), 1, 1)
    i = 0
    while i < 126:
        if i % 10 == 0:
            inkyphat.line((fill_max - i, 2, fill_max -i, 22), 1, 1)
        else:
            inkyphat.line((fill_max - i, 2, fill_max - i, 12), 1, 1)
        i += 2

def draw_celsius_scale():
    # inkyphat.line((fill_max - 140, 102, fill_max, 102), 1, 1)
    # inkyphat.line((fill_max - 140, 103, fill_max, 103), 1, 1)
    i = 0
    while i < 141:
        if i == 100:
            inkyphat.line((fmax - i, tubeline_top_y - 5, fmax - i, tubeline_top_y - 5 - 33), 1, 1)
            inkyphat.line((fmax - i, tubeline_bottom_y + 5, fmax - i, tubeline_bottom_y + 5 + 33), 1, 1)
        elif i % 20 == 0:
            inkyphat.line((fmax - i, tubeline_top_y - 5, fmax - i, tubeline_top_y - 5 - 18), 1, 1)
            inkyphat.line((fmax - i, tubeline_bottom_y + 5, fmax - i, tubeline_bottom_y + 5 + 18), 1, 1)
            # inkyphat.line((fmax - i, 103, fmax - i, 85), 1, 1)
        elif i % 10 == 0:
            inkyphat.line((fmax - i, tubeline_top_y - 5, fmax - i, tubeline_top_y - 5 - 12), 1, 1)
            inkyphat.line((fmax - i, tubeline_bottom_y + 5, fmax - i, tubeline_bottom_y + 5 + 12), 1, 1)
            # inkyphat.line((fmax - i, 103, fmax - i, 91), 1, 1)
        elif i % 2 == 0:
            inkyphat.line((fmax - i, tubeline_top_y - 5, fmax - i, tubeline_top_y - 5 - 8), 1, 1)
            inkyphat.line((fmax - i, tubeline_bottom_y + 5, fmax - i, tubeline_bottom_y + 5 + 8), 1, 1)
            # inkyphat.line((fmax - i, 103, fmax - i, 95), 1, 1)
        else:
            inkyphat.line((fmax - i, tubeline_top_y - 5, fmax - i, tubeline_top_y - 5 - 8), 0, 0)
            inkyphat.line((fmax - i, tubeline_bottom_y + 5, fmax - i, tubeline_bottom_y + 5 + 8), 0, 0)
            # inkyphat.line((fmax - i, 103, fmax - i, 95), 0, 0)
        i += 1

def refresh():
    draw_therm()
    fill_up()
    decorate()
    inkyphat.show()

# test = "20 \xb0"
#
# inkyphat.text((150, 15), test, inkyphat.BLACK, font)

schedule.every(5).minutes.do(refresh)

while True:
    schedule.run_pending()

    time.sleep(240)
