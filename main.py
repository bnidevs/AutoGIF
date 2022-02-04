"""temporary file docstring"""

import numpy as np
import cv2
from mss import mss
from PIL import Image

def main():
    """main function"""
    sct = mss()
    # take a screenshot of the screen and use that to determine the user's screen size
    sizing_sct = sct.grab(sct.monitors[1])
    box = {'left': 0, 'top': 0, 'width': sizing_sct.width, 'height': sizing_sct.height}

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

        countdown -= 1
        cv2.waitKey(1)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
