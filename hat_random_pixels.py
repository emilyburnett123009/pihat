#!/usr/bin/env python
# this script will show a matrix of colors on the Pi HAT
from sense_hat import SenseHat
sense = SenseHat()
r = (255, 0, 125)
b = (0, 0, 225)

pixels = [
    b, r, r, b, r, r, b, b, 
    r, r, r, r, r, r, r, b, 
    r, r, r, r, r, r, r, b, 
    r, r, r, r, r, r, r, b, 
    b, r, r, r, r, r, b, b, 
    b, b, r, r, r, b, b, b, 
    b, b, b, r, b, b, b, b, 
    b, b, b, b, b, b, b, b, 
]

sense.set_pixels(pixels)
