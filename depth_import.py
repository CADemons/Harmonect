#!/usr/bin/env python
import sys
import freenect
import cv2
import numpy as np

cv2.namedWindow('Depth')
depth = np.loadtxt(sys.argv[1], dtype=np.dtype('u1'), delimiter=',')
while 1:
    cv2.imshow('Depth', depth)
    if cv2.waitKey(100) == 27:
        break
