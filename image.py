#!/usr/bin/env python3
import sys

from PIL import Image
import ST7789 as ST7789

print("""
image.py - Display techno spros image.

""")

image_file = "techno_sp.jpg"
display_type = "square"
dc = 24
rst = 25
bl = 27

# Create ST7789 LCD display class.
disp = ST7789.ST7789( port=0, cs=ST7789.BG_SPI_CS_FRONT, dc=dc, rst=rst, backlight=bl, mode=3, spi_speed_hz=80 * 1000 * 1000 ) 

WIDTH = disp.width
HEIGHT = disp.height

# Initialize display.
disp.begin()

# Load an image.
print('Loading image: {}...'.format(image_file))
image = Image.open(image_file)

# Resize the image
image = image.resize((WIDTH, HEIGHT))

# Draw the image on the display hardware.
print('Showing...')

disp.display(image)

print("Showed!")