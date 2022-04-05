"""temporary file docstring"""

import numpy as np
import cv2
from mss import mss
import imageio
import time
import guiTest as gui
import tkinter as tnk

FRAME_LIST = []
MAXRECORDTIME = 1
FPS = 30
DELAY = 1
master = tnk.Tk()
master.title('AutoGIF')
master.geometry('320x180')

def windowLoop(sct):
    global master
    global MAXRECORDTIME
    global DELAY
    ap = gui.App(master=master)
    ap.run()
    MAXRECORDTIME = ap.recordTime
    DELAY = ap.delayTime
    cv2.namedWindow("Preview")
    cv2.resizeWindow('Preview',720,480)
    
    
    while(cv2.getWindowProperty('Preview', cv2.WND_PROP_VISIBLE) != 0):
        img = sct.grab(sct.monitors[1])
        frame = np.array(img)
        frame = cv2.resize(frame,(720,480))
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow('Preview',frame)
        if cv2.waitKey(1) == ord('q'):
            break

def convertToGif(lst):
    global FPS
    global FRAME_LIST
    for x in lst:
        frame = np.array(x)
        frame = cv2.resize(frame, (720,480))
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_LIST.append(frame)
    imageio.mimsave('output.gif', FRAME_LIST, fps=FPS)

def main():
    """main function"""
    global FPS
    global DELAY
    global MAXRECORDTIME
    global FRAME_LIST
    sct_img_list = []
    sct = mss()
    windowLoop(sct)

    countdown = MAXRECORDTIME*FPS
    cv2.destroyAllWindows()
    while DELAY > 0:
        time.sleep(1)
        print(DELAY)
        DELAY -= 1
    print("\nRecording...\n")
    while countdown > 0:
        sct_img = sct.grab(sct.monitors[1])
        sct_img_list.append(sct_img)
        time.sleep(1/FPS) # Wait 1/fps
        countdown -= 1
    
    print("\nConverting to GIF...\n")
    convertToGif(sct_img_list)
    print("\nRecording time: ", MAXRECORDTIME)

if __name__ == "__main__":
    main()


