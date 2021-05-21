#!/usr/bin/env python3
import sys, time, cv2
from random import randint

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import ST7789

print("\ncamera.py - Showing image from camera.\n")

# Open capture
cap = cv2.VideoCapture(0)

# Create ST7789 LCD display class.
disp = ST7789.ST7789( port=0, cs=ST7789.BG_SPI_CS_FRONT, dc=24, rst=25, backlight=27, mode=3, spi_speed_hz=80 * 1000 * 1000 ) 
# Initialize display.
disp.begin()

WIDTH = 240
HEIGHT = 240

while 1:
	_, frame = cap.read()
	frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
	disp.display(Image.fromarray(frame).resize((240,240)))
	cv2.waitKey(10)

# Write buffer to display hardware, must be called to make things visible on the
# display!