from scipy import ndimage
import freenect
import frame_convert2


def getDepth(dsRate):
    return frame_convert2.pretty_depth_cv(freenect.sync_get_depth()[0])[::dsRate, ::dsRate]


def thinLineFilter(img, filterPx):
    opened = ndimage.binary_opening(img, iterations=filterPx)
    return opened
