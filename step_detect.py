import numpy as np

import ms_tools

# Uncertainty around average depth
UNCERT = 10

def getStepArr(masks, base, depth, depthThresh, filterPx, coverThresh):

    changed = (base - depth) > depthThresh
    filteredChanged = ms_tools.thinLineFilter(changed, filterPx)
    vid = np.where(filteredChanged, 150, 0)

    numStairs = masks.shape[0]
    activeStairs = np.zeros(numStairs, np.dtype(bool))
    for stairNum in range(0, numStairs):
        # Retrieving region
        mask = masks[stairNum, 0]

        # Retrieving Average depth value
        maskAvgDepth = masks[stairNum, 1]
        
        area = np.sum(mask)
        coverageArr = np.logical_and(mask, filteredChanged)
        coveredDepths = np.where(coverageArr, depth, 0)
        avgCoveredDepth = np.sum(coveredDepths) / np.sum(coverageArr)
        
        covered = np.sum(coverageArr)
        if (float(covered) / float(area)) >= coverThresh and avgCoveredDepth > maskAvgDepth - UNCERT and avgCoveredDepth < maskAvgDepth + UNCERT:
            activeStairs[stairNum] = True
            vid = np.where(mask, 255, vid)
        else:
            activeStairs[stairNum] = False
    return activeStairs, vid.astype(np.dtype('uint8'))
