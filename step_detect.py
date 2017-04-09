import numpy as np

import ms_tools


def getStepArr(masks, base, depth, depthThresh, filterPx, coverThresh):
    changed = (base - depth) > depthThresh
    filteredChanged = ms_tools.thinLineFilter(changed, filterPx)
    vid = np.where(filteredChanged, 150, 0)

    numStairs = masks.shape[0]
    activeStairs = np.zeros(numStairs, np.dtype(bool))
    for stairNum in range(0, numStairs):
        mask = masks[stairNum]
        area = np.sum(mask)
        coverageArr = np.logical_and(mask, filteredChanged)
        covered = np.sum(coverageArr)
        if (float(covered) / float(area)) >= coverThresh:
            activeStairs[stairNum] = True
            vid = np.where(mask, 255, vid)
        else:
            activeStairs[stairNum] = False
    return activeStairs, vid.astype(np.dtype('uint8'))
