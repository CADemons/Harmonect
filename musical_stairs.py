import os
import sys
import time
import cv2
import matplotlib.pyplot as plt

import ms_tools
import auto_calib
import step_detect
# import music


if __name__ == '__main__':
    if os.geteuid() != 0:
        sys.exit('Error: This program must be run as root')
    if len(sys.argv) != 7:
        sys.exit('Usage: musical_stairs.py numStairs depthThreshold downsampleRate waitMs filterPx coverageThresh')
    numStairs = int(sys.argv[1])
    depthThresh = int(sys.argv[2])
    dsRate = int(sys.argv[3])
    waitMs = int(sys.argv[4])
    filterPx = int(sys.argv[5])
    coverThresh = float(sys.argv[6])

    base = ms_tools.getDepth(dsRate)
    time.sleep(.5)
    base = ms_tools.getDepth(dsRate)
    plt.figure()
    plt.imshow(base, cmap=plt.cm.gray)
    plt.show(block=False)

    masks = auto_calib.getMasks(base, numStairs, depthThresh, dsRate, filterPx)
    spaceHeld = False
    cv2.namedWindow('Depth')
    print('Press ESC in window to stop')
    while 1:
        depth = ms_tools.getDepth(dsRate)

        steps, vid = step_detect.getStepArr(masks, base, depth, depthThresh, filterPx, coverThresh)
        cv2.imshow('Depth', vid)
        key = cv2.waitKey(waitMs)

        # music.processSteps(steps)

        if key == ord(' ') and not spaceHeld:
            print 'Base reset'
            base = depth
            spaceHeld = True
        else:
            spaceHeld = False
        if key == 27:  # ESC
            break
