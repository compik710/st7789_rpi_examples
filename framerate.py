#!/usr/bin/env python3
import time
import math
import sys

from PIL import Image
from PIL import ImageDraw
import ST7789 as ST7789

# Higher SPI bus speed = higher framerate
SPI_SPEED_MHZ = 80
display_type = "square"

print("""
framerate.py - Test monitor framerate.

Running at: {}MHz on a {} display.
Calculation started, please wait a results.
""".format(SPI_SPEED_MHZ, display_type))

# Create ST7789 LCD display class.
disp = ST7789.ST7789( port=0, cs=ST7789.BG_SPI_CS_FRONT, dc=24, rst=25, backlight=27, mode=3, spi_speed_hz=80 * 1000 * 1000 )

WIDTH = disp.width
HEIGHT = disp.height
STEPS = WIDTH * 2
images = []

for step in range(STEPS):
    image = Image.new("RGB", (WIDTH, HEIGHT), (0, 0, 128))
    draw = ImageDraw.Draw(image)

    if step % 2 == 0:
        draw.rectangle((120, 120, 240, 240), (0, 128, 0))
    else:
        draw.rectangle((0, 0, 119, 119), (0, 128, 0))

    f = math.sin((float(step) / STEPS) * math.pi)
    offset_left = int(f * WIDTH)
    draw.ellipse((offset_left, 35, offset_left + 10, 45), (255, 0, 0))

    images.append(image)

count = 0
time_start = time.time()

while True:
    disp.display(images[count % len(images)])
    count += 1
    time_current = time.time() - time_start
    if count % 120 == 0:
        print("Time: {:8.3f},      Frames: {:6d},      FPS: {:8.3f}".format(
            time_current,
            count,
            count / time_current))
