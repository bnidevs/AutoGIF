"""temporary file docstring"""

import numpy as np
import cv2
from mss import mss
from guiTest import App

def main():
    """main function"""
    sct = mss()
    
    cv2.namedWindow("Preview", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Preview", 480,270)
    while True:
        sct_img = sct.grab(sct.monitors[1])
        cv2.imshow("Preview", np.array(sct_img))
        
        if cv2.waitKey(1) == ord('q'):
            break
        if cv2.getWindowProperty('Preview',cv2.WND_PROP_VISIBLE) == 0:
            break
        
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
    
