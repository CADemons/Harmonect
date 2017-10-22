#!/usr/bin/env python
import freenect
import cv2
import frame_convert2
import numpy as np

cv2.namedWindow('Video')
print('Press ESC in window to stop')


def get_video():
    return frame_convert2.video_cv(freenect.sync_get_video()[0]).astype(np.dtype('int16'))[::1, ::1, ::1]

def get_essences():
    vid = get_video()
    totals = np.sum(vid, axis=2).astype(float)[:, :, None]
    return (np.divide(vid, totals) * vid).astype('int16')

def get_nesses():
    vid = get_video()
    totals = np.sum(vid, axis=2).astype(float)[:, :, None]
    return (np.divide(vid, totals) * 255).astype('int16')

def get_relative():
    vid = get_video()
    ref = np.average(vid[-50:, -50:], axis=(0, 1))
    return (vid / ref * 255).astype('int16')


keyHeld = False
based = False
base = np.array([])
while 1:
    data = get_essences()
    ref = np.average(data[:50, :50], axis=(0, 1))
    rgb = data - ref
    if based:
        diff = np.absolute(base - rgb)
        combDiff = diff[:, :, 1]
        vid = np.where(combDiff > 20, np.array([255]).astype(np.dtype('uint8')), 0)
        cv2.imshow('Video', vid)
    else:
        cv2.imshow('Video', rgb.astype(np.dtype('uint8')))
    key = cv2.waitKey(10)
    if key == ord(' ') and not keyHeld:
        print 'Space pressed'
        base = rgb
        based = True
        keyHeld = True
    else:
        keyHeld = False
    if key == 27:
        break
