# Test

import matplotlib.pyplot as plt
import numpy as np

import ms_tools


def getMasks(baseDepth, numStairs, depthThresh, dsRate, filterPx):
    masks = np.zeros((numStairs,) + baseDepth.shape, np.dtype(bool))
    maskImg = np.zeros(baseDepth.shape, np.dtype('uint8'))
    plt.figure()
    plt.imshow(maskImg, cmap=plt.cm.gray)
    plt.show(block=False)
    for stairNum in range(1, numStairs + 1):
        raw_input('Press enter to record stair ' + str(stairNum))
        depth = ms_tools.getDepth(dsRate)
        changed = (baseDepth - depth) > depthThresh
        filteredChanged = ms_tools.thinLineFilter(changed, filterPx)
        # Find average depth value of DEPTH where filteredChange is true
        depth_region = np.where(filteredChanged, depth, 0)
        average_depth = np.sum(depth_region)/np.sum(filteredChaged)

        # Stores 2d region with average depth
        masks[stairNum - 1] = [filteredChanged, average_depth]
        maskImg = np.where(filteredChanged, stairNum, maskImg)
        plt.imshow(maskImg, cmap=plt.cm.gray)
        plt.draw()
    return masks
