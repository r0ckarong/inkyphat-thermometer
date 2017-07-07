#!/usr/bin/env python
# -*- coding: utf-8 -*-

import inkyphat
import math
import PIL
from PIL import ImageFont

inkyphat.set_rotation(180)

font = ImageFont.truetype(inkyphat.fonts.AmaticSC, 12)

bulb_width = 48
bulb_space = 5
bulb_fill = bulb_width - (bulb_space * 2)
margin_bottom = 5
margin_top = 5
margin_left = (inkyphat.HEIGHT - bulb_width) / 2
margin_right = (inkyphat.HEIGHT - bulb_width) / 2
fill_max = inkyphat.WIDTH - margin_top - 2
tube_width = math.ceil((bulb_width / 3) / 2.) * 2
tube_x = margin_bottom + bulb_width
tube_y = margin_left + (bulb_width - (tube_width * 2))
tube_end = fill_max

hi_temp_c = 50
low_temp_c = -20

hi_temp_f = 122
lo_temp_f = -4

hipoint = fill_max

# bulb_open_left =
# bulb_open_right =

def draw_therm():
    inkyphat.arc((margin_bottom,margin_left,margin_bottom+bulb_width,margin_right+bulb_width), 0, 360, 1)
    inkyphat.arc((margin_bottom-1,margin_left-1,margin_bottom+bulb_width+1,margin_right+bulb_width+1), 0, 360, 1)
    inkyphat.rectangle((tube_x - (bulb_width/2), tube_y, (fill_max - tube_width), (tube_y + tube_width)), 0, 0)

    tubeline_top_x = tube_x - 2
    tubeline_top_y = tube_y - 1

    tubeline_bottom_x = tubeline_top_x
    tubeline_bottom_y = tube_y + tube_width + 1

    inkyphat.line((tubeline_top_x, tubeline_top_y, fill_max - tube_width / 2, tubeline_top_y), 1, 1)
    inkyphat.line((tubeline_top_x, (tubeline_top_y - 1), fill_max - tube_width / 2, (tubeline_top_y - 1)), 1, 1)

    inkyphat.line((tubeline_top_x, tubeline_bottom_y, (fill_max - tube_width / 2), tubeline_bottom_y), 1, 1)
    inkyphat.line((tubeline_top_x, (tubeline_bottom_y + 1), fill_max - tube_width / 2, (tubeline_bottom_y + 1)), 1, 1)

    inkyphat.arc(((fill_max - tube_width), tubeline_top_y, fill_max, tubeline_bottom_y), 270, 90, 1)
    inkyphat.arc(((fill_max - tube_width + 1), tubeline_top_y - 1, fill_max + 1, tubeline_bottom_y + 1), 270, 90, 1)

def draw_tube():
    # Upper part of tube
    inkyphat.line((65, 36, 200, 37), 1, 1)
    inkyphat.line((65, 37, 200, 36), 1, 1)

    # Lower part of tube
    inkyphat.line((65, 66, 200, 66), 1, 1)
    inkyphat.line((65, 67, 200, 67), 1, 1)

    # Round top of tube
    inkyphat.arc((187, 37, inkyphat.WIDTH - margin_top, 66), 270, 90, 1)
    inkyphat.arc((186, 37, (inkyphat.WIDTH - margin_top) + 1, 67), 270, 90, 1)

def fill_up():
    # Filled bulb
    inkyphat.pieslice((margin_bottom + bulb_space, margin_left + bulb_space, margin_bottom + bulb_space + bulb_fill, margin_left + bulb_space + bulb_fill), 0, 360, 2, 2)

    # Filled tube
    inkyphat.rectangle((60, 42, 190, 61), 2, 2)
    inkyphat.pieslice((180, 42, 202, 62), 270, 90, 2, 2)

def decorate():
    # Reflection
    inkyphat.pieslice((40, 52, 52, 64), 0, 360, 0, 0)

    #draw_fahrenheit_scale()
    draw_celsius_scale()

def draw_fahrenheit_scale():
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
            inkyphat.line((fill_max - i, 103, fill_max - i, 70), 1, 1)
        elif i % 20 == 0:
            inkyphat.line((fill_max - i, 103, fill_max - i, 85), 1, 1)
        elif i % 10 == 0:
            inkyphat.line((fill_max - i, 103, fill_max - i, 91), 1, 1)
        elif i % 2 == 0:
            inkyphat.line((fill_max - i, 103, fill_max - i, 95), 1, 1)
        else:
            inkyphat.line((fill_max - i, 103, fill_max - i, 95), 0, 0)
        i += 1

#test = "20 \xb0"

#inkyphat.text((180, 15), test, inkyphat.BLACK, font).rotate(90)

#draw_bulb()
#draw_tube()
draw_therm()
#fill_up()
decorate()

inkyphat.show()
