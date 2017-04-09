import matplotlib.pyplot as plt
import numpy as np

import ms_tools


def getMasks(baseDepth, numStairs, depthThresh, dsRate, filterPx):
    height = int(480 / dsRate)
    width = int(640 / dsRate)
    masks = np.zeroes((numStairs, height, width), np.dtype(bool))
    maskImg = np.zeroes((height, width), np.dtype('uint8'))
    plt.figure()
    plt.imshow(maskImg)
    plt.show(block=False)
    for stairNum in range(1, numStairs + 1):
        raw_input('Press enter to record stair ' + str(stairNum))
        depth = ms_tools.getDepth(dsRate)
        changed = (baseDepth - depth) > depthThresh
        filteredChanged = ms_tools.thinLineFilter(changed, filterPx)
        masks[stairNum - 1] = filteredChanged
        maskImg = np.where(filteredChanged, stairNum, maskImg)
        plt.imshow(maskImg)
    return masks
