"""temporary file docstring"""

import numpy as np
import cv2
from mss import mss
import imageio
import time


FRAME_LIST = []
maxRecordTime = 10
FPS = 10

def windowLoop(sct):
    cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Live',720,480)
    cv2.createButton("Start",startButton,None,cv2.QT_PUSH_BUTTON,0)
    cv2.createTrackbar('Seconds', 'Live', 0, 100, onSliderChange)
    while(cv2.getWindowProperty('Live', cv2.WND_PROP_VISIBLE) != 0):
        img = sct.grab(sct.monitors[1])
        frame = np.array(img)
        frame = cv2.resize(frame,(720,480))
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow('Live',frame)
        cv2.waitKey(1)




def startButton():
    cv2.destroyAllWindows()

def onSliderChange(value):
    maxRecordTime = value
    print(value)


def convertToGif(lst):
    for x in lst:
        frame = np.array(x)
        frame = cv2.resize(frame, (720,480))
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_LIST.append(frame)
    imageio.mimsave('test.gif', FRAME_LIST, fps=FPS)

def main():
    """main function"""
    sct_img_list = []
    sct = mss()
    windowLoop(sct)
    


    countdown = maxRecordTime*FPS
    cv2.destroyAllWindows()
    while countdown > 0:
        sct_img = sct.grab(sct.monitors[1])
        sct_img_list.append(sct_img)
        time.sleep(1/FPS) # Wait 1/fps
        countdown -= 1
    
    print("\nConverting to GIF...\n")
    convertToGif(sct_img_list)
    
    
    

if __name__ == "__main__":
    main()


