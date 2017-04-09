#!/usr/bin/env python
import freenect
import cv2
import frame_convert2
import numpy as np

cv2.namedWindow('Depth')
print('Press ESC in window to stop')


def get_depth():
    depth = frame_convert2.pretty_depth_cv(freenect.sync_get_depth()[0])
    return np.where(np.array(depth) == 255, 0, 255).astype(np.dtype('uint8'))


keyHeld = False
while 1:
    depth = get_depth()
    cv2.imshow('Depth', depth)
    key = cv2.waitKey(10)
    if key == ord(' ') and not keyHeld:
        print 'Space pressed'
        print depth
        print depth.dtype
        keyHeld = True
    else:
        keyHeld = False
    if key == 27:
        break
