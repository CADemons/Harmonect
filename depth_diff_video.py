#!/usr/bin/env python
import freenect
import cv2
import frame_convert2
import numpy as np

cv2.namedWindow('Depth')
print('Press ESC in window to stop')


def get_depth():
    return frame_convert2.pretty_depth_cv(freenect.sync_get_depth()[0])


keyHeld = False
based = False
base = np.array([])
while 1:
    depth = get_depth()
    if based:
        diff = base - depth
        vid = np.where(diff > 2, np.array([255]).astype(np.dtype('uint8')), 0)
        cv2.imshow('Depth', vid)
    else:
        cv2.imshow('Depth', depth)
    key = cv2.waitKey(10)
    if key == ord(' ') and not keyHeld:
        print 'Space pressed'
        base = depth
        based = True
        keyHeld = True
    else:
        keyHeld = False
    if key == 27:
        break
