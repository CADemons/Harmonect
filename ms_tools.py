from scipy import ndimage
import numpy as np
import freenect
import frame_convert2

def getMetric(dsRate):
    return getColorEssence(dsRate, 1)

def getDepth(dsRate):
    return frame_convert2.pretty_depth_cv(freenect.sync_get_depth()[0])[::dsRate, ::dsRate]

def getVideo(dsRate):
    return frame_convert2.video_cv(freenect.sync_get_video()[0]).astype(np.dtype('int16'))[::dsRate, ::dsRate, :]

def getColorEssence(dsRate, color):
    vid = getVideo()
    totals = np.sum(vid, axis=2).astype(float)
    colorVals = vid[:, :, color]
    return (np.divide(colorVals, totals) * colorVals).astype('int16')

def thinLineFilter(img, filterPx):
    opened = ndimage.binary_opening(img, iterations=filterPx)
    return opened
