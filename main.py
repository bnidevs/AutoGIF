"""temporary file docstring"""

# pylint: disable=redefined-outer-name

import numpy as np
import cv2
from mss import mss
from PIL import Image

box = {'left': 0, 'top': 0, 'width': 200, 'height': 200}

def gcd(a,b):
	if b == 0:
		return a
	return gcd(b, a % b)

def get_aspect_ratio(width, height):
	factor = gcd(width, height)
	return (width / factor, height / factor)

def zoom_in(speed, aspect_ratio):
    """zoom in based on aspect ratio"""
    box['width'] -= aspect_ratio[0] * speed
    box['height'] -= aspect_ratio[1] * speed

def zoom_out(speed, aspect_ratio):
    """opposite of zoom in"""
    zoom_in(-1 * speed)

def main():
    """main function"""
    sct = mss()
    # take a screenshot of the screen and use that to determine the user's screen size
    sizing_sct = sct.grab(sct.monitors[1])
    box = {'left': 0, 'top': 0, 'width': sizing_sct.width, 'height': sizing_sct.height}
    aspect_ratio = get_aspect_ratio(sizing_sct.width, sizing_sct.height)

    cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

    countdown = 800

    while countdown > 0:
        sct_img = sct.grab(box)
        img = Image.frombytes(
            'RGB',
            (sct_img.width, sct_img.height),
            sct_img.rgb,
        )
        cv2.imshow('Live', np.array(img))
        cv2.resizeWindow("Live", width, height)

        countdown -= 1
        cv2.waitKey(1)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
