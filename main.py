"""temporary file docstring"""

# pylint: disable=redefined-outer-name, global-statement

from threading import Thread
import numpy as np
import cv2
from mss import mss

FRAME_LIST = []
RECORDING = True

OUT = cv2.VideoWriter('test.avi', cv2.VideoWriter_fourcc(*"XVID"), 60, (1920, 1080))

def save_frame():
    """function for frame writing thread"""
    count = 0

    while RECORDING or len(FRAME_LIST) > 0:
        if len(FRAME_LIST) > 0:
            print(count)
            count += 1

            current_frame = FRAME_LIST.pop(0)

            OUT.write(current_frame)

    OUT.release()

def main():
    """main function"""
    global RECORDING

    writer_thread = Thread(target = save_frame)

    sct = mss()

    cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

    countdown = 300

    writer_thread.start()

    while countdown > 0:
        sct_img = sct.grab(sct.monitors[1])

        frame = np.array(sct_img)

        frame = cv2.resize(frame, (1920, 1080))
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        FRAME_LIST.append(frame)

        cv2.imshow('Live', frame)
        cv2.resizeWindow("Live", 480, 270)

        countdown -= 1
        if cv2.waitKey(1) == ord('q'):
            break

    RECORDING = False

    writer_thread.join()

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
