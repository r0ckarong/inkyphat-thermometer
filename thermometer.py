#!/usr/bin/env python
# -*- coding: utf-8 -*-

import inkyphat
import PIL
from PIL import ImageFont

inkyphat.set_rotation(180)

font = ImageFont.truetype(inkyphat.fonts.AmaticSC, 12)

bulb_width = 64
bulb_space = 5
bulb_fill = bulb_width - (bulb_space * 2)
margin_bottom = 5
margin_top = 5
margin_left = (inkyphat.HEIGHT - bulb_width) / 2
margin_right = (inkyphat.HEIGHT - bulb_width) / 2
hi_temp = 50
low_temp = -20
lowpoint = margin_bottom
hipoint = inkyphat.WIDTH - margin_top
# bulb_open_left =
# bulb_open_right =

def draw_bulb():
    # Main bulb
    inkyphat.arc((lowpoint, margin_left, lowpoint+bulb_width, margin_left+bulb_width), 30, 330, 1)
    inkyphat.arc((lowpoint-1, margin_left-1, lowpoint+bulb_width+1, margin_left+bulb_width+1), 30, 330, 1)

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
    # Scale
    inkyphat.line((202, 20, 202, 36), 1, 1)

#test = "20 \xb0"

#inkyphat.text((180, 15), test, inkyphat.BLACK, font).rotate(90)

draw_bulb()
draw_tube()
fill_up()
decorate()

inkyphat.show()
