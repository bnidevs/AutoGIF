"""temporary file docstring"""

import numpy as np
import cv2
from mss import mss

def main():
    """main function"""
    sct = mss()

    cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

    countdown = 400

    while countdown > 0:
        sct_img = sct.grab(sct.monitors[1])
        cv2.imshow('Live', np.array(sct_img))
        cv2.resizeWindow("Live", 480, 270)

        countdown -= 1
        cv2.waitKey(1)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
