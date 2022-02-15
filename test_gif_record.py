"""temporary file docstring"""

import numpy as np
import cv2
from mss import mss
import imageio

FRAME_LIST = []

def main():
    """main function"""

    sct = mss()

    cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

    countdown = 300

    while countdown > 0:
        sct_img = sct.grab(sct.monitors[1])

        frame = np.array(sct_img)

        frame = cv2.resize(frame, (720, 480))
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        FRAME_LIST.append(frame)

        cv2.imshow('Live', frame)
        cv2.resizeWindow("Live", 480, 270)

        countdown -= 1
        cv2.waitKey(1)
        
        if cv2.getWindowProperty('Live', cv2.WND_PROP_VISIBLE) == 0:
            break

    cv2.destroyAllWindows()
    imageio.mimsave('test.gif', FRAME_LIST, fps=60)

if __name__ == "__main__":
    main()
