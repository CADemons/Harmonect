import matplotlib.pyplot as plt
import numpy as np

import ms_tools


def getMasks(baseDepth, numStairs, depthThresh, dsRate, filterPx):
    # A "mask" is an image-size 2d boolean array for each stair,
    # true where the pixel location is part of the region triggering
    # the stair. `masks` is an array of these masks, one for each stair.
    masks = np.zeros((numStairs,) + baseDepth.shape, np.dtype(bool))
    # Image of masks for display during calibration
    maskImg = np.zeros(baseDepth.shape, np.dtype('uint8'))
    plt.figure()
    # maskImg is blank for this display
    plt.imshow(maskImg, cmap=plt.cm.gray)
    plt.show(block=False)
    for stairNum in range(1, numStairs + 1):
        raw_input('Press enter to record stair ' + str(stairNum))
        depth = ms_tools.getDepth(dsRate)
        # Pixels where depth has changed since the base image
        # (where people are standing)
        changed = (baseDepth - depth) > depthThresh
        # Remove thin-line noise from `changed`
        filteredChanged = ms_tools.thinLineFilter(changed, filterPx)
        # Set the mask for each stair to its filteredChanged calibration image
        masks[stairNum - 1] = filteredChanged
        # Overlay mask on maskImg and display
        maskImg = np.where(filteredChanged, stairNum, maskImg)
        plt.imshow(maskImg, cmap=plt.cm.gray)
        plt.draw()
    return masks
