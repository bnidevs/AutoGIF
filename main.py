"""temporary file docstring"""

import numpy as np
import cv2
from mss import mss
from PIL import Image

box = {'left': 0, 'top': 0, 'width': 200, 'height': 200}

# add some way to zoom based on aspect ratio instead of arbitrary values
def zoom_in(speed):
	box['left'] += 2*speed
	box['top'] += speed
	box['width'] -= 4*speed
	box['height'] -= 2*speed

def zoom_out(speed):
	zoom_in(-1 * speed)

def main():
    """main function"""
    sct = mss()
    # take a screenshot of the screen and use that to determine the user's screen size
    sizing_sct = sct.grab(sct.monitors[1])
    box['width'] = sizing_sct.width
    box['height'] = sizing_sct.height

    cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

    countdown = 400

    while countdown > 0:
        sct_img = sct.grab(box)
        img = Image.frombytes(
            'RGB', 
            (sct_img.width, sct_img.height), 
            sct_img.rgb, 
        )
        cv2.imshow('Live', np.array(img))
        cv2.resizeWindow("Live", 480, 270)
        
        if countdown % 2 == 0:
        	zoom_in(1)
        
        countdown -= 1
        cv2.waitKey(1)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
