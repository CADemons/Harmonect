import numpy as np

import ms_tools


def getStepArr(masks, base, depth, depthThresh, filterPx, coverThresh):
    # Pixels where depth has changed since the base image (where people are standing)
    changed = (base - depth) > depthThresh
    # Remove thin-line noise from `changed`
    filteredChanged = ms_tools.thinLineFilter(changed, filterPx)
    # Show pixels with changed depth as gray in the video
    vid = np.where(filteredChanged, 150, 0)

    numStairs = masks.shape[0]
    activeStairs = np.zeros(numStairs, np.dtype(bool))
    # For each stair:
    for stairNum in range(0, numStairs):
        mask = masks[stairNum]
        area = np.sum(mask)
        # Find where the mask overlaps with where people are currently standing
        coverageArr = np.logical_and(mask, filteredChanged)
        # Area of this overlap
        covered = np.sum(coverageArr)
        # If the area of the overlap is large enough (relative to the area of
        # the mask), set the stair to active and show the mask in white on the video.
        if (float(covered) / float(area)) >= coverThresh:
            activeStairs[stairNum] = True
            vid = np.where(mask, 255, vid)
        else:
            activeStairs[stairNum] = False
    return activeStairs, vid.astype(np.dtype('uint8'))
