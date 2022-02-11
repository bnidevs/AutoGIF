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

def main():
    """main function"""
    sct = mss()
    # take a screenshot of the screen and use that to determine the user's screen size
    sizing_sct = sct.grab(sct.monitors[1])
    scr_width = sizing_sct.width
    scr_height = sizing_sct.height
    box = {'left': 0, 'top': 0, 'width': scr_width, 'height': scr_height}
    aspect_ratio = get_aspect_ratio(scr_width, scr_height)

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
        cv2.resizeWindow("Live", 720, 480)

        countdown -= 1
        if cv2.waitKey(1) == ord('q'):
        	break
        if cv2.getWindowProperty('Live',cv2.WND_PROP_VISIBLE) == 0:
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
