#!/usr/bin/env python
import freenect
import cv2
import frame_convert2
import csv
import numpy

cv2.namedWindow('Depth')
cv2.namedWindow('Video')
print('Press ESC in window to stop')


def get_depth():
    return frame_convert2.pretty_depth_cv(freenect.sync_get_depth()[0])


def get_video():
    return frame_convert2.video_cv(freenect.sync_get_video()[0])


keyHeld = False;
while 1:
    depth = get_depth()
    cv2.imshow('Depth', depth)
    cv2.imshow('Video', get_video())
    key = cv2.waitKey(10)
    if key == ord(' ') and not keyHeld:
        print "Space pressed"
        numpy.savetxt('data.csv', depth, fmt='%d', delimiter=',')
        keyHeld = True;
    else:
        keyHeld = False;
    if key == 27:
        break
